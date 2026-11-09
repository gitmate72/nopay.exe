# 007 Open Generative AI — open-source AI image/video studio (github.com/Anil-matcha/Open-Generative-AI, MIT, ~33.6k stars)
# Free = the app (MIT). Local image models run offline free; cloud models use Muapi.ai credits (said in the reel).
N = 7
DUR = 29.8
ROLLS = [10.8, 13.5, 17.35, 24.9]
STATUS = [(2.05, 'AI STUDIO'), (10.8, 'SEARCH'), (13.5, 'STUDIOS'), (17.35, 'LICENSE'), (24.9, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING PER')], inverse=(0.96, 'AI VIDEO'), until=2.05)
SEARCH = dict(domain='github.com/Anil-matcha/Open-Generative-AI', t0=11.3, t1=12.9, until=13.5)
FIX = {}
WINDOWS = [
    (2.05, 10.8, 'fr_demo', 1.0, 9.0, ' muapi.ai/open-generative-ai '),
    (10.8, 13.5, 'gs', 0, 0, ' google.com '),
    (13.5, 17.35, 'fr_demo', 14.0, 24.0, ' muapi.ai/open-generative-ai '),
    (17.4, 24.9, 'fr_gh', 3.0, 16.0, ' github.com/Anil-matcha/Open-Generative-AI '),
]
LABELS = [
    dict(t0=2.86, t1=10.8, kind='count', to=600, step=10, t_end=3.74, suffix='+ MODELS', x=40, y=110, size=84),
    dict(t0=5.16, t1=10.8, kind='inv', text=' OPEN SOURCE ', x=40, y=220, size=64),
    dict(t0=6.4, t1=10.8, kind='inv', text=' OPEN GENERATIVE AI ', x=40, y=990, size=56),
    dict(t0=8.54, t1=10.8, kind='type', text='= Higgsfield, but open source', x=40, y=1056, size=50),
    dict(t0=13.96, t1=17.35, kind='inv', text=' IMAGES ', x=40, y=110, size=60),
    dict(t0=14.26, t1=17.35, kind='inv', text=' VIDEOS ', x=300, y=110, size=60),
    dict(t0=14.84, t1=17.35, kind='count', to=14, t_end=15.38, suffix=' STUDIOS', x=40, y=200, size=76),
    dict(t0=16.12, t1=17.35, kind='type', text='> all in one app', x=40, y=995, size=60),
    dict(t0=17.48, t1=24.9, kind='inv', text=' APP: FREE ', x=40, y=110, size=64),
    dict(t0=18.72, t1=24.9, kind='inv', text=' MIT LICENSE ', x=40, y=200, size=64, hit=True),
    dict(t0=20.2, t1=24.9, kind='type', text='> local image models: offline, free', x=40, y=992, size=48),
    dict(t0=22.74, t1=24.9, kind='type', text='> cloud models: use credits', x=40, y=1052, size=48),
    dict(t0=24.95, kind='text', text='OPEN AI STUDIO', x=480, y=200, size=92, anchor='ma'),
    dict(t0=24.95, kind='inv', text=' $0 APP ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=25.0, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=25.7, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=26.08, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=26.08, kind='cursor', x=760, y=820, size=132),
    dict(t0=27.6, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
