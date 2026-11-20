# 017 SolidCraft — free, open-source parametric 3D CAD (Autodesk Fusion alt), desktop + browser
# Official site solidcraft.io (read 2026-11-20): "Open-source parametric CAD. Built in Rust." "Desktop + browser",
#   "Windows / macOS / Linux / FreeBSD", "Try in your browser", "AI is optional". v0.45.0 released Nov 19 2026.
#   solidcraft.io/licenses: "SolidCraft is licensed under MIT OR Apache-2.0, at your option." No paid plan / pricing page.
# Repo github.com/tangency-labs/solidcraft (17.3k stars). New: listed Oct 2026 on saasisdead.si/new under Autodesk Fusion;
#   Hackaday Oct 17 2026; pbxscience Nov 17 2026. README: "Early but usable for simple parts".
# Footage: the official demo recordings playing on solidcraft.io (hero, parameters, MCP rover), cropped from the page
#   recording (the browser app needs a GPU and stays on its loading screen headless).
N = 17
DUR = 34.3
ROLLS = [11.3, 15.8, 19.6, 23.2, 27.92]
STATUS = [(2.2, 'FREE CAD'), (8.9, 'SEARCH'), (11.3, 'SKETCH'), (15.8, 'PARAMETERS'),
          (19.6, 'AI AGENT'), (23.2, 'PRICE CHECK'), (27.92, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.92, '3D CAD'), until=2.2)
SEARCH = dict(domain='solidcraft.io', t0=9.0, t1=9.9, until=11.3)
FIX = {'fusion': 'Fusion', 'SolidCraft': 'SolidCraft', '.io.': '.io', 'nopay': 'nopay'}
WINDOWS = [
    (2.2, 8.9, 'fr_home', 2.0, 8.0, ' solidcraft.io '),
    (8.9, 11.3, 'gs', 0, 0, ' google.com '),
    (11.3, 15.8, 'fr_hero', 1.0, 7.5, ' solidcraft.io / demo '),
    (15.8, 19.6, 'fr_param', 0.5, 8.0, ' solidcraft.io / parameters '),
    (19.6, 23.2, 'fr_rover', 1.0, 6.9, ' solidcraft.io / mcp '),
    (23.2, 25.0, 'fr_licenses', 3.0, 6.0, ' solidcraft.io / licenses '),
    (25.0, 26.6, 'fr_download', 15.0, 17.0, ' solidcraft.io / download '),
    (26.6, 27.92, 'fr_home', 2.5, 3.8, ' solidcraft.io '),
]
LABELS = [
    dict(t0=2.3, t1=8.9, kind='inv', text=' REAL 3D PARTS ', x=40, y=110, size=64),
    dict(t0=3.4, t1=8.9, kind='type', text='> free, in your browser', x=40, y=210, size=56),
    dict(t0=5.5, t1=8.9, kind='inv', text=' SOLIDCRAFT ', x=40, y=992, size=64),
    dict(t0=7.1, t1=8.9, kind='inv', text=' FUSION ALT ', x=430, y=992, size=64, hit=True),
    dict(t0=11.4, t1=15.8, kind='inv', text=' SKETCH ', x=40, y=110, size=64),
    dict(t0=12.4, t1=15.8, kind='inv', text=' DIMENSION ', x=290, y=110, size=64),
    dict(t0=13.5, t1=15.8, kind='type', text='> build a solid part', x=40, y=210, size=56),
    dict(t0=15.9, t1=19.6, kind='inv', text=' HEIGHT 24 -> 32 MM ', x=40, y=110, size=60, hit=True),
    dict(t0=18.3, t1=19.6, kind='type', text='> whole model rebuilds', x=40, y=210, size=56),
    dict(t0=19.7, t1=23.2, kind='inv', text=' AI AGENT (MCP) ', x=40, y=110, size=64),
    dict(t0=21.6, t1=23.2, kind='type', text='> builds models for you', x=40, y=210, size=56),
    dict(t0=23.3, t1=27.92, kind='inv', text=' $0 ', x=40, y=110, size=72, hit=True),
    dict(t0=23.76, t1=27.92, kind='inv', text=' OPEN SOURCE ', x=200, y=110, size=64),
    dict(t0=24.1, t1=25.0, kind='type', text='> MIT or Apache-2.0', x=40, y=210, size=56),
    dict(t0=25.0, t1=27.92, kind='type', text='> Win / Mac / Linux', x=40, y=210, size=56),
    dict(t0=26.7, t1=27.92, kind='inv', text=' + BROWSER ', x=40, y=992, size=60),
    dict(t0=27.94, kind='text', text='FREE 3D CAD', x=480, y=200, size=76, anchor='ma'),
    dict(t0=27.94, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=27.96, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=29.2, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=29.62, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=29.62, kind='cursor', x=760, y=820, size=132),
    dict(t0=31.3, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
