# 009 Wanaka Studio — AI game maker: one sentence -> playable 3D game (wanaka.app)
# Pricing page (wanaka.app/#pricing, read 2026-11-12): Free $0 forever, no credit card, 60 credits/day, Wanaka 1.0 Lite.
# Source: Product Hunt weekly leaderboard, week of Nov 2 2026 (#2).
N = 9
DUR = 31.95
ROLLS = [7.4, 20.5, 26.1]
STATUS = [(2.2, 'GAME MAKER'), (5.5, 'SEARCH'), (7.4, 'BUILD'), (15.0, 'SHARE'), (20.5, 'PRICE CHECK'), (26.1, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(1.12, 'GAME DEVS'), until=2.2)
SEARCH = dict(domain='wanaka.app', t0=5.7, t1=6.6, until=7.4)
FIX = {'Wanaka': 'wanaka', 'or': 'Or'}
WINDOWS = [
    (2.2, 5.5, 'fr_home', 4.0, 7.5, ' wanaka.app '),
    (5.5, 7.4, 'gs', 0, 0, ' google.com '),
    (7.4, 12.3, 'fr_home', 24.0, 28.5, ' wanaka.app '),
    (12.3, 15.0, 'fr_home', 22.0, 23.9, ' wanaka.app/#games '),
    (15.0, 20.5, 'fr_home', 9.5, 13.6, ' wanaka.app '),
    (20.5, 26.1, 'fr_pricing', 1.6, 16.3, ' wanaka.app/#pricing '),
]
LABELS = [
    dict(t0=2.4, t1=5.5, kind='type', text='> 1 sentence = 3D game', x=40, y=230, size=62),
    dict(t0=4.78, t1=5.5, kind='inv', text=' WANAKA ', x=40, y=110, size=80),
    dict(t0=8.86, t1=12.3, kind='inv', text=' AI GAME TEAM ', x=40, y=110, size=72),
    dict(t0=10.2, t1=12.3, kind='type', text='> world, characters, music', x=40, y=210, size=52),
    dict(t0=13.04, t1=15.0, kind='inv', text=' REMIX ', x=40, y=110, size=72),
    dict(t0=13.44, t1=15.0, kind='type', text="> other people's games", x=40, y=210, size=52),
    dict(t0=15.74, t1=20.5, kind='inv', text=' 1 LINK ', x=40, y=110, size=72),
    dict(t0=16.78, t1=20.5, kind='type', text='> friends play in browser', x=40, y=210, size=52),
    dict(t0=18.82, t1=20.5, kind='inv', text=' NO CODE ', x=40, y=992, size=52),
    dict(t0=19.52, t1=20.5, kind='inv', text=' NO DOWNLOAD ', x=290, y=992, size=52),
    dict(t0=21.52, t1=26.1, kind='inv', text=' $0 FOREVER ', x=40, y=110, size=72, hit=True),
    dict(t0=23.44, t1=26.1, kind='type', text='> no credit card', x=40, y=210, size=52),
    dict(t0=24.6, t1=26.1, kind='inv', text=' 60 CREDITS / DAY ', x=40, y=992, size=56),
    dict(t0=26.15, kind='text', text='FREE GAME MAKER', x=480, y=200, size=88, anchor='ma'),
    dict(t0=26.15, kind='inv', text=' $0 PLAN ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=26.2, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=27.08, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=27.4, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=27.4, kind='cursor', x=760, y=820, size=132),
    dict(t0=28.94, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
