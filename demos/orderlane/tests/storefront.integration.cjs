// DOM integration checks against the running Django API, without a browser.
// Usage: ORDERLANE_JSDOM_PATH=/path/to/jsdom node tests/storefront.integration.cjs
const assert = require('node:assert/strict');
const {readFileSync} = require('node:fs');
const {join} = require('node:path');
const {JSDOM, CookieJar} = require(process.env.ORDERLANE_JSDOM_PATH || 'jsdom');
const base = process.env.ORDERLANE_TEST_URL || 'http://127.0.0.1:8771';
const jar = new CookieJar();
const wait = async (fn, description) => {const end=Date.now()+6000;while(Date.now()<end){if(fn())return;await new Promise(r=>setTimeout(r,20));}throw Error('Timeout: '+description);};
let checks = 0;
function pass(description){checks++;console.log('PASS '+description);}

async function page(saved){
  const html=await(await fetch(base+'/')).text();
  const dom=new JSDOM(html,{url:base+'/',runScripts:'outside-only',cookieJar:jar,pretendToBeVisual:true});
  const w=dom.window;
  w.scrollTo=()=>{};w.HTMLElement.prototype.scrollIntoView=()=>{};
  w.matchMedia=()=>({matches:true});
  if(saved)w.sessionStorage.setItem('orderlane-draft-v2',saved);
  w.fetch=async(path,options={})=>{
    const url=new URL(path,base);const cookie=jar.getCookieStringSync(url.href);
    const response=await fetch(url,{...options,headers:{...options.headers,...cookie?{Cookie:cookie}:{}},signal:options.signal});
    for(const raw of response.headers.getSetCookie())jar.setCookieSync(raw,url.href);
    return response;
  };
  const script=w.document.createElement('script');script.src=base+'/static/storefront.js';
  Object.defineProperty(w.document,'currentScript',{get:()=>script,configurable:true});
  w.eval(readFileSync(join(__dirname,'../static/storefront.js'),'utf8'));
  await wait(()=>w.document.getElementById('connection-text').textContent.includes('Kitchen connected'),'bootstrap');
  await wait(()=>w.document.getElementById('photo-credits').textContent.trim().length>0,'photo credits');
  return dom;
}

(async()=>{
  let dom=await page();let d=dom.window.document;
  assert.equal(d.querySelectorAll('.meal').length,3);assert.equal(d.querySelectorAll('#customer-orders .order').length,0);pass('menu loads and starter orders stay out of customer history');
  const historyLength=dom.window.history.length;
  d.querySelector('.primary-nav [data-view="tracking"]').click();await wait(()=>!d.getElementById('tracking-view').hidden&&!d.getElementById('place-order').firstElementChild.textContent.includes('Sending'),'tracking panel');
  assert.equal(dom.window.history.length,historyLength);assert.equal(dom.window.location.hash,'#orders');
  d.querySelector('.primary-nav [data-view="customer"]').click();await wait(()=>!d.getElementById('customer-view').hidden&&!d.getElementById('place-order').firstElementChild.textContent.includes('Sending'),'menu panel');
  assert.equal(dom.window.history.length,historyLength);assert.equal(dom.window.location.hash,'');pass('panel changes do not create history entries that can restore the wrong panel');
  const suyaCredit=[...d.querySelectorAll('#photo-credits p')].find(p=>p.textContent.includes('suya'));
  assert.match(suyaCredit.querySelector('[rel="license"]').href,/publicdomain\/zero/);pass('each photograph links to its own license');
  d.querySelector('[data-filter="vegetarian"]').click();assert.equal(d.querySelectorAll('.meal').length,1);assert.match(d.querySelector('.meal h3').textContent,/Beans/);pass('dietary filter limits the actual menu');
  d.querySelector('[data-filter="all"]').click();const search=d.getElementById('menu-search');search.value='no such meal';search.dispatchEvent(new dom.window.Event('input',{bubbles:true}));assert.equal(d.querySelectorAll('.meal').length,0);d.getElementById('clear-search').click();assert.equal(d.querySelectorAll('.meal').length,3);pass('search empty state can recover');
  d.querySelector('#menu [data-meal="jollof"][data-delta="1"]').click();assert.equal(d.activeElement.dataset.meal,'jollof');assert.equal(d.getElementById('basket-count').textContent,'1');pass('adding a meal updates the basket and retains keyboard focus');
  d.getElementById('restaurant').value='ember';d.getElementById('restaurant').dispatchEvent(new dom.window.Event('change',{bubbles:true}));assert.equal(d.getElementById('basket-count').textContent,'0');
  d.querySelector('#menu [data-meal="suya"][data-delta="1"]').click();
  d.getElementById('restaurant').value='lagos';d.getElementById('restaurant').dispatchEvent(new dom.window.Event('change',{bubbles:true}));assert.equal(d.getElementById('basket-count').textContent,'1');assert.match(d.getElementById('basket').textContent,/jollof/);assert.doesNotMatch(d.getElementById('basket').textContent,/Suya/);pass('kitchen switching preserves separate baskets');
  const stored=dom.window.sessionStorage.getItem('orderlane-draft-v2');dom.window.close();dom=await page(stored);d=dom.window.document;assert.equal(d.getElementById('basket-count').textContent,'1');pass('the draft survives a reload');
  d.getElementById('place-order').click();await wait(()=>!d.getElementById('confirmation').hidden&&!d.getElementById('tracking-view').hidden,'order confirmation');
  await wait(()=>!d.getElementById('place-order').firstElementChild.textContent.includes('Sending'),'submission completed');
  assert.equal(d.getElementById('basket-count').textContent,'0');assert.match(d.getElementById('confirmation-text').textContent,/Lagos Kitchen/);pass('submission reaches a real server-confirmed order');
  d.querySelector('#confirmation [data-view="vendor"]').click();await wait(()=>!d.getElementById('vendor-view').hidden&&d.querySelector('#vendor-orders [data-advance]:not(:disabled)'),'vendor ready');
  assert.equal(d.querySelectorAll('#vendor-orders .order').length,2);d.querySelector('#vendor-orders [data-advance]').click();await wait(()=>d.getElementById('notice').textContent.includes('Order updated'),'vendor acceptance');pass('vendor actions are enabled after navigation and advance an actual order');
  d.querySelector('.primary-nav [data-view="tracking"]').click();await wait(()=>!d.getElementById('tracking-view').hidden&&d.querySelector('#customer-orders .order-status')?.textContent==='Accepted','customer updated');pass('customer tracking sees the vendor update');
  await wait(()=>!d.getElementById('place-order').firstElementChild.textContent.includes('Sending'),'navigation finished');
  const again=dom.window.sessionStorage.getItem('orderlane-draft-v2');dom.window.close();dom=await page(again);d=dom.window.document;assert.equal(d.querySelectorAll('#customer-orders .order').length,1);pass('order history remains available after reload');
  d.querySelector('#menu [data-meal="beans"][data-delta="1"]').click();
  const workingFetch=dom.window.fetch;let dropOnce=true;
  dom.window.fetch=async(path,options={})=>{const result=await workingFetch(path,options);if(path==='/api/orders/'&&options.method==='POST'&&dropOnce){dropOnce=false;throw Error('Connection lost after the order was sent.');}return result;};
  d.getElementById('place-order').click();await wait(()=>!d.getElementById('retry-order').hidden,'safe retry available');
  assert.equal(d.querySelector('#menu [data-meal="beans"][data-delta="1"]').disabled,true);
  const uncertain=dom.window.sessionStorage.getItem('orderlane-draft-v2');const requestKey=JSON.parse(uncertain).pending.key;
  dom.window.close();dom=await page(uncertain);d=dom.window.document;assert.equal(JSON.parse(dom.window.sessionStorage.getItem('orderlane-draft-v2')).pending.key,requestKey);
  d.getElementById('retry-order').click();await wait(()=>!d.getElementById('confirmation').hidden&&!d.getElementById('tracking-view').hidden,'replayed order confirmed');
  await wait(()=>d.querySelectorAll('#customer-orders .order').length===2,'exactly two total orders');
  await wait(()=>!d.getElementById('place-order').firstElementChild.textContent.includes('Sending'),'retry finished');
  pass('an uncertain response keeps its request key across reload and retries without duplication');
  dom.window.close();console.log(`${checks} storefront integration checks passed.`);
})().catch(error=>{console.error(error);process.exitCode=1;});
