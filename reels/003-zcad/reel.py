# nopay.exe reel #2 — "3 free AI agents" in Phosphor Terminal style. Reuses the CRT pipeline from crt.py.
import sys, os, json, numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, 'assets')   # recordings, google stills, voice, words (not committed)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'pipeline', 'engine'))
import crt_engine as C
from PIL import Image, ImageDraw

FPS = 30; DUR = 32.4
C.DUR = DUR
WT = dict(stop=0.0, paying=0.44, cad=0.9, this=1.66, builds=2.04, model=2.82, one=3.32, sentence=3.62, called=4.7,
          zcad=4.88, search=5.7, zcad2=5.8, type=7.78, drone=8.96, gearbox=9.66, generates=10.74, editable=11.52,
          parts=12.04, assemblies=12.64, keep=14.06, browser=15.1, exports=16.04, every=16.36, step=17.62, free=18.64,
          zero=19.38, c200=20.54, month=21.48, c600=22.52, gift=23.42, noncom=24.54, students=26.66, save=27.04,
          follow=28.26, nopay=28.54, more=30.18, ai=30.8)
ROLLS = [4.42, 15.62, 26.86]
C.ROLLS = ROLLS; C.SCENE_T = [0.0] + ROLLS + [99]
TYPE0, DT, URL = 5.86, 0.11, 'zcad.ai'
WX, WY = 30, 400

_cache = {}
def load(p, invert_bright=False):
    """original-colour footage, 900x562 RGB float 0..1"""
    if p in _cache: return _cache[p]
    g = np.asarray(Image.open(p).convert('RGB').resize((900, 562), Image.LANCZOS), np.float32) / 255
    if len(_cache) > 300: _cache.clear()
    _cache[p] = g; return g
def clip(name, t, t0, t1, s0, s1):
    n = len(os.listdir(f'{A}/fr_{name}'))
    s = s0 + (s1 - s0) * C.clamp((t - t0) / (t1 - t0))
    return load(f'{A}/fr_{name}/{max(1, min(n, int(s * 30) + 1)):04d}.jpg')
def gs(t):
    if t < 5.4: nm = '00'
    elif t < TYPE0: nm = '01'
    else:
        k = int((t - TYPE0) / DT) + 1
        nm = ('08' if t < 7.5 else '99') if k >= len(URL) else f'{k + 1:02d}'
    return load(f'{A}/gs/{nm}.png')

text, inverse, tw, typed, cursor, boxdraw, arrow, put = C.text, C.inverse, C.tw, C.typed, C.cursor, C.boxdraw, C.arrow, C.put_footage
TW = C.TW
def status(d, label):
    d.rectangle((0, 18, TW, 84), fill=230)
    text(d, (24, 22), 'nopay.exe #3', 54, 8); text(d, (TW - 24, 22), label, 54, 8, anchor='ra')
FOOT = {}
def window(d, buf, g, title):
    boxdraw(d, WX - 14, WY - 14, WX + 914, WY + 576, 200, title, 44); FOOT['g'] = g
def pop(t, at, base): return int(base * (1.18 if 0 <= t - at < 0.08 else 1))

def s_hook(d, buf, t):
    if t < WT['this'] - 0.03:
        text(d, (TW / 2, 330), 'STOP' if t < WT['paying'] else 'STOP PAYING FOR', 124, 255, anchor='ma')
        if t >= WT['cad'] - 0.04: inverse(d, (TW / 2, 500), 'CAD SOFTWARE', pop(t, WT['cad'], 132), anchor='ma', pad=16)
        return
    status(d, 'TEXT -> CAD')
    text(d, (30, 112), typed('> prompt "a gearbox"', WT['this'] - 0.05, t, 26), 66, 230)
    if t >= WT['builds'] - 0.05:
        text(d, (30, 200), typed('BUILDING 3D MODEL' + '.' * (int(t * 4) % 4), WT['builds'] - 0.05, t, 30), 60, 255)
    if t >= WT['model'] - 0.1: window(d, buf, clip('ai', t, WT['model'], 4.42, 16.8, 18.4), ' zcad.ai ')
    if t >= WT['one'] - 0.06:
        inverse(d, (TW / 2, 1000), ' 1 SENTENCE = 3D MODEL ', pop(t, WT['one'], 72), anchor='ma', pad=8)

def s_search(d, buf, t):
    status(d, 'SEARCH')
    if t < 7.55:
        inverse(d, (40, 104), ' TOOL ', 72, pad=6); text(d, (230, 98), typed('zCAD', WT['called'], t, 16), 96, 255)
        text(d, (40, 206), 'SEARCH>', 56, 200)
        s = typed(URL, TYPE0, t, 1 / DT) if t >= TYPE0 else ''
        size = 140; x0 = TW / 2 - tw(URL, size) / 2
        text(d, (x0, 236), s, size, 255); cursor(d, x0 + tw(s, size), 236, size, t)
        if len(s) == len(URL): d.line((x0, 380, x0 + tw(s, size), 380), fill=255, width=6)
        window(d, buf, gs(t), ' google.com ')
        arrow(d, [(TW / 2, 384), (TW / 2, WY + 280)], C.clamp((t - 6.9) / 0.3), 255)
        return
    inverse(d, (40, 104), ' TOOL ', 72, pad=6); text(d, (230, 98), 'zCAD', 96, 255)
    if t < WT['keep'] - 0.1:
        window(d, buf, clip('ai', t, 7.55, 10.5, 5.0, 8.0) if t < 10.5 else clip('ai', t, 10.5, WT['keep'], 13.0, 18.5), ' zcad.ai ')
        text(d, (40, 214), typed('> type: drone | gearbox', WT['type'] - 0.05, t, 30), 60, 230)
        if t >= WT['editable'] - 0.06: inverse(d, (40, 984), ' EDITABLE PARTS ', pop(t, WT['editable'], 58), pad=8)
        if t >= WT['assemblies'] - 0.06: inverse(d, (40, 1052), ' + ASSEMBLIES ', pop(t, WT['assemblies'], 52), pad=8)
    else:
        window(d, buf, clip('online', t, WT['keep'], 15.62, 9.9, 11.0), ' zcad.ai/online ')
        text(d, (40, 214), typed('> keep building online', WT['keep'] - 0.1, t, 34), 60, 230)
        if t >= WT['browser'] - 0.06: inverse(d, (40, 990), ' IN YOUR BROWSER ', pop(t, WT['browser'], 72), pad=8)

def s_free(d, buf, t):
    status(d, 'PRICE CHECK')
    window(d, buf, clip('pricing', t, 15.7, 26.86, 10.0, 12.6), ' zcad.ai/pricing ')
    text(d, (40, 106), typed('> export --format', WT['exports'] - 0.05, t, 32), 60, 230)
    if t >= WT['step'] - 0.06: inverse(d, (40, 190), ' EVERY FORMAT + STEP ', pop(t, WT['step'], 64), pad=8)
    if t >= WT['zero'] - 0.05:
        inverse(d, (TW - 40 - tw(' $0 ', 150), 150), ' $0 ', pop(t, WT['zero'], 150), pad=10)
    if t >= WT['c200'] - 0.05:
        p = C.clamp((t - WT['c200']) / (WT['month'] - WT['c200'])); n = int(round(200 * (1 - (1 - int(p * 8) / 8) ** 2) / 10) * 10)
        text(d, (40, 980), f'{n} CREDITS / MONTH', 64, 255)
    if t >= WT['c600'] - 0.05: inverse(d, (40, 1050), ' +600 BETA GIFT ', pop(t, WT['c600'], 52), pad=8)
    if t >= WT['noncom'] - 0.05:
        d.rectangle((0, 1045, TW, 1120), fill=0)
        text(d, (40, 1052), typed('NON-COMMERCIAL ->', WT['noncom'] - 0.05, t, 34), 60, 230)
        if t >= WT['students'] - 0.5: inverse(d, (TW - 40 - tw(' STUDENTS ', 56), 1050), ' STUDENTS ', pop(t, WT['students'] - 0.5, 56), pad=8)

def s_end(d, buf, t):
    status(d, 'EXIT 0')
    text(d, (TW / 2, 200), 'CAD FROM A SENTENCE', 92, 255, anchor='ma')
    inverse(d, (TW / 2, 340), ' FOR $0 ', 150, anchor='ma', pad=14)
    if t >= WT['save'] - 0.08: text(d, (40, 620), typed('> save this reel', WT['save'] - 0.08, t, 34), 66, 230)
    if t >= WT['follow'] - 0.08:
        text(d, (40, 710), typed('> follow', WT['follow'] - 0.08, t, 30), 66, 230)
        if t >= WT['nopay'] - 0.05:
            sz = pop(t, WT['nopay'], 132)
            text(d, (TW / 2, 820), 'nopay.exe', sz, 255, anchor='ma'); cursor(d, TW / 2 + tw('nopay.exe', sz) / 2, 820, sz, t)
    if t >= WT['more'] - 0.3: text(d, (TW / 2, 990), typed('for more free AI', WT['more'] - 0.3, t, 30), 72, 220, anchor='ma')

C.SCENES = [s_hook, s_search, s_free, s_end]

# ---------- subtitles (safe zone: output y <= 1440, right 230 px clear) ----------
words = json.load(open(f'{A}/words.json'))
ws = []
for w, a, b in words:
    lw = w.lower()
    if (w.startswith('-') or w.startswith('.') or w.startswith(',')) and ws: ws[-1][0] += w; ws[-1][2] = b; continue
    if lw in ('anti',) : w = 'Anti'
    ws.append([w, a, b])
for w in ws:
    w[0] = w[0].replace('Anti-Gravity', 'Antigravity').replace('NoPay.exe', 'nopay.exe').replace('ZCAD', 'zCAD').replace('$0', '$0').replace('perplexity.ai', 'perplexity.ai')
# merge "Google" "Anti-Gravity." tokens, "9,000" ok
G = []; cur = []
for w in ws:
    if cur and w[1] - cur[-1][2] > 0.35: G.append(cur); cur = []
    cur.append(w)
    if len(cur) >= 3 or w[0][-1] in '.,!': G.append(cur); cur = []
if cur: G.append(cur)
C.GROUPS = G
SUBX, SUBMAX, SUBY = 400, 700, 1150
def subtitles(d, t):
    if t < WT['this'] - 0.03: return
    g = None
    for i, gr in enumerate(G):
        end = G[i + 1][0][1] if i + 1 < len(G) else 99
        if gr[0][1] - 0.05 <= t < min(end - 0.05, gr[-1][2] + 0.7): g = gr
    if not g: return
    tx = [w[0].strip('.,!').upper() if not w[0].lower().startswith(('zcad', 'nopay')) else w[0].strip('.,!') for w in g]
    size = 88
    while size > 40:
        sp = size * 0.35; tot = sum(tw(x, size) for x in tx) + sp * (len(tx) - 1)
        if tot <= SUBMAX: break
        size -= 4
    x = SUBX - tot / 2; y = SUBY
    d.rectangle((0, SUBY - 24, TW, SUBY + size + 20), fill=0)
    for w, s in zip(g, tx):
        if t >= w[1] - 0.03:
            if t < w[2] + 0.05: inverse(d, (x, y), s, size, pad=6)
            else: text(d, (x, y), s, size, 235)
        x += tw(s, size) + sp
C.subtitles = subtitles
_orig_screen = C.screen
def screen(t, si=None):
    if si is None: si = C.scene_index(t)
    im = Image.new('L', (TW, C.THh), 0); d = ImageDraw.Draw(im)
    buf = np.zeros((C.THh, TW), np.float32)
    FOOT.clear()
    C.SCENES[si](d, buf, t)
    subtitles(d, t)
    if t >= WT['this']: text(d, (30, 1300), '>', 60, 200); cursor(d, 58, 1300, 60, t)
    I = np.maximum(np.asarray(im, np.float32), buf)
    out = np.zeros((C.THh, TW, 5), np.float32); out[..., 0] = I
    if 'g' in FOOT:
        h, w = 562, 900
        out[WY:WY + h, WX:WX + w, 1:4] = FOOT['g']; out[WY:WY + h, WX:WX + w, 4] = 1.0
        out[WY:WY + h, WX:WX + w, 0] = 0
    return out
C.screen = screen

# CRT pass that keeps the website footage in its original colours
_yy = C.yy
def crt_color(S, t, power=1.0):
    if S.ndim == 2: S = np.dstack([S, np.zeros(S.shape + (4,), np.float32)])
    r = C.rng(int(t * 30) + 77)
    x = S[..., 0] / 255.0
    hb = ((t * 0.18) % 1.3 - 0.15) * C.THh
    hum = (0.93 + 0.07 * np.exp(-((_yy[:, :1] - hb) / 110) ** 2))
    flick = (0.97 + 0.03 * r.random())
    x = x * hum * C.SCAN * flick
    col = x[..., None] * C.P1 + (x[..., None] ** 3) * (C.HOT - C.P1) * 0.6
    bright = np.clip(x - 0.35, 0, 1)
    bl = cv2.GaussianBlur(bright, (0, 0), 6) * 0.55 + cv2.GaussianBlur(bright, (0, 0), 22) * 0.45
    col = col + bl[..., None] * C.P1 * 0.9
    m = S[..., 4:5]
    foot = S[..., 1:4] * (0.80 + 0.20 * C.SCAN[..., None]) * hum[..., None]   # light scanlines on the real screen
    fb = cv2.GaussianBlur(np.ascontiguousarray(foot), (0, 0), 8) * 0.12            # soft glow
    col = col * (1 - m) + (foot + fb) * m
    col = col * C.VIG[..., None]
    out = np.empty_like(col)
    for c in range(3): out[..., c] = cv2.remap(np.ascontiguousarray(col[..., c]), C.MAPS[c][0], C.MAPS[c][1], cv2.INTER_LINEAR, borderValue=0)
    out = out * C.TUBE[..., None] * power
    out += 0.018 * np.array([0.5, 1, 0.6]) * C.TUBE[..., None]
    out += C.GLASS[..., None] * np.array([1.0, 0.95, 0.85])
    out += r.normal(0, 0.012, (C.THh, TW, 1)).astype(np.float32)
    frame = C.BEZEL.copy(); tube = np.clip(out * 255, 0, 255)
    reg = frame[C.TY:C.TY + C.THh, C.TX:C.TX + TW]
    frame[C.TY:C.TY + C.THh, C.TX:C.TX + TW] = reg * (1 - C.TUBE[..., None]) + tube * C.TUBE[..., None]
    return np.clip(frame, 0, 255).astype(np.uint8)
C.crt = crt_color
def power_on(t):
    I = np.zeros((C.THh, TW), np.float32)
    if t < 0.08: cv2.circle(I, (TW // 2, C.THh // 2), 6, 255, -1); return I, 1.0
    if t < 0.16:
        w = int(TW * (t - 0.08) / 0.08); cv2.rectangle(I, (TW // 2 - w // 2, C.THh // 2 - 3), (TW // 2 + w // 2, C.THh // 2 + 3), 255, -1); return I, 1.0
    if t < 0.24:
        h = int(C.THh * (t - 0.16) / 0.08); cv2.rectangle(I, (0, C.THh // 2 - h // 2), (TW, C.THh // 2 + h // 2), 150, -1)
        return np.maximum(I, screen(t, 0)[..., 0] * 0.6), 1.0
    return None, 1.0
C.power_on = power_on

if __name__ == '__main__':
    if sys.argv[1] == 'check':
        os.makedirs(os.path.join(A, 'out'), exist_ok=True)
        for ts in sys.argv[2:]: Image.fromarray(C.frame_at(float(ts))).save(os.path.join(A, 'out', f'c_{ts}.png'))
    else:
        a, b = int(sys.argv[1]), int(sys.argv[2]); os.makedirs(os.path.join(A, 'frames'), exist_ok=True)
        for i in range(a, b): Image.fromarray(C.frame_at(i / FPS)).save(os.path.join(A, 'frames', f'{i:04d}.jpg'), quality=93)
