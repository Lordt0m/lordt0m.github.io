import json
import uuid
from functools import wraps
from django.db import OperationalError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from . import services as s
from .models import Order


def endpoint(methods):
    def decorate(fn):
        @wraps(fn)
        def wrapped(request, **kwargs):
            if request.method not in methods:
                response = JsonResponse({'error': 'Method not allowed.'}, status=405)
                response['Allow'] = ', '.join(methods)
                return response
            if not request.session.get('workspace'):
                return JsonResponse({'error': 'Open the demo first to start a workspace.'}, status=401)
            try:
                response = fn(request, **kwargs)
            except s.Problem as exc:
                response = JsonResponse({'error': exc.message}, status=exc.code)
            except (json.JSONDecodeError, UnicodeDecodeError):
                response = JsonResponse({'error': 'Send a valid JSON object.'}, status=400)
            except OperationalError:
                response = JsonResponse({'error': 'The demo database is busy. Retry the same request key.'}, status=503)
                response['Retry-After'] = '1'
            response['Cache-Control'] = 'no-store'
            return response
        return wrapped
    return decorate


def body(request):
    if request.content_type != 'application/json':
        raise s.Problem('Send application/json.', 415)
    result = json.loads(request.body)
    if not isinstance(result, dict):
        raise s.Problem('Send a JSON object.')
    return result


@ensure_csrf_cookie
def index(request):
    return render(request, 'counter.html')


def health(request):
    return JsonResponse({'status': 'ok', 'service': 'orderlane'})


@ensure_csrf_cookie
def bootstrap(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    if not request.session.get('workspace'):
        workspace = str(uuid.uuid4())
        s.seed(workspace)
        request.session['workspace'] = workspace
        request.session['role'] = 'customer'
    response = JsonResponse({'restaurants': s.RESTAURANTS, 'menu': s.MENU,
                             'role': request.session.get('role', 'customer'),
                             'workspace': request.session['workspace'],
                             'demo': True, 'storage': 'Temporary SQLite demo; records may reset on service restart.'})
    response['Cache-Control'] = 'no-store'
    return response


@endpoint(['POST'])
def role(request):
    selected = body(request).get('role')
    if selected not in ['customer', *s.RESTAURANTS]:
        raise s.Problem('Choose a demo customer or a listed vendor.')
    request.session['role'] = selected
    return JsonResponse({'role': selected, 'demo_role_switch': True})


@endpoint(['GET', 'POST'])
def orders(request):
    workspace, role = request.session['workspace'], request.session.get('role', 'customer')
    if request.method == 'POST':
        if role != 'customer':
            raise s.Problem('Switch to the customer view to place an order.', 403)
        order, created = s.create_order(workspace, body(request), request.headers.get('Idempotency-Key'))
        return JsonResponse({'order': s.serialise(order), 'created': created}, status=201 if created else 200)
    query = Order.objects.filter(workspace=workspace)
    if role != 'customer':
        query = query.filter(restaurant=role)
    return JsonResponse({'orders': [s.serialise(order) for order in query.order_by('-created_at')]})


@endpoint(['GET'])
def detail(request, order_id):
    return JsonResponse({'order': s.serialise(s.get_order(request.session['workspace'], order_id,
                                                          request.session.get('role', 'customer')))})


@endpoint(['POST'])
def status(request, order_id):
    return JsonResponse({'order': s.serialise(s.advance(request.session['workspace'], order_id,
                                                        request.session.get('role', 'customer'), body(request)))})
