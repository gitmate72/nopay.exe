# nopay.exe CRT engine (Phosphor Terminal). Per-reel scripts import this, then set WT, ROLLS/SCENE_T, SCENES, subtitles.
import json, math, os, sys, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

OW, OH = 1080, 1920            # output
TX, TY, TW, THh = 60, 150, 960, 1560   # tube rect on output
FPS = 30; DUR = 34.0
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts') + '/'
_fc = {}
def F(size, fam='VT323'):
    k = (fam, size)
    if k not in _fc: _fc[k] = ImageFont.truetype(FD + {'VT323': 'VT323.ttf', 'MONO': 'SpaceMono-Bold.ttf'}[fam], size)
    return _fc[k]

def rng(seed):
    return np.random.default_rng(abs(int(seed)) % (2**32))
def clamp(x, a=0., b=1.): return max(a, min(b, x))
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)

# ---- set by each reel ----
WT = {}
ROLLS = []
SCENE_T = [0.0, 99]
SCENES = []
GROUPS = []
def subtitles(d, t): pass

# ---------------- drawing primitives on the screen buffer (mode 'L', 0..255 intensity) ----------------
def text(d, xy, s, size, val=255, anchor='la', fam='VT323'):
    d.text(xy, s, font=F(size, fam), fill=val, anchor=anchor)
def tw(s, size, fam='VT323'): return F(size, fam).getlength(s)
def typed(s, t0, t, cps=28):
    if t < t0: return ''
    return s[:min(len(s), int((t - t0) * cps) + 1)]
def inverse(d, xy, s, size, anchor='la', pad=10):
    f = F(size); x, y = xy; w = f.getlength(s); asc, desc = f.getmetrics()
    if anchor == 'ma': x -= w / 2
    d.rectangle((x - pad, y + 2, x + w + pad, y + asc + desc - 4), fill=235)
    d.text((x, y), s, font=f, fill=10)
def cursor(d, x, y, size, t, on=True):
    if on and int(t * 2.4) % 2 == 0: d.rectangle((x + 4, y + 8, x + 4 + size * 0.45, y + size * 0.92), fill=230)
def boxdraw(d, x0, y0, x1, y1, val=200, title=None, size=44):
    for o in (0, 9):  # double-line box, like ╔═╗
        d.rectangle((x0 + o, y0 + o, x1 - o, y1 - o), outline=val, width=3)
    if title:
        w = tw(title, size); d.rectangle((x0 + 28, y0 - 6, x0 + 52 + w, y0 + 22), fill=0)
        text(d, (x0 + 40, y0 - size * 0.42), title, size, val)
def arrow(d, pts, p, val=230, w=5):
    """phosphor line arrow drawing on along pts with progress p."""
    if p <= 0: return
    L = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]; tot = sum(L); want = tot * clamp(p); acc = 0; out = [pts[0]]
    for i, l in enumerate(L):
        if acc + l >= want:
            k = (want - acc) / l; out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * k, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * k)); break
        acc += l; out.append(pts[i + 1])
    d.line(out, fill=val, width=w, joint='curve')
    if p >= 0.98:
        (x0, y0), (x1, y1) = out[-2], out[-1]; a = math.atan2(y1 - y0, x1 - x0)
        for s in (2.6, -2.6): d.line([(x1, y1), (x1 + 30 * math.cos(a + s), y1 + 30 * math.sin(a + s))], fill=val, width=w)
def put_footage(buf, g, x, y, bright=0.85):
    h, w = g.shape; buf[y:y + h, x:x + w] = np.maximum(buf[y:y + h, x:x + w], g * 255 * bright)

# ---------------- scenes ----------------
def scene_index(t):
    for i in range(len(SCENE_T) - 1):
        if SCENE_T[i] <= t < SCENE_T[i + 1]: return i
    return len(SCENE_T) - 2

def screen(t, si=None):
    """intensity buffer (THh x TW) float32 0..255 for scene si at time t."""
    if si is None: si = scene_index(t)
    im = Image.new('L', (TW, THh), 0); d = ImageDraw.Draw(im)
    buf = np.zeros((THh, TW), np.float32)
    SCENES[si](d, buf, t)
    if si > 0 or t >= WT['because']:
        subtitles(d, t)
        text(d, (30, 1470), '>', 60, 200); cursor(d, 58, 1470, 60, t)
    a = np.asarray(im, np.float32)
    return np.maximum(a, buf)

# ---------------- CRT post ----------------
yy, xx = np.mgrid[0:THh, 0:TW].astype(np.float32)
nx, ny = (xx - TW / 2) / (TW / 2), (yy - THh / 2) / (THh / 2)
def _barrel(k):
    r2 = nx * nx * 0.55 + ny * ny * 0.45
    f = 1 + k * r2
    return ((nx * f) * TW / 2 + TW / 2).astype(np.float32), ((ny * f) * THh / 2 + THh / 2).astype(np.float32)
MAPS = [_barrel(k) for k in (0.105, 0.095, 0.085)]   # R, G, B -> fringing at the edges
SCAN = (0.62 + 0.38 * (np.sin(yy[:, :1] * np.pi / 2.0) ** 2)).astype(np.float32)   # 4px period scanlines
VIG = np.clip(1 - (nx ** 2 * 0.55 + ny ** 2 * 0.45) ** 1.6 * 0.75, 0, 1).astype(np.float32)
mask = np.zeros((THh, TW), np.uint8); cv2.rectangle(mask, (30, 30), (TW - 30, THh - 30), 255, -1)
MASK = cv2.GaussianBlur(cv2.erode(mask, np.ones((5, 5))), (0, 0), 14).astype(np.float32) / 255
# rounded tube mask
rm = np.zeros((THh, TW), np.uint8); cv2.rectangle(rm, (70, 0), (TW - 70, THh), 255, -1); cv2.rectangle(rm, (0, 70), (TW, THh - 70), 255, -1)
for cx, cy in [(70, 70), (TW - 70, 70), (70, THh - 70), (TW - 70, THh - 70)]: cv2.circle(rm, (cx, cy), 70, 255, -1)
TUBE = cv2.GaussianBlur(rm, (0, 0), 3).astype(np.float32) / 255

def bezel():
    rng0 = rng(5); b = np.zeros((OH, OW, 3), np.float32)
    base = np.array([38, 37, 34], np.float32)
    g = np.linspace(1.15, 0.8, OH)[:, None, None]
    b[:] = base * g + rng0.normal(0, 2.0, (OH, OW, 1))
    im = Image.fromarray(np.clip(b, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((TX - 26, TY - 26, TX + TW + 26, TY + THh + 26), 90, fill=(18, 18, 17))
    d.rounded_rectangle((TX - 8, TY - 8, TX + TW + 8, TY + THh + 8), 80, fill=(6, 7, 6))
    d.text((OW / 2, 70), 'PHOSPHOR · P1', font=F(40, 'MONO'), fill=(120, 118, 110), anchor='mm')
    d.text((OW - 120, TY + THh + 105), 'POWER', font=F(26, 'MONO'), fill=(105, 104, 98), anchor='mm')
    for i, x in enumerate([160, 300]):
        d.ellipse((x - 34, TY + THh + 72, x + 34, TY + THh + 140), fill=(26, 26, 24), outline=(70, 70, 66), width=3)
        d.line((x, TY + THh + 80, x + 10 * (i * 2 - 1), TY + THh + 104), fill=(150, 150, 140), width=4)
    return np.asarray(im, np.float32)
BEZEL = bezel()
# glass catching the room light
gl = np.zeros((THh, TW), np.float32)
gl += np.clip(1 - np.hypot((xx - TW * 0.22) / (TW * 0.55), (yy - THh * 0.12) / (THh * 0.28)), 0, 1) ** 2 * 0.10
cv2.rectangle(win := np.zeros((THh, TW), np.float32), (int(TW * 0.62), 60), (int(TW * 0.9), 230), 1.0, -1)
GLASS = gl + cv2.GaussianBlur(win, (0, 0), 30) * 0.06
P1 = np.array([0.30, 1.0, 0.42], np.float32)   # P1 green
HOT = np.array([0.75, 1.0, 0.8], np.float32)

def crt(I, t, power=1.0):
    """I: intensity 0..255 -> RGB output frame (OH,OW,3) uint8"""
    r = rng(int(t * 30) + 77)
    x = I / 255.0
    # hum bar rolling slowly
    hb = ((t * 0.18) % 1.3 - 0.15) * THh
    x = x * (0.93 + 0.07 * np.exp(-((yy[:, :1] - hb) / 110) ** 2))
    x = x * SCAN
    x = x * (0.97 + 0.03 * r.random())                       # flicker
    col = x[..., None] * P1 + (x[..., None] ** 3) * (HOT - P1) * 0.6
    # bloom / halation
    bright = np.clip(x - 0.35, 0, 1)
    bl = cv2.GaussianBlur(bright, (0, 0), 6) * 0.55 + cv2.GaussianBlur(bright, (0, 0), 22) * 0.45
    col = col + bl[..., None] * P1 * 0.9
    col = col * VIG[..., None]
    # barrel distortion with RGB fringing
    out = np.empty_like(col)
    for c in range(3): out[..., c] = cv2.remap(np.ascontiguousarray(col[..., c]), MAPS[c][0], MAPS[c][1], cv2.INTER_LINEAR, borderValue=0)
    out = out * TUBE[..., None] * power
    out += 0.018 * np.array([0.5, 1, 0.6]) * TUBE[..., None]          # phosphor black level
    out += GLASS[..., None] * np.array([1.0, 0.95, 0.85])
    out += r.normal(0, 0.012, (THh, TW, 1)).astype(np.float32)        # grain
    frame = BEZEL.copy()
    tube = np.clip(out * 255, 0, 255)
    reg = frame[TY:TY + THh, TX:TX + TW]
    frame[TY:TY + THh, TX:TX + TW] = reg * (1 - TUBE[..., None]) + tube * TUBE[..., None] + reg * 0
    # tube light spilling on the bezel lip
    return np.clip(frame, 0, 255).astype(np.uint8)

def power_on(t):
    """returns (intensity buffer, power) for t<0.32: dot -> line -> raster flash."""
    I = np.zeros((THh, TW), np.float32)
    if t < 0.08:
        cv2.circle(I, (TW // 2, THh // 2), 6, 255, -1); return I, 1.0
    if t < 0.16:
        w = int(TW * (t - 0.08) / 0.08); cv2.rectangle(I, (TW // 2 - w // 2, THh // 2 - 3), (TW // 2 + w // 2, THh // 2 + 3), 255, -1); return I, 1.0
    if t < 0.24:
        h = int(THh * (t - 0.16) / 0.08); I[:] = 0; cv2.rectangle(I, (0, THh // 2 - h // 2), (TW, THh // 2 + h // 2), 150, -1)
        return np.maximum(I, screen(t, 0) * 0.6), 1.0
    return None, 1.0

def frame_at(t):
    if t < 0.24:
        I, pw = power_on(t)
        return crt(I, t, pw)
    I = None
    for rt in ROLLS:
        if rt - 0.2 <= t < rt + 0.2:          # V-hold roll between screens
            p = ease((t - (rt - 0.2)) / 0.4); si = scene_index(rt + 0.01)
            old = screen(min(t, rt - 0.001), si - 1); new = screen(max(t, rt + 0.001), si)
            off = int(p * THh); I = np.zeros_like(old)
            I[:THh - off] = old[off:]; I[THh - off:] = new[:off]
            bar = THh - off; I[max(0, bar - 40):min(THh, bar + 40)] = 0
            I = I * (1.15 if 0.3 < p < 0.7 else 1.0)
            break
    if I is None: I = screen(t)
    warm = clamp((t - 0.24) / 0.6)            # raster settles as the phosphor warms
    return crt(I * (1.25 - 0.25 * warm), t)

