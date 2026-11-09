// Hi-res frames of Google with the domain being typed, one PNG per character.
// usage: node google_typing.js <domain> <outdir>
// writes 00.png (page), 01.png (box focused), 02..NN.png (after each char), 99.png (held)
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const [domain, out] = process.argv.slice(2);
if (!domain || !out) { console.error('usage: node google_typing.js <domain> <outdir>'); process.exit(1); }
fs.mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch();
  const c = await b.newContext({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 2, locale: 'en-US' });
  const p = await c.newPage();
  await p.goto('https://www.google.com/?hl=en'); await p.waitForTimeout(2000);
  await p.addStyleTag({ content: 'textarea[name=q]{caret-color:#1a73e8}' });
  const clip = { x: 320, y: 152, width: 640, height: 400 };
  const shot = (n) => p.screenshot({ path: path.join(out, n + '.png'), clip });
  await shot('00');
  await p.click('textarea[name=q]'); await p.waitForTimeout(400); await shot('01');
  for (let i = 0; i < domain.length; i++) { await p.keyboard.type(domain[i]); await p.waitForTimeout(250); await shot(String(i + 2).padStart(2, '0')); }
  await p.waitForTimeout(1200); await shot('99');
  await b.close();
  console.log(`google frames: ${domain.length + 3} in ${out} (last char frame = ${String(domain.length + 1).padStart(2, '0')}.png)`);
})();
