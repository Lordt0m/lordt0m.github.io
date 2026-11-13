import json
from django.test import Client, TestCase
from .models import Event, Order


class OrderAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.get('/api/bootstrap/')
        self.payload = {'restaurant': 'lagos', 'items': [{'meal': 'jollof', 'quantity': 2}]}

    def post(self, path, data, client=None, key=None):
        headers = {'HTTP_IDEMPOTENCY_KEY': key} if key else {}
        return (client or self.client).post(path, data=json.dumps(data), content_type='application/json', **headers)

    def create(self, key='request-0001', payload=None):
        return self.post('/api/orders/', payload or self.payload, key=key)

    def role(self, role, client=None):
        return self.post('/api/role/', {'role': role}, client=client)

    def test_new_order_uses_server_prices_and_one_event(self):
        self.payload['total'] = 1
        self.payload['items'][0]['price'] = 1
        response = self.create()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['order']['total'], 9000)
        self.assertEqual(len(response.json()['order']['events']), 1)

    def test_identical_replay_returns_original(self):
        first = self.create()
        second = self.create()
        self.assertEqual(second.status_code, 200)
        self.assertFalse(second.json()['created'])
        self.assertEqual(first.json()['order']['id'], second.json()['order']['id'])
        self.assertEqual(Order.objects.filter(request_key='request-0001').count(), 1)

    def test_key_cannot_be_reused_for_different_payload(self):
        self.create()
        self.payload['items'][0]['quantity'] = 3
        self.assertEqual(self.create().status_code, 409)

    def test_cross_restaurant_read_and_write_are_hidden(self):
        order = self.create().json()['order']
        self.role('ember')
        self.assertEqual(self.client.get(f"/api/orders/{order['id']}/").status_code, 404)
        self.assertEqual(self.post(f"/api/orders/{order['id']}/status/", {'status':'accepted','revision':0}).status_code, 404)
        self.assertTrue(all(row['restaurant'] == 'ember' for row in self.client.get('/api/orders/').json()['orders']))

    def test_separate_browser_workspaces_are_isolated(self):
        order = self.create().json()['order']
        other = Client()
        other.get('/api/bootstrap/')
        self.assertEqual(other.get(f"/api/orders/{order['id']}/").status_code, 404)
        self.role('lagos', client=other)
        self.assertEqual(other.get(f"/api/orders/{order['id']}/").status_code, 404)

    def test_customer_cannot_advance(self):
        order = self.create().json()['order']
        self.assertEqual(self.post(f"/api/orders/{order['id']}/status/", {'status':'accepted','revision':0}).status_code, 403)

    def test_vendor_cannot_create_customer_order(self):
        self.role('lagos')
        self.assertEqual(self.create().status_code, 403)

    def test_complete_valid_lifecycle_records_events(self):
        order = self.create().json()['order']
        self.role('lagos')
        for revision, status in enumerate(['accepted','preparing','ready','completed']):
            response = self.post(f"/api/orders/{order['id']}/status/", {'status':status,'revision':revision})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['order']['revision'], revision + 1)
        self.assertEqual(Event.objects.filter(order_id=order['id']).count(), 5)

    def test_skipped_stage_does_not_change_record_or_history(self):
        order = self.create().json()['order']
        self.role('lagos')
        self.assertEqual(self.post(f"/api/orders/{order['id']}/status/", {'status':'completed','revision':0}).status_code, 409)
        self.assertEqual(Order.objects.get(id=order['id']).status, 'placed')
        self.assertEqual(Event.objects.filter(order_id=order['id']).count(), 1)

    def test_stale_revision_cannot_overwrite(self):
        order = self.create().json()['order']
        self.role('lagos')
        path = f"/api/orders/{order['id']}/status/"
        self.assertEqual(self.post(path, {'status':'accepted','revision':0}).status_code, 200)
        self.assertEqual(self.post(path, {'status':'preparing','revision':0}).status_code, 409)
        self.assertEqual(Order.objects.get(id=order['id']).status, 'accepted')
        self.assertEqual(Event.objects.filter(order_id=order['id']).count(), 2)

    def test_no_workspace_is_unauthorized(self):
        self.assertEqual(Client().get('/api/orders/').status_code, 401)

    def test_missing_idempotency_key_is_rejected(self):
        self.assertEqual(self.post('/api/orders/', self.payload).status_code, 400)

    def test_invalid_quantities_are_rejected(self):
        for quantity in [0, -1, 11, True, '2', None, 1.5]:
            with self.subTest(quantity=quantity):
                self.payload['items'][0]['quantity'] = quantity
                self.assertEqual(self.create().status_code, 400)

    def test_cross_restaurant_meal_is_rejected(self):
        self.payload['items'][0]['meal'] = 'suya'
        self.assertEqual(self.create().status_code, 400)

    def test_malformed_restaurant_is_rejected(self):
        for restaurant in [[], {}, None, 123]:
            with self.subTest(restaurant=restaurant):
                self.payload['restaurant'] = restaurant
                self.assertEqual(self.create().status_code, 400)

    def test_duplicate_meal_rows_are_rejected(self):
        self.payload['items'] *= 2
        self.assertEqual(self.create().status_code, 400)

    def test_bad_json_and_wrong_type_are_rejected(self):
        self.assertEqual(self.client.post('/api/orders/', '{', content_type='application/json').status_code, 400)
        self.assertEqual(self.post('/api/orders/', []).status_code, 400)
        self.assertEqual(self.client.post('/api/orders/', '{}', content_type='text/plain').status_code, 415)

    def test_unknown_role_is_rejected(self):
        self.assertEqual(self.role('admin').status_code, 400)

    def test_csrf_is_required_for_writes(self):
        protected = Client(enforce_csrf_checks=True)
        protected.get('/api/bootstrap/')
        self.assertEqual(self.post('/api/role/', {'role':'lagos'}, client=protected).status_code, 403)
        token = protected.cookies['csrftoken'].value
        response = protected.post('/api/role/', json.dumps({'role':'lagos'}), content_type='application/json', HTTP_X_CSRFTOKEN=token)
        self.assertEqual(response.status_code, 200)

    def test_health_and_html(self):
        self.assertEqual(self.client.get('/health/').json()['status'], 'ok')
        response = self.client.get('/')
        self.assertContains(response, 'Orderlane')
        self.assertContains(response, '/static/app.js')

    def test_seed_is_not_repeated_on_refresh(self):
        count = Order.objects.count()
        self.client.get('/api/bootstrap/')
        self.assertEqual(Order.objects.count(), count)

    def test_wrong_http_method_is_rejected(self):
        self.assertEqual(self.client.delete('/api/orders/').status_code, 405)

    def test_cart_order_does_not_change_replay_identity(self):
        self.payload['items'].append({'meal':'beans','quantity':1})
        first = self.create()
        self.payload['items'].reverse()
        replay = self.create()
        self.assertEqual(replay.status_code, 200)
        self.assertEqual(first.json()['order']['id'], replay.json()['order']['id'])
