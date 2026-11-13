/* Same-origin Django API. No client-side simulation or local-storage fallback. */
(() => {
  'use strict';
  const $ = (id) => document.getElementById(id);
  const state = { boot: null, view: 'customer', restaurant: 'lagos', vendor: 'lagos', cart: {}, orders: [], latest: null, pending: null, busy: false };
  const money = (value) => new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN', maximumFractionDigits: 0 }).format(value);
  const esc = (value) => String(value).replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const stages = ['placed', 'accepted', 'preparing', 'ready', 'completed'];
  const nextLabel = {placed: 'Accept order', accepted: 'Start preparing', preparing: 'Mark ready', ready: 'Complete collection'};
  const notice = (message, error = false) => { $('notice').textContent = message; $('notice').classList.toggle('failure', error); };
  async function request(path, options = {}) {
    const csrf = document.cookie.split('; ').find((c) => c.startsWith('csrftoken='))?.split('=')[1] || '';
    const response = await fetch(path, { credentials: 'same-origin', cache: 'no-store', ...options,
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf, ...options.headers } });
    let data;
    try { data = await response.json(); } catch { throw new Error('The API returned an unreadable response. Refresh and try again.'); }
    return { status: response.status, ok: response.ok, data };
  }
  async function api(path, options) {
    const result = await request(path, options);
    if (!result.ok) throw new Error(result.data.error || `Request failed (${result.status}).`);
    return result.data;
  }
  async function setRole(role) { await api('/api/role/', {method:'POST', body:JSON.stringify({role})}); }
  async function loadOrders() { state.orders = (await api('/api/orders/')).orders; renderOrders(); }
  function renderMenu() {
    const restaurant = state.boot.restaurants[state.restaurant];
    $('kitchen-name').textContent = restaurant.name;
    $('kitchen-description').textContent = restaurant.description;
    $('prep-time').textContent = restaurant.prep;
    $('menu').innerHTML = Object.entries(state.boot.menu).filter(([, m]) => m.restaurant === state.restaurant).map(([id, meal]) => {
      const qty = state.cart[id] || 0;
      return `<article class="meal"><div><h3>${esc(meal.name)}</h3><p>${esc(meal.description)}</p><strong>${money(meal.price)}</strong><small>${esc(meal.category)}</small></div><div class="quantity"><button data-meal="${id}" data-delta="-1" aria-label="Remove one ${esc(meal.name)}" ${!qty || state.pending ? 'disabled' : ''}>-</button><output aria-label="Quantity of ${esc(meal.name)}">${qty}</output><button data-meal="${id}" data-delta="1" aria-label="Add one ${esc(meal.name)}" ${qty >= 10 || state.pending ? 'disabled' : ''}>+</button></div></article>`;
    }).join('');
    renderBasket();
  }
  function renderBasket() {
    const rows = Object.entries(state.cart).filter(([, qty]) => qty > 0);
    $('basket').innerHTML = rows.length ? rows.map(([id, qty]) => `<div class="basket-row"><span>${qty} � ${esc(state.boot.menu[id].name)}</span><strong>${money(state.boot.menu[id].price * qty)}</strong></div>`).join('') : '<p class="empty">Your tray is empty.<br>Add something from the menu.</p>';
    $('total').textContent = money(rows.reduce((sum, [id, qty]) => sum + state.boot.menu[id].price * qty, 0));
    $('place-order').disabled = !rows.length || state.busy || !!state.pending;
    $('place-order').textContent = state.busy ? 'Placing your order.' : 'Place demo order';
    $('restaurant').disabled = !!state.pending || state.busy;
    $('retry-order').hidden = !state.pending || state.busy;
  }
  function timeline(order) {
    return `<ol class="timeline" aria-label="Order progress">${stages.map((stage, index) => {
      const event = order.events.find((e) => e.status === stage);
      return `<li class="${index <= stages.indexOf(order.status) ? 'done' : ''}">${stage[0].toUpperCase() + stage.slice(1)}${event ? `<time datetime="${esc(event.at)}">${new Date(event.at).toLocaleTimeString('en-NG', {hour:'2-digit', minute:'2-digit'})}</time>` : ''}</li>`;
    }).join('')}</ol>`;
  }
  function orderMarkup(order, vendor = false) {
    return `<article class="order"><div class="order-head"><span class="order-id">#${esc(order.id.slice(0,8).toUpperCase())} � ${esc(order.restaurant_name)}</span><span class="status ${order.status}">${order.status}</span></div><p class="order-items">${order.items.map((i) => `${i.quantity} � ${esc(i.name)}`).join('<br>')}</p><strong>${money(order.total)}</strong>${timeline(order)}${vendor && nextLabel[order.status] ? `<button class="primary" data-advance="${order.id}">${nextLabel[order.status]}</button>` : ''}</article>`;
  }
  function renderOrders() {
    const latest = state.orders.find((o) => o.id === state.latest);
    $('customer-orders').innerHTML = latest ? orderMarkup(latest) : '<p class="empty">Place an order to follow its progress here. The vendor desk also contains clearly fictional starter orders.</p>';
    $('vendor-orders').innerHTML = state.orders.length ? state.orders.map((o) => orderMarkup(o, true)).join('') : '<p class="empty">No orders for this restaurant. Place one in Customer view.</p>';
  }
  async function switchView(view) {
    if (!state.boot || state.busy) return;
    state.busy = true;
    try {
      await setRole(view === 'vendor' ? state.vendor : 'customer');
      state.view = view;
      for (const name of ['customer', 'vendor', 'engineering']) $(name + '-view').hidden = name !== view;
      document.querySelectorAll('[data-view]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.view === view)));
      await loadOrders(); notice('');
    } catch (error) { notice(error.message, true); }
    finally { state.busy = false; renderBasket(); }
  }
  async function placeOrder() {
    if (state.busy) return;
    if (!state.pending) state.pending = { key: crypto.randomUUID(), payload: {restaurant: state.restaurant, items: Object.entries(state.cart).filter(([, q]) => q > 0).map(([meal, quantity]) => ({meal, quantity}))} };
    state.busy = true; renderMenu();
    try {
      await setRole('customer');
      const data = await api('/api/orders/', {method:'POST',headers:{'Idempotency-Key':state.pending.key},body:JSON.stringify(state.pending.payload)});
      state.latest = data.order.id; state.pending = null; state.cart = {};
      await loadOrders(); notice(`Order #${state.latest.slice(0,8).toUpperCase()} ${data.created ? 'placed' : 'recovered safely'}. Open Vendor desk to accept it.`);
    } catch (error) { notice(`${error.message} Your request is saved for retry with the same key.`, true); }
    finally { state.busy = false; renderMenu(); }
  }
  async function advance(id, button) {
    if (state.busy) return;
    const order = state.orders.find((o) => o.id === id);
    state.busy = true; button.disabled = true;
    try {
      await api(`/api/orders/${id}/status/`, {method:'POST',body:JSON.stringify({status:stages[stages.indexOf(order.status)+1], revision:order.revision})});
      await loadOrders(); notice('Order updated. Its history was recorded in the same transaction.');
    } catch (error) { notice(error.message, true); await loadOrders().catch(() => {}); }
    finally {state.busy = false; button.disabled = false;}
  }
  async function runChecks() {
    if (state.busy) return;
    state.busy = true; $('run-checks').disabled = true; $('check-results').innerHTML = ''; $('api-log').textContent = '';
    const append = (message, passed) => { const item = document.createElement('li'); item.className = passed ? 'passed' : 'failed'; item.textContent = `${passed ? 'PASS' : 'FAIL'} � ${message}`; $('check-results').append(item); };
    async function probe(path, options = {}) {
      const result = await request(path, options);
      $('api-log').textContent += `${options.method || 'GET'} ${path}\n${options.body || ''}\nHTTP ${result.status}\n${JSON.stringify(result.data, null, 2)}\n\n`;
      return result;
    }
    try {
      await setRole('customer');
      const payload = JSON.stringify({restaurant:'lagos', items:[{meal:'jollof',quantity:1}]});
      const options = {method:'POST',headers:{'Idempotency-Key':crypto.randomUUID()},body:payload};
      const first = await probe('/api/orders/', options);
      if (!first.ok) throw new Error(first.data.error);
      const replay = await probe('/api/orders/', options);
      append('Identical submission returns the same order, without a second creation.', first.status === 201 && replay.status === 200 && replay.data.order?.id === first.data.order.id && replay.data.created === false);
      const id = first.data.order.id;
      await setRole('ember');
      const forbidden = await probe(`/api/orders/${id}/`);
      append('Ember & Grain cannot read a Lagos Kitchen order (HTTP 404).', forbidden.status === 404);
      await setRole('lagos');
      const skip = await probe(`/api/orders/${id}/status/`, {method:'POST',body:JSON.stringify({status:'completed',revision:0})});
      append('Skipping from placed to completed is rejected (HTTP 409).', skip.status === 409);
      const valid = await probe(`/api/orders/${id}/status/`, {method:'POST',body:JSON.stringify({status:'accepted',revision:0})});
      const stale = await probe(`/api/orders/${id}/status/`, {method:'POST',body:JSON.stringify({status:'preparing',revision:0})});
      append('An old revision cannot overwrite an accepted order (HTTP 409).', valid.status === 200 && stale.status === 409);
      notice('Live checks finished. Inspect each response in the request log.');
    } catch (error) { append(error.message, false); notice('The checks could not finish. You can retry.', true); }
    finally { await setRole('customer').catch(() => {}); state.busy = false; $('run-checks').disabled = false; }
  }
  document.querySelectorAll('[data-view]').forEach((b) => b.addEventListener('click', () => switchView(b.dataset.view)));
  $('restaurant').addEventListener('change', (e) => {state.restaurant = e.target.value;state.cart = {};renderMenu();});
  $('vendor').addEventListener('change', async (e) => {if(state.busy)return;state.vendor=e.target.value;await switchView('vendor');});
  $('menu').addEventListener('click', (e) => {const b=e.target.closest('[data-meal]');if(!b||state.pending||state.busy)return;state.cart[b.dataset.meal]=Math.max(0,Math.min(10,(state.cart[b.dataset.meal]||0)+Number(b.dataset.delta)));renderMenu();});
  $('place-order').addEventListener('click', placeOrder); $('retry-order').addEventListener('click', placeOrder);
  $('vendor-orders').addEventListener('click', (e) => {const b=e.target.closest('[data-advance]');if(b)advance(b.dataset.advance,b);});
  ['refresh-customer','refresh-vendor'].forEach((id) => $(id).addEventListener('click', async () => {try{await loadOrders();notice('Order status refreshed.');}catch(error){notice(error.message,true);}}));
  $('run-checks').addEventListener('click', runChecks);
  async function start() {
    try {state.boot=await api('/api/bootstrap/');await setRole('customer');renderMenu();await loadOrders();$('connection').textContent='Django API connected � Your own demo workspace';}
    catch(error){$('connection').textContent='API unavailable';notice(`${error.message} Refresh the page to reconnect.`,true);}
  }
  start();
})();
