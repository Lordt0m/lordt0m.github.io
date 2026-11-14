import hashlib
import json
import uuid
from django.db import IntegrityError, transaction
from .models import Event, Order

RESTAURANTS = {
    'lagos': {'name': 'Lagos Kitchen', 'description': 'Comfort food, made for your lunch break.', 'prep': '20–30 min'},
    'ember': {'name': 'Ember & Grain', 'description': 'Smoky grills and generous bowls.', 'prep': '25–35 min'},
}
MENU = {
    'jollof': {'restaurant': 'lagos', 'name': 'Party jollof & chicken', 'description': 'Smoky rice, grilled chicken, sweet plantain.', 'price': 4500, 'category': 'House favourite'},
    'egusi': {'restaurant': 'lagos', 'name': 'Egusi & pounded yam', 'description': 'Melon-seed soup, tender beef, soft pounded yam.', 'price': 5200, 'category': 'From the pot'},
    'beans': {'restaurant': 'lagos', 'name': 'Beans & plantain', 'description': 'Slow-cooked honey beans with golden plantain.', 'price': 2800, 'category': 'Vegetarian'},
    'amala': {'restaurant': 'lagos', 'name': 'Amala, ewedu & gbegiri', 'description': 'Yam-flour swallow, jute-leaf and bean soups, beef stew.', 'price': 4800, 'category': 'From the pot'},
    'ofada': {'restaurant': 'lagos', 'name': 'Ofada rice & ayamase', 'description': 'Local rice, green pepper sauce and tender beef.', 'price': 5000, 'category': 'House favourite'},
    'moi-moi': {'restaurant': 'lagos', 'name': 'Moi moi & pap', 'description': 'Steamed bean pudding with smooth maize pap. No egg, fish or meat.', 'price': 2500, 'category': 'Vegetarian'},
    'suya': {'restaurant': 'ember', 'name': 'Suya rice bowl', 'description': 'Spiced beef, seasoned rice, crunchy slaw.', 'price': 4800, 'category': 'Off the grill'},
    'chicken': {'restaurant': 'ember', 'name': 'Grilled chicken bowl', 'description': 'Charred chicken, herbed grains, pepper sauce.', 'price': 5500, 'category': 'House favourite'},
    'waakye': {'restaurant': 'ember', 'name': 'Waakye & egg', 'description': 'Ghanaian rice and beans, boiled egg and shito pepper sauce.', 'price': 4200, 'category': 'House favourite'},
    'thieboudienne': {'restaurant': 'ember', 'name': 'Thieboudienne', 'description': 'Senegalese tomato rice, fish, cabbage, carrot and cassava.', 'price': 6000, 'category': 'From the pot'},
    'ndole': {'restaurant': 'ember', 'name': 'Ndole & plantain', 'description': 'Cameroonian bitterleaf and groundnut stew with beef and boiled plantain.', 'price': 5800, 'category': 'From the pot'},
    'peri-peri': {'restaurant': 'ember', 'name': 'Peri-peri chicken & rice', 'description': 'Mozambican-style chilli-grilled chicken with seasoned rice.', 'price': 5600, 'category': 'Off the grill'},
}
NEXT = {'placed': 'accepted', 'accepted': 'preparing', 'preparing': 'ready', 'ready': 'completed'}


class Problem(Exception):
    def __init__(self, message, code=400):
        self.message, self.code = message, code


def serialise(order):
    return {'id': str(order.id), 'restaurant': order.restaurant,
            'demo_sample': order.request_key.startswith('seed-'),
            'restaurant_name': RESTAURANTS[order.restaurant]['name'], 'items': order.items,
            'total': order.total, 'status': order.status, 'revision': order.revision,
            'created_at': order.created_at.isoformat(),
            'events': [{'status': e.status, 'actor': e.actor, 'at': e.created_at.isoformat()}
                       for e in order.events.order_by('id')]}


def create_order(workspace, payload, key):
    if not isinstance(key, str) or not 8 <= len(key) <= 80:
        raise Problem('Send an Idempotency-Key between 8 and 80 characters.')
    restaurant = payload.get('restaurant')
    if not isinstance(restaurant, str) or restaurant not in RESTAURANTS:
        raise Problem('Choose a listed restaurant.')
    rows = payload.get('items')
    max_meals = sum(meal['restaurant'] == restaurant for meal in MENU.values())
    if not isinstance(rows, list) or not 1 <= len(rows) <= max_meals:
        raise Problem(f'Choose between one and {max_meals} different meals from this kitchen.')
    items, seen = [], set()
    for row in rows:
        if not isinstance(row, dict):
            raise Problem('Each item must contain a meal and quantity.')
        meal, qty = row.get('meal'), row.get('quantity')
        if not isinstance(meal, str) or meal not in MENU or MENU[meal]['restaurant'] != restaurant:
            raise Problem('Every meal must belong to the selected restaurant.')
        if type(qty) is not int or not 1 <= qty <= 10 or meal in seen:
            raise Problem('Use a quantity from 1 to 10 and list each meal once.')
        seen.add(meal)
        items.append({'meal': meal, 'name': MENU[meal]['name'], 'quantity': qty, 'price': MENU[meal]['price']})
    items.sort(key=lambda item: item['meal'])
    digest = hashlib.sha256(json.dumps({'restaurant': restaurant, 'items': items}, sort_keys=True).encode()).hexdigest()

    def replay(existing):
        if existing.request_hash != digest:
            raise Problem('This request key was already used for a different order.', 409)
        return existing, False

    existing = Order.objects.filter(workspace=workspace, request_key=key).first()
    if existing:
        return replay(existing)
    try:
        with transaction.atomic():
            if Order.objects.filter(workspace=workspace).count() >= 40:
                raise Problem('This demo workspace has reached 40 orders. Open a new browser session.', 429)
            order = Order.objects.create(workspace=workspace, restaurant=restaurant, request_key=key,
                                         request_hash=digest, items=items,
                                         total=sum(item['price'] * item['quantity'] for item in items))
            Event.objects.create(order=order, status='placed', actor='customer')
            return order, True
    except IntegrityError:
        return replay(Order.objects.get(workspace=workspace, request_key=key))


def get_order(workspace, order_id, role):
    query = Order.objects.filter(workspace=workspace, id=order_id)
    if role != 'customer':
        query = query.filter(restaurant=role)
    order = query.first()
    if not order:
        raise Problem('Order not found in this workspace and restaurant.', 404)
    return order


def advance(workspace, order_id, role, payload):
    if role not in RESTAURANTS:
        raise Problem('Switch to the vendor desk to change an order.', 403)
    order = get_order(workspace, order_id, role)
    revision, target = payload.get('revision'), payload.get('status')
    if type(revision) is not int or revision != order.revision:
        raise Problem('This order changed. Refresh before trying again.', 409)
    if target != NEXT.get(order.status):
        raise Problem('That status change is not allowed.', 409)
    with transaction.atomic():
        changed = Order.objects.filter(id=order.id, workspace=workspace, restaurant=role,
                                       revision=revision, status=order.status).update(status=target, revision=revision + 1)
        if not changed:
            raise Problem('Another update won. Refresh this order.', 409)
        Event.objects.create(order=order, status=target, actor='vendor:' + role)
    order.refresh_from_db()
    return order


def seed(workspace):
    for restaurant, meal in [('lagos', 'jollof'), ('ember', 'suya')]:
        create_order(workspace, {'restaurant': restaurant, 'items': [{'meal': meal, 'quantity': 1}]}, 'seed-' + restaurant)
