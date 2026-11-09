// Real screen recording of public pages (no login). One webm per page + screenshots + page text.
// usage: node capture_site.js <outdir> <name>=<url> [<name>=<url> ...]
// then:  ffmpeg -i <outdir>/vid_<name>/*.webm -vf fps=30 -q:v 3 <outdir>/fr_<name>/%04d.jpg
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const [out, ...pairs] = process.argv.slice(2);
if (!out || !pairs.length) { console.error('usage: node capture_site.js <outdir> name=url ...'); process.exit(1); }
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36';
const CURSOR = `(()=>{const add=()=>{if(document.getElementById('__cur'))return;const d=document.createElement('div');d.id='__cur';
d.innerHTML='<svg width="28" height="34" viewBox="0 0 28 34"><path d="M2 2 L2 26 L8 20 L12.5 30 L16.5 28.2 L12 18.5 L20 18.5 Z" fill="black" stroke="white" stroke-width="2" stroke-linejoin="round"/></svg>';
d.style.cssText='position:fixed;left:-50px;top:-50px;z-index:2147483647;pointer-events:none';document.documentElement.appendChild(d);
addEventListener('mousemove',e=>{d.style.left=(e.clientX-2)+'px';d.style.top=(e.clientY-2)+'px'},true);};
if(document.readyState==='loading')addEventListener('DOMContentLoaded',add);else add();setInterval(add,500);})();`;
fs.mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch();
  for (const pr of pairs) {
    const i = pr.indexOf('='); const name = pr.slice(0, i), url = pr.slice(i + 1);
    const c = await b.newContext({ viewport: { width: 1280, height: 800 }, locale: 'en-US', userAgent: UA, recordVideo: { dir: path.join(out, 'vid_' + name), size: { width: 1280, height: 800 } } });
    await c.addInitScript(CURSOR);
    const p = await c.newPage(); let ok = false;
    for (let k = 0; k < 3 && !ok; k++) {
      try { await p.goto(url, { timeout: 30000 }); } catch (e) { }
      await p.waitForTimeout(5000);
      ok = (await p.evaluate(() => document.body ? document.body.innerText.length : 0)) > 200;
    }
    for (const label of ['Accept all', 'Accept All', 'Accept', 'I agree', 'Got it']) {
      try { await p.getByRole('button', { name: label }).first().click({ timeout: 1200 }); break; } catch (e) { }
    }
    await p.mouse.move(640, 400, { steps: 20 }); await p.waitForTimeout(800);
    await p.screenshot({ path: path.join(out, `${name}_0.png`) });
    for (let s = 1; s <= 7; s++) {
      await p.mouse.move(400 + (s % 2) * 400, 300 + (s % 3) * 120, { steps: 15 });
      const before = await p.evaluate(() => window.scrollY + (document.scrollingElement ? document.scrollingElement.scrollTop : 0));
      await p.mouse.wheel(0, 520); await p.waitForTimeout(700);
      const after = await p.evaluate(() => window.scrollY + (document.scrollingElement ? document.scrollingElement.scrollTop : 0));
      if (after === before) {   // sites with custom scroll containers ignore the wheel: scroll by script instead
        await p.evaluate(() => {
          const els = [document.scrollingElement, ...document.querySelectorAll('main, [class*=scroll], body > div, #__next, #root')].filter(Boolean);
          const el = els.find(e => e.scrollHeight > e.clientHeight + 50) || document.scrollingElement;
          el.scrollBy({ top: 520, behavior: 'smooth' }); window.scrollBy({ top: 520, behavior: 'smooth' });
        });
        await p.keyboard.press('PageDown').catch(() => { });
      }
      await p.waitForTimeout(900);
      await p.screenshot({ path: path.join(out, `${name}_${s}.png`) });
    }
    fs.writeFileSync(path.join(out, name + '.txt'), await p.evaluate(() => document.body ? document.body.innerText : ''));
    console.log(name, ok ? 'OK' : 'FAILED-TO-LOAD', p.url());
    await c.close();
  }
  await b.close();
})();
