"""Spec-driven nopay.exe reel (green CRT terminal, website footage in original colours).

A reel folder needs:  spec.py  +  assets/{vo.wav, words.json, gs/*.png, fr_<name>/*.jpg}
run:   python3 reels/_lib/specreel.py reels/NNN-slug check 1.0 5.2 ...   (writes assets/out/c_<t>.png)
       python3 reels/_lib/specreel.py reels/NNN-slug <frame_from> <frame_to>  (writes assets/frames/)
spec.py defines (times in seconds of the tightened voice):
  N            reel number shown in the status line ("nopay.exe #N")
  DUR          total length (voice + ~1 s)
  ROLLS        times of V-hold roll scene changes
  STATUS       list of (t, label) for the right side of the status line
  HOOK         dict(lines=[(t, text)], inverse=(t, text), until=t)  big centred hook, before t=until
  SEARCH       dict(domain=..., t0=typing start, t1=typing end, until=t, title=' google.com ')
  WINDOWS      list of (t0, t1, source, s0, s1, title): footage window; source 'fr_<name>' plays
               s0..s1 seconds of that recording across t0..t1
  LABELS       list of dicts: t0, t1 (default 99), kind 'type'|'text'|'inv'|'big'|'count',
               text, x, y, size, cps (type), anchor 'la'|'ma'|'ra', to/t_end/suffix (count), hit (bool)
  ARROWS       list of (t0, dur, [(x,y),...])
  FIX          dict word->display word for subtitles (optional)
Screen buffer is 960x1560; window at (30,400) 900x562. Keep labels in y 100-385 or 985-1110.
Subtitles sit at y=1150 (safe zone). Final card ("nopay.exe" + cursor) is just LABELS.
"""
import importlib.util, json, os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'pipeline', 'engine'))
import crt_engine as C

REEL = os.path.abspath(sys.argv[1])
A = os.path.join(REEL, 'assets')
_s = importlib.util.spec_from_file_location('spec', os.path.join(REEL, 'spec.py'))
S = importlib.util.module_from_spec(_s); _s.loader.exec_module(S)
FPS = 30
TW, THh = C.TW, C.THh
WX, WY, WW, WH = 30, 400, 900, 562
text, inverse, tw, typed, cursor, boxdraw, arrow = C.text, C.inverse, C.tw, C.typed, C.cursor, C.boxdraw, C.arrow
C.ROLLS = list(S.ROLLS); C.SCENE_T = [0.0] + list(S.ROLLS) + [99]

# ---------- footage ----------
_cache = {}
def load(p):
    if p in _cache: return _cache[p]
    g = np.asarray(Image.open(p).convert('RGB').resize((WW, WH), Image.LANCZOS), np.float32) / 255
    if len(_cache) > 240: _cache.clear()
    _cache[p] = g; return g
def gs_frame(t):
    s = S.SEARCH; dom = s['domain']; n = len(dom)
    if t < s['t0'] - 0.5: nm = '00'
    elif t < s['t0']: nm = '01'
    else:
        k = int((t - s['t0']) / max(0.03, (s['t1'] - s['t0']) / n)) + 1
        nm = (f'{n + 1:02d}' if t < s['until'] - 0.4 else '99') if k >= n else f'{k + 1:02d}'
    p = os.path.join(A, 'gs', nm + '.png')
    return load(p if os.path.exists(p) else os.path.join(A, 'gs', '99.png'))
def footage(t):
    for (t0, t1, src, s0, s1, title) in S.WINDOWS:
        if t0 <= t < t1:
            if src == 'gs': return gs_frame(t), title
            d = os.path.join(A, src); n = len(os.listdir(d))
            s = s0 + (s1 - s0) * C.clamp((t - t0) / max(1e-6, t1 - t0))
            return load(os.path.join(d, f'{max(1, min(n, int(s * 30) + 1)):04d}.jpg')), title
    return None, None

# ---------- drawing ----------
def pop(t, at, base): return int(base * (1.18 if 0 <= t - at < 0.08 else 1))
def status(d, t):
    lab = ''
    for (ts, l) in S.STATUS:
        if t >= ts: lab = l
    d.rectangle((0, 18, TW, 84), fill=230)
    text(d, (24, 22), f'nopay.exe #{S.N}', 54, 8); text(d, (TW - 24, 22), lab, 54, 8, anchor='ra')
def fit(s, size, maxw):
    while size > 30 and tw(s, size) > maxw: size -= 4
    return size
def draw_label(d, L, t):
    t0, t1 = L['t0'], L.get('t1', 99)
    if not (t0 <= t < t1): return
    k = L.get('kind', 'text'); s = L.get('text', ''); x, y = L.get('x', 40), L.get('y', 120)
    size = L.get('size', 60); anchor = L.get('anchor', 'la'); maxw = L.get('maxw', 880)
    if k == 'type':
        s = typed(s, t0, t, L.get('cps', 30)); size = fit(L['text'], size, maxw)
        text(d, (x, y), s, size, L.get('val', 240), anchor=anchor)
    elif k == 'text':
        text(d, (x, y), s, fit(s, size, maxw), L.get('val', 240), anchor=anchor)
    elif k in ('inv', 'big'):
        sz = fit(s, size, maxw - 30)
        if x == 'right': x = TW - 40 - tw(s, sz) - 10; anchor = 'la'
        inverse(d, (x, y), s, pop(t, t0, sz), anchor=anchor, pad=L.get('pad', 8))
    elif k == 'count':
        p = C.clamp((t - t0) / max(1e-6, L['t_end'] - t0)); st = int(p * 10)
        v = L['to'] * (1 - (1 - st / 10) ** 2); v = int(round(v / L.get('step', 1)) * L.get('step', 1))
        s2 = L.get('fmt', '{:,}').format(v) + (L.get('suffix', '') if p >= 1 else '')
        sz = fit(s2, size, maxw)
        if p >= 1: inverse(d, (x, y), ' ' + s2 + ' ', pop(t, L['t_end'], sz), anchor=anchor, pad=8)
        else: text(d, (x, y), s2, sz, 255, anchor=anchor)
    elif k == 'cursor':
        cursor(d, x, y, size, t)
    if L.get('wipe'): pass

FIX = getattr(S, 'FIX', {})
words = json.load(open(os.path.join(A, 'words.json')))
ws = []
for w, a, b in words:
    if (w[:1] in '-.,') and ws: ws[-1][0] += w; ws[-1][2] = b; continue
    ws.append([FIX.get(w, FIX.get(w.lower(), w)), a, b])
G = []; cur = []
for w in ws:
    if cur and w[1] - cur[-1][2] > 0.35: G.append(cur); cur = []
    cur.append(w)
    if len(cur) >= 3 or w[0][-1] in '.,!?': G.append(cur); cur = []
if cur: G.append(cur)
KEEP_CASE = tuple(getattr(S, 'KEEP_CASE', ('nopay', 'github', 'http')))
def subtitles(d, t):
    if t < S.HOOK['until'] - 0.03: return
    g = None
    for i, gr in enumerate(G):
        end = G[i + 1][0][1] if i + 1 < len(G) else 99
        if gr[0][1] - 0.05 <= t < min(end - 0.05, gr[-1][2] + 0.7): g = gr
    if not g: return
    tx = [w[0].strip('.,!?"') if w[0].lower().startswith(KEEP_CASE) or '.' in w[0].strip('.,!?') else w[0].strip('.,!?"').upper() for w in g]
    size = 88
    while size > 40:
        sp = size * 0.35; tot = sum(tw(x, size) for x in tx) + sp * (len(tx) - 1)
        if tot <= 700: break
        size -= 4
    x = 400 - tot / 2; y = 1150
    d.rectangle((0, 1126, TW, 1150 + size + 20), fill=0)
    for w, s in zip(g, tx):
        if t >= w[1] - 0.03:
            if t < w[2] + 0.05: inverse(d, (x, y), s, size, pad=6)
            else: text(d, (x, y), s, size, 235)
        x += tw(s, size) + sp

def hook(d, t):
    h = S.HOOK
    lines = [s for (ts, s) in h['lines'] if t >= ts - 0.03]
    y = 300
    for s in lines[-2:]:
        text(d, (TW / 2, y), s, fit(s, 128, 900), 255, anchor='ma'); y += 150
    if 'inverse' in h and t >= h['inverse'][0] - 0.04:
        s = h['inverse'][1]; inverse(d, (TW / 2, y + 20), s, pop(t, h['inverse'][0], fit(s, 140, 860)), anchor='ma', pad=16)

def search(d, t):
    s = S.SEARCH
    if not (s['t0'] - s.get('lead', 0.6) <= t < s['until']): return False
    dom = s['domain']; n = len(dom)
    if t >= s['t0']:
        k = min(n, int((t - s['t0']) / max(0.03, (s['t1'] - s['t0']) / n)) + 1)
        shown = dom[:k]
    else: shown = ''
    size = fit(dom, 140, 880); x0 = TW / 2 - tw(dom, size) / 2
    text(d, (40, 196), 'SEARCH>', 52, 200)
    text(d, (x0, 250), shown, size, 255); cursor(d, x0 + tw(shown, size), 250, size, t)
    yb = 250 + size * 1.05
    if len(shown) == n: d.line((x0, yb, x0 + tw(dom, size), yb), fill=255, width=6)
    arrow(d, [(TW / 2, yb + 6), (TW / 2, WY + 280)], C.clamp((t - s['t1'] - 0.05) / 0.3), 255)
    return True

FOOT = {}
def screen(t, si=None):
    im = Image.new('L', (TW, THh), 0); d = ImageDraw.Draw(im)
    FOOT.clear()
    if t < S.HOOK['until'] - 0.03:
        hook(d, t)
        for L in S.LABELS:
            if L.get('hook'): draw_label(d, L, t)
    else:
        status(d, t)
        g, title = footage(t)
        if g is not None:
            boxdraw(d, WX - 14, WY - 14, WX + WW + 14, WY + WH + 14, 200, title, 44); FOOT['g'] = g
        searching = search(d, t)
        for L in S.LABELS:
            if L.get('hook'): continue
            if searching and L.get('y', 0) < 390 and not L.get('keep'): continue
            draw_label(d, L, t)
        for (t0, dur, pts) in getattr(S, 'ARROWS', []):
            if t >= t0: arrow(d, pts, C.clamp((t - t0) / dur), 255)
        subtitles(d, t)
        text(d, (30, 1300), '>', 60, 200); cursor(d, 58, 1300, 60, t)
    I = np.asarray(im, np.float32)
    out = np.zeros((THh, TW, 5), np.float32); out[..., 0] = I
    if 'g' in FOOT:
        out[WY:WY + WH, WX:WX + WW, 1:4] = FOOT['g']; out[WY:WY + WH, WX:WX + WW, 4] = 1.0
        out[WY:WY + WH, WX:WX + WW, 0] = 0
    return out
C.screen = screen

_yy = C.yy
def crt_color(Sx, t, power=1.0):
    if Sx.ndim == 2: Sx = np.dstack([Sx, np.zeros(Sx.shape + (4,), np.float32)])
    r = C.rng(int(t * 30) + 77)
    x = Sx[..., 0] / 255.0
    hb = ((t * 0.18) % 1.3 - 0.15) * THh
    hum = (0.93 + 0.07 * np.exp(-((_yy[:, :1] - hb) / 110) ** 2))
    x = x * hum * C.SCAN * (0.97 + 0.03 * r.random())
    col = x[..., None] * C.P1 + (x[..., None] ** 3) * (C.HOT - C.P1) * 0.6
    bright = np.clip(x - 0.35, 0, 1)
    bl = cv2.GaussianBlur(bright, (0, 0), 6) * 0.55 + cv2.GaussianBlur(bright, (0, 0), 22) * 0.45
    col = col + bl[..., None] * C.P1 * 0.9
    m = Sx[..., 4:5]
    foot = Sx[..., 1:4] * (0.80 + 0.20 * C.SCAN[..., None]) * hum[..., None]
    fb = cv2.GaussianBlur(np.ascontiguousarray(foot), (0, 0), 8) * 0.12
    col = col * (1 - m) + (foot + fb) * m
    col = col * C.VIG[..., None]
    out = np.empty_like(col)
    for c in range(3): out[..., c] = cv2.remap(np.ascontiguousarray(col[..., c]), C.MAPS[c][0], C.MAPS[c][1], cv2.INTER_LINEAR, borderValue=0)
    out = out * C.TUBE[..., None] * power
    out += 0.018 * np.array([0.5, 1, 0.6]) * C.TUBE[..., None]
    out += C.GLASS[..., None] * np.array([1.0, 0.95, 0.85])
    out += r.normal(0, 0.012, (THh, TW, 1)).astype(np.float32)
    frame = C.BEZEL.copy(); tube = np.clip(out * 255, 0, 255)
    reg = frame[C.TY:C.TY + THh, C.TX:C.TX + TW]
    frame[C.TY:C.TY + THh, C.TX:C.TX + TW] = reg * (1 - C.TUBE[..., None]) + tube * C.TUBE[..., None]
    return np.clip(frame, 0, 255).astype(np.uint8)
C.crt = crt_color
def power_on(t):
    I = np.zeros((THh, TW), np.float32)
    if t < 0.08: cv2.circle(I, (TW // 2, THh // 2), 6, 255, -1); return I, 1.0
    if t < 0.16:
        w = int(TW * (t - 0.08) / 0.08); cv2.rectangle(I, (TW // 2 - w // 2, THh // 2 - 3), (TW // 2 + w // 2, THh // 2 + 3), 255, -1); return I, 1.0
    if t < 0.24:
        h = int(THh * (t - 0.16) / 0.08); cv2.rectangle(I, (0, THh // 2 - h // 2), (TW, THh // 2 + h // 2), 150, -1)
        return np.maximum(I, screen(t)[..., 0] * 0.6), 1.0
    return None, 1.0
C.power_on = power_on

if __name__ == '__main__':
    if sys.argv[2] == 'check':
        os.makedirs(os.path.join(A, 'out'), exist_ok=True)
        for ts in sys.argv[3:]: Image.fromarray(C.frame_at(float(ts))).save(os.path.join(A, 'out', f'c_{ts}.png'))
    else:
        a, b = int(sys.argv[2]), int(sys.argv[3]); os.makedirs(os.path.join(A, 'frames'), exist_ok=True)
        for i in range(a, b): Image.fromarray(C.frame_at(i / FPS)).save(os.path.join(A, 'frames', f'{i:04d}.jpg'), quality=90)
