(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const assetRoot = new URL('assets/', document.currentScript.src).href;
  const money = value => new Intl.NumberFormat('en-NG', {style:'currency',currency:'NGN',maximumFractionDigits:0}).format(value);
  const esc = value => String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const icon = kind => `<svg viewBox="0 0 20 20" aria-hidden="true"><path d="${kind==='plus'?'M4 10h12M10 4v12':'M4 10h12'}"/></svg>`;
  const stages = ['placed','accepted','preparing','ready','completed'];
  const stageNames = {placed:'Received',accepted:'Accepted',preparing:'Preparing',ready:'Ready',completed:'Collected'};
  const actions = {placed:'Accept order',accepted:'Start preparing',preparing:'Mark ready',ready:'Complete collection'};
  const storeKey = 'orderlane-draft-v2';
  let saved = {};
  try { const value=JSON.parse(sessionStorage.getItem(storeKey)||'{}');if(value&&typeof value==='object'&&!Array.isArray(value))saved=value; } catch {}
  const state = {boot:null,view:'customer',restaurant:['lagos','ember'].includes(saved.restaurant)?saved.restaurant:'lagos',vendor:'lagos',carts:saved.carts&&typeof saved.carts==='object'&&!Array.isArray(saved.carts)?saved.carts:{},orders:[],pending:saved.pending||null,workspace:saved.workspace,ready:false,busy:false,filter:'all',search:'',confirmation:null};
  const cart = () => state.carts[state.restaurant] || (state.carts[state.restaurant]={});
  const notice = (message,error=false) => {$('notice').hidden=false;$('notice').textContent=message;$('notice').classList.toggle('error',error);};
  function persist(){try{sessionStorage.setItem(storeKey,JSON.stringify({restaurant:state.restaurant,carts:state.carts,pending:state.pending,workspace:state.workspace}));}catch{}}
  async function request(path,options={}){
    const csrf=document.cookie.split('; ').find(c=>c.startsWith('csrftoken='))?.split('=')[1]||'';
    const controller=new AbortController();const timeout=setTimeout(()=>controller.abort(),15000);
    try{
      const response=await fetch(path,{credentials:'same-origin',cache:'no-store',...options,signal:controller.signal,headers:{'Content-Type':'application/json','X-CSRFToken':csrf,...options.headers}});
      let data;try{data=await response.json();}catch{throw Error('The kitchen could not respond. Please try again.');}
      return {status:response.status,ok:response.ok,data};
    }catch(error){if(error.name==='AbortError')throw Error('The kitchen is taking longer than expected.');throw error;}
    finally{clearTimeout(timeout);}
  }
  async function api(path,options){const result=await request(path,options);if(!result.ok){const error=Error(result.data.error||`Request failed (${result.status}).`);error.status=result.status;throw error;}return result.data;}
  const setRole=role=>api('/api/role/',{method:'POST',body:JSON.stringify({role})});
  async function loadOrders(){state.orders=(await api('/api/orders/')).orders;renderOrders();}
  function quantity(id,qty,context){return `<div class="quantity"><button data-meal="${id}" data-delta="-1" data-context="${context}" aria-label="Remove one ${esc(state.boot.menu[id].name)}" ${!qty||state.pending||state.busy?'disabled':''}>${icon('minus')}</button><output aria-label="Quantity of ${esc(state.boot.menu[id].name)}">${qty}</output><button data-meal="${id}" data-delta="1" data-context="${context}" aria-label="Add one ${esc(state.boot.menu[id].name)}" ${qty>=10||state.pending||state.busy?'disabled':''}>${icon('plus')}</button></div>`;}
  function renderMenu(){
    if(!state.boot)return;
    const restaurant=state.boot.restaurants[state.restaurant];
    $('restaurant').value=state.restaurant;
    $('kitchen-name').textContent=restaurant.name;
    $('kitchen-description').textContent=restaurant.description;
    $('prep-time').textContent=restaurant.prep;
    const rows=Object.entries(state.boot.menu).filter(([,m])=>m.restaurant===state.restaurant&&(state.filter==='all'||state.filter==='favourites'&&m.category==='House favourite'||state.filter==='vegetarian'&&m.category==='Vegetarian')&&`${m.name} ${m.description}`.toLowerCase().includes(state.search));
    $('menu').innerHTML=rows.length?rows.map(([id,meal])=>{
      const qty=cart()[id]||0;
      return `<article class="meal"><img class="meal-image" src="${assetRoot+id}-illustrative.jpg" alt="" width="960" height="720" loading="lazy"><div class="meal-content"><div class="meal-top"><h3>${esc(meal.name)}</h3></div><div class="meal-bottom"><strong class="meal-price">${money(meal.price)}</strong>${qty?quantity(id,qty,'menu'):`<button class="add-meal" data-meal="${id}" data-delta="1" data-context="menu" aria-label="Add one ${esc(meal.name)}" ${state.pending||state.busy?'disabled':''}>${icon('plus')}</button>`}</div></div></article>`;
    }).join(''):'<div class="empty-state"><h2>No meals found</h2><p>Try a different search or choose All meals.</p><button class="secondary" id="clear-search">Clear filters</button></div>';
    $('menu-result').textContent=`${rows.length} ${rows.length===1?'meal':'meals'} on this menu. Prices in Nigerian naira.`;
    renderBasket();
  }
  function renderBasket(){
    if(!state.boot)return;
    const rows=Object.entries(cart()).filter(([id,qty])=>qty>0&&state.boot.menu[id]?.restaurant===state.restaurant);
    const count=rows.reduce((sum,[,qty])=>sum+qty,0);
    const total=rows.reduce((sum,[id,qty])=>sum+state.boot.menu[id].price*qty,0);
    $('basket').innerHTML=rows.length?rows.map(([id,qty])=>`<div class="basket-row"><div><h3>${esc(state.boot.menu[id].name)}</h3>${quantity(id,qty,'basket')}</div><strong>${money(state.boot.menu[id].price*qty)}</strong></div>`).join(''):'<div class="basket-empty"><svg viewBox="0 0 44 44" aria-hidden="true"><path d="M9 17h26l-3 22H12L9 17Zm8 0v-5a5 5 0 0 1 10 0v5M16 23v8m12-8v8"/></svg><p>Add a meal to start.</p></div>';
    $('basket-count').textContent=count;
    $('basket-summary').hidden=!rows.length;
    $('subtotal').textContent=money(total);$('total').textContent=money(total);
    $('place-order').disabled=!rows.length||state.busy||!!state.pending||!state.ready;
    $('place-order').firstElementChild.textContent=state.busy?'Placing order…':'Place order';
    $('retry-order').hidden=!state.pending||state.busy||!state.ready;
    $('restaurant').disabled=!!state.pending||state.busy;
    $('mobile-basket').hidden=!count||state.view!=='customer';
    $('mobile-count').textContent=count;$('mobile-item-label').textContent=count===1?'item':'items';$('mobile-total').textContent=money(total);
  }
  function timeline(order){return `<ol class="timeline" aria-label="Order progress">${stages.map((stage,index)=>{const event=order.events.find(e=>e.status===stage);return `<li class="${index<=stages.indexOf(order.status)?'done':''}">${stageNames[stage]}${event?`<time datetime="${esc(event.at)}">${new Date(event.at).toLocaleTimeString('en-NG',{hour:'2-digit',minute:'2-digit'})}</time>`:''}</li>`;}).join('')}</ol>`;}
  function orderMarkup(order,vendor=false){return `<article class="order"><div class="order-head"><div class="order-id"><strong>${esc(order.restaurant_name)}</strong>#${esc(order.id.slice(0,8).toUpperCase())} · ${new Date(order.created_at).toLocaleDateString('en-NG',{day:'numeric',month:'short'})}</div><span class="order-status ${order.status}">${stageNames[order.status]}</span></div><div class="order-body"><p class="order-items">${order.items.map(i=>`${i.quantity} × ${esc(i.name)}`).join('<br>')}</p><strong class="order-total">${money(order.total)}</strong></div>${timeline(order)}${vendor&&actions[order.status]?`<button class="primary" data-advance="${order.id}" ${state.busy?'disabled':''}>${actions[order.status]}</button>`:''}${order.demo_sample?'<span class="order-seed">Sample order</span>':''}</article>`;}
  function renderOrders(){
    const customers=state.orders.filter(o=>!o.demo_sample);
    $('order-count').hidden=!customers.length;$('order-count').textContent=customers.length;
    $('customer-orders').innerHTML=customers.length?customers.map(o=>orderMarkup(o)).join(''):'<div class="empty-state"><h2>No orders yet</h2><p>Your orders will appear here.</p><button class="primary" data-view="customer">Explore the menu</button></div>';
    const vendors=state.orders.filter(o=>o.restaurant===state.vendor);
    if($('kitchen-order-count'))$('kitchen-order-count').textContent=`${vendors.length} ${vendors.length===1?'order':'orders'}`;
    $('vendor-orders').innerHTML=vendors.length?vendors.map(o=>orderMarkup(o,true)).join(''):'<div class="empty-state"><h2>No kitchen orders</h2><p>Orders for this kitchen will appear here.</p><button class="primary" data-view="customer">Go to the menu</button></div>';
  }
  function showView(view){
    state.view=view;document.title='Orderlane | '+({customer:'Menu',tracking:'Orders',vendor:'Kitchen',engineering:'API lab'}[view]);
    for(const name of ['customer','tracking','vendor','engineering'])$(name+'-view').hidden=name!==view;
    document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===view)));
    $('mobile-basket').hidden=state.view!=='customer'||!Object.values(cart()).some(q=>q>0);
    if(view==='tracking')history.replaceState(null,'',location.pathname+location.search+'#orders');else if(view==='customer'&&location.hash)history.replaceState(null,'',location.pathname+location.search);
  }
  async function switchView(view,{focus=true}={}){
    if(!['customer','tracking','vendor','engineering'].includes(view)||!state.boot||state.busy)return;
    state.busy=true;renderBasket();
    try{
      await setRole(view==='vendor'?state.vendor:'customer');
      showView(view);await loadOrders();notice('');
      if(focus){$(view==='customer'?'kitchen-name':view+'-heading').setAttribute('tabindex','-1');$(view==='customer'?'kitchen-name':view+'-heading').focus({preventScroll:true});window.scrollTo({top:0,behavior:'instant'});}
    }catch(error){notice(error.message,true);}
    finally{state.busy=false;renderBasket();renderOrders();}
  }
  function adjust(meal,delta,context){
    if(!state.ready||state.busy||state.pending)return;
    cart()[meal]=Math.max(0,Math.min(10,(cart()[meal]||0)+delta));persist();renderMenu();
    const container=context==='basket'?$('basket'):$('menu');
    const desired=container.querySelector(`[data-meal="${meal}"][data-delta="${delta}"]`);
    const target=desired&&!desired.disabled?desired:container.querySelector(`[data-meal="${meal}"]:not(:disabled)`);
    if(target)target.focus({preventScroll:true});else $('basket-panel').focus({preventScroll:true});
  }
  async function placeOrder(){
    if(!state.ready||state.busy)return;
    if(!state.pending){const items=Object.entries(cart()).filter(([,q])=>q>0).map(([meal,quantity])=>({meal,quantity}));if(!items.length)return;state.pending={key:crypto.randomUUID(),payload:{restaurant:state.restaurant,items}};persist();}
    state.busy=true;renderMenu();
    try{
      await setRole('customer');
      const data=await api('/api/orders/',{method:'POST',headers:{'Idempotency-Key':state.pending.key},body:JSON.stringify(state.pending.payload)});
      const order=data.order;state.vendor=order.restaurant;$('vendor').value=state.vendor;
      state.pending=null;state.carts[state.restaurant]={};persist();
      state.confirmation=order.id;state.orders=[order,...state.orders.filter(o=>o.id!==order.id)];
      showView('tracking');renderOrders();$('confirmation').hidden=false;$('confirmation-text').textContent=`${order.restaurant_name} · #${order.id.slice(0,8).toUpperCase()} · ${money(order.total)}`;
      $('confirmation').focus({preventScroll:true});window.scrollTo({top:0,behavior:'instant'});
      try{await loadOrders();notice('');}catch{notice('Your order was placed. Status could not refresh; select Refresh to reconnect.',true);}
    }catch(error){
      if(error.status&&[400,401,403,409,415,429].includes(error.status)){state.pending=null;persist();notice(`${error.message} Review your basket before sending again.`,true);}
      else notice(`${error.message} Basket saved. Select Retry order to check the same submission.`,true);
    }finally{state.busy=false;renderMenu();}
  }
  async function advanceOrder(id,button){
    if(state.busy)return;const order=state.orders.find(o=>o.id===id);if(!order)return;
    state.busy=true;button.disabled=true;
    try{await api(`/api/orders/${id}/status/`,{method:'POST',body:JSON.stringify({status:stages[stages.indexOf(order.status)+1],revision:order.revision})});await loadOrders();notice('Order updated.');}
    catch(error){notice(error.message,true);await loadOrders().catch(()=>{});}
    finally{state.busy=false;renderOrders();}
  }
  async function refreshOrders(button){if(!state.ready||state.busy)return;state.busy=true;button.disabled=true;try{await loadOrders();notice('Order status is up to date.');}catch(error){notice(error.message,true);}finally{state.busy=false;button.disabled=false;renderOrders();}}
  async function runChecks(){
    if(!state.ready||state.busy)return;state.busy=true;$('run-checks').disabled=true;$('check-results').innerHTML='';$('api-log').textContent='';
    const append=(message,passed)=>{const row=document.createElement('li');row.className=passed?'passed':'failed';row.textContent=`${passed?'PASS':'FAIL'} · ${message}`;$('check-results').append(row);};
    async function probe(path,options={}){const r=await request(path,options);$('api-log').textContent+=`${options.method||'GET'} ${path}\n${options.body||''}\nHTTP ${r.status}\n${JSON.stringify(r.data,null,2)}\n\n`;return r;}
    try{
      await setRole('customer');const options={method:'POST',headers:{'Idempotency-Key':crypto.randomUUID()},body:JSON.stringify({restaurant:'lagos',items:[{meal:'jollof',quantity:1}]})};
      const first=await probe('/api/orders/',options);if(!first.ok)throw Error(first.data.error);const replay=await probe('/api/orders/',options);const id=first.data.order.id;
      append('Identical submission returns the same order.',first.status===201&&replay.status===200&&replay.data.order?.id===id&&replay.data.created===false);
      await setRole('ember');const isolated=await probe(`/api/orders/${id}/`);append('The other kitchen cannot read it (404).',isolated.status===404);
      await setRole('lagos');const skip=await probe(`/api/orders/${id}/status/`,{method:'POST',body:JSON.stringify({status:'completed',revision:0})});append('Skipping preparation is rejected (409).',skip.status===409);
      const accepted=await probe(`/api/orders/${id}/status/`,{method:'POST',body:JSON.stringify({status:'accepted',revision:0})});const stale=await probe(`/api/orders/${id}/status/`,{method:'POST',body:JSON.stringify({status:'preparing',revision:0})});append('A stale revision cannot overwrite the order (409).',accepted.status===200&&stale.status===409);notice('Live checks finished. Expand the log to inspect the responses.');
    }catch(error){append(error.message,false);notice('The checks could not finish. Please try again.',true);}
    finally{await setRole('customer').catch(()=>{});await loadOrders().catch(()=>{});state.busy=false;$('run-checks').disabled=false;renderBasket();}
  }
  document.addEventListener('click',event=>{
    const view=event.target.closest('[data-view]');if(view){switchView(view.dataset.view);return;}
    const meal=event.target.closest('[data-meal]');if(meal){adjust(meal.dataset.meal,Number(meal.dataset.delta),meal.dataset.context);return;}
    const filter=event.target.closest('[data-filter]');if(filter){state.filter=filter.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===filter)));renderMenu();return;}
    if(event.target.closest('#clear-search')){state.search='';state.filter='all';$('menu-search').value='';document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter==='all')));renderMenu();$('menu-search').focus();}
    const advance=event.target.closest('[data-advance]');if(advance)advanceOrder(advance.dataset.advance,advance);
  });
  $('restaurant').addEventListener('change',e=>{if(state.busy||state.pending){e.target.value=state.restaurant;return;}state.restaurant=e.target.value;state.filter='all';state.search='';$('menu-search').value='';document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter==='all')));persist();renderMenu();notice('');});
  $('vendor').addEventListener('change',async e=>{if(state.busy){e.target.value=state.vendor;return;}const previous=state.vendor;state.vendor=e.target.value;state.busy=true;try{await setRole(state.vendor);await loadOrders();notice('');}catch(error){state.vendor=previous;e.target.value=previous;notice(error.message,true);}finally{state.busy=false;renderOrders();}});
  $('menu-search').addEventListener('input',e=>{state.search=e.target.value.trim().toLowerCase();renderMenu();});
  $('place-order').addEventListener('click',placeOrder);$('retry-order').addEventListener('click',placeOrder);
  $('refresh-customer').addEventListener('click',e=>refreshOrders(e.currentTarget));$('refresh-vendor').addEventListener('click',e=>refreshOrders(e.currentTarget));$('run-checks').addEventListener('click',runChecks);
  $('mobile-basket').addEventListener('click',()=>{$('basket-panel').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'center'});$('basket-panel').focus({preventScroll:true});});
  async function start(){
    try{
      state.boot=await api('/api/bootstrap/');
      if(state.workspace&&state.workspace!==state.boot.workspace&&state.pending){state.pending=null;notice('Your session expired. Review your saved basket before placing an order.');}
      state.workspace=state.boot.workspace;
      if(state.pending&&!state.boot.restaurants[state.pending.payload?.restaurant])state.pending=null;
      if(state.pending)state.restaurant=state.pending.payload.restaurant;
      for(const restaurant of ['lagos','ember']){const old=state.carts[restaurant];state.carts[restaurant]={};if(old&&typeof old==='object')for(const [id,qty]of Object.entries(old))if(state.boot.menu[id]?.restaurant===restaurant&&Number.isInteger(qty)&&qty>0&&qty<=10)state.carts[restaurant][id]=qty;}
      await setRole('customer');state.ready=true;persist();renderMenu();await loadOrders();
      $('connection-text').textContent='Connected';$('connection').hidden=true;
      if(location.hash==='#orders')showView('tracking');
    }catch(error){state.ready=false;$('connection').hidden=false;$('connection').classList.add('error');$('connection-text').textContent='Offline. Refresh to reconnect.';notice(`${error.message} Refresh to reconnect.`,true);renderBasket();}
    fetch(assetRoot+'credits.json').then(r=>r.json()).then(rows=>{$('photo-credits').innerHTML=rows.map(row=>row.type==='generated'?`<p>${esc(row.title)} · AI-generated illustration.</p>`:`<p><a href="${esc(row.source)}" rel="noreferrer">${esc(row.key)} photo</a> ${esc(row.artist)} · <a href="${esc(row.licenseUrl)}" rel="license">${esc(row.license)}</a></p>`).join('');}).catch(()=>{$('photo-credits').textContent='Menu images are AI-generated illustrations. Asset details are included with the source.';});
  }
  start();
  document.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){const b=e.target.closest('button');if(b)b.setAttribute('data-keyboard','');}});
  document.addEventListener('pointerdown',e=>{const b=e.target.closest('button');if(b)b.removeAttribute('data-keyboard');});
})();
