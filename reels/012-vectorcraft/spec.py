# 012 VectorCraft — free, open-source vector illustration app (Adobe Illustrator alternative) by ArtCraft (getartcraft.com)
# Official page (getartcraft.com/apps/vectorcraft, read 2026-11-15): "Open source, and in your browser too." / "OPEN SOURCE · FREE".
# getartcraft.com: "ArtCraft builds open source tools, free to use." "NO SUBSCRIPTION REQUIRED". Paid plans = AI image/video credits for ArtCraft Studio only.
# github.com/storytold/vectorcraft: license MIT OR Apache-2.0, ~11.7k stars, status alpha; macOS/Windows/Linux/FreeBSD + web (WASM); MCP server so Claude can draw/edit/export.
# Source: XDA Developers, Nov 8 2026, "I ditched Inkscape for an open-source Illustrator rival built with AI".
N = 12
DUR = 33.8
ROLLS = [9.22, 21.32, 27.56]
STATUS = [(2.24, 'VECTOR APP'), (6.46, 'SEARCH'), (9.22, 'PEN TOOL'), (13.86, 'FILES'), (16.82, 'AI AGENT'), (19.38, 'PLATFORMS'),
          (21.32, 'PRICE CHECK'), (27.56, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(1.02, 'ILLUSTRATOR'), until=2.24)
SEARCH = dict(domain='getartcraft.com', t0=6.6, t1=8.1, until=9.22)
FIX = {'Vectorcraft.': 'VectorCraft.', 'getartcraft': 'getartcraft', '.com.': '.com', 'pathfinder,': 'Pathfinder,',
       'notepay': 'nopay', 'Save': 'Save', '.exe': '.exe'}
WINDOWS = [
    (2.24, 6.46, 'fr_vc', 2.5, 6.7, ' getartcraft.com '),
    (6.46, 9.22, 'gs', 0, 0, ' google.com '),
    (9.22, 11.62, 'fr_vc', 17.2, 19.6, ' getartcraft.com/apps/vectorcraft '),
    (11.62, 13.86, 'fr_vc', 33.0, 35.1, ' getartcraft.com/apps/vectorcraft '),
    (13.86, 16.82, 'fr_vc', 29.4, 32.4, ' getartcraft.com/apps/vectorcraft '),
    (16.82, 18.0, 'fr_vc', 20.3, 21.5, ' getartcraft.com/apps/vectorcraft '),
    (18.0, 19.38, 'fr_vc', 24.2, 25.6, ' getartcraft.com/apps/vectorcraft '),
    (19.38, 21.32, 'fr_gh', 22.0, 23.9, ' github.com/storytold/vectorcraft '),
    (21.32, 24.94, 'fr_gh', 8.0, 11.6, ' github.com/storytold/vectorcraft '),
    (24.94, 27.56, 'fr_look', 19.0, 21.6, ' github.com/storytold/vectorcraft '),
]
LABELS = [
    dict(t0=2.5, t1=6.46, kind='inv', text=' VECTOR ART APP ', x=40, y=110, size=64),
    dict(t0=3.26, t1=6.46, kind='type', text='> free + open source', x=40, y=210, size=56),
    dict(t0=5.12, t1=6.46, kind='inv', text=' VECTORCRAFT ', x=40, y=992, size=64),
    dict(t0=9.86, t1=11.62, kind='inv', text=' PEN TOOL ', x=40, y=110, size=64),
    dict(t0=10.78, t1=11.62, kind='inv', text=' PATHFINDER ', x=40, y=992, size=60),
    dict(t0=11.76, t1=13.86, kind='inv', text=' LIVE EFFECTS ', x=40, y=110, size=64),
    dict(t0=12.78, t1=13.86, kind='type', text='> outer glow', x=40, y=210, size=56),
    dict(t0=13.98, t1=16.82, kind='inv', text=' OPENS SVG + PDF ', x=40, y=110, size=64),
    dict(t0=16.94, t1=19.38, kind='inv', text=' CLAUDE CAN DRAW ', x=40, y=110, size=64),
    dict(t0=17.72, t1=19.38, kind='type', text='> via MCP server', x=40, y=210, size=56),
    dict(t0=19.38, t1=21.32, kind='inv', text=' MAC ', x=40, y=110, size=60),
    dict(t0=19.72, t1=21.32, kind='inv', text=' WINDOWS ', x=200, y=110, size=60),
    dict(t0=20.5, t1=21.32, kind='inv', text=' LINUX ', x=500, y=110, size=60),
    dict(t0=22.18, t1=27.56, kind='inv', text=' $0 FREE ', x=40, y=110, size=72, hit=True),
    dict(t0=22.66, t1=27.56, kind='type', text='> open source (MIT/Apache)', x=40, y=210, size=48),
    dict(t0=23.66, t1=24.94, kind='inv', text=' NO SUBSCRIPTION ', x=40, y=992, size=56),
    dict(t0=25.6, t1=27.56, kind='inv', text=' ALPHA: EARLY BUILD ', x=40, y=992, size=56),
    dict(t0=27.6, kind='text', text='FREE ILLUSTRATOR', x=480, y=200, size=80, anchor='ma'),
    dict(t0=27.6, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=27.62, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=28.8, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=29.14, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=29.14, kind='cursor', x=760, y=820, size=132),
    dict(t0=30.76, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
