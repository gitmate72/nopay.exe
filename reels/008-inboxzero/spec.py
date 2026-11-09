# 008 Inbox Zero — free, open-source email app (getinboxzero.com, github.com/elie222/inbox-zero)
# Homepage: "The app is free. Add the AI only if you want it." AI plans from $20/month (pricing page). Self-hostable.
N = 8
DUR = 31.3
ROLLS = [9.6, 15.45, 24.85]
STATUS = [(1.95, 'EMAIL APP'), (7.0, 'SEARCH'), (9.6, 'INBOX'), (15.45, 'PRICE CHECK'), (24.85, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(1.02, 'SUPERHUMAN'), until=1.95)
SEARCH = dict(domain='getinboxzero.com', t0=7.5, t1=8.9, until=9.6)
FIX = {'superhuman.': 'Superhuman.', 'stop': 'Stop', 'getinboxzero.com.': 'getinboxzero.com'}
WINDOWS = [
    (1.95, 7.0, 'fr_home2', 0.0, 1.4, ' getinboxzero.com '),
    (7.0, 9.6, 'gs', 0, 0, ' google.com '),
    (9.6, 15.45, 'fr_home2', 1.5, 6.3, ' getinboxzero.com '),
    (15.5, 21.2, 'fr_pricing', 1.0, 8.0, ' getinboxzero.com/pricing '),
    (21.2, 24.85, 'fr_gh', 25.0, 26.6, ' github.com/elie222/inbox-zero '),
]
LABELS = [
    dict(t0=2.9, t1=7.0, kind='type', text='> free + open source', x=40, y=230, size=62),
    dict(t0=5.5, t1=7.0, kind='inv', text=' INBOX ZERO ', x=40, y=110, size=80),
    dict(t0=10.1, t1=15.45, kind='inv', text=' GMAIL ', x=40, y=110, size=60),
    dict(t0=10.7, t1=15.45, kind='inv', text=' OUTLOOK ', x=270, y=110, size=60),
    dict(t0=11.7, t1=15.45, kind='type', text='> one inbox', x=40, y=205, size=60),
    dict(t0=12.85, t1=15.45, kind='inv', text=' WEB ', x=40, y=992, size=52),
    dict(t0=13.6, t1=15.45, kind='inv', text=' MAC ', x=190, y=992, size=52),
    dict(t0=13.9, t1=15.45, kind='inv', text=' WINDOWS ', x=340, y=992, size=52),
    dict(t0=14.5, t1=15.45, kind='inv', text=' IPHONE ', x=620, y=992, size=52),
    dict(t0=15.5, t1=24.85, kind='inv', text=' APP: FREE ', x=40, y=110, size=72, hit=True),
    dict(t0=19.75, t1=24.85, kind='type', text='> AI assistant: optional, paid', x=40, y=210, size=52),
    dict(t0=22.2, t1=24.85, kind='inv', text=' OR SELF-HOST IT ', x=40, y=992, size=56),
    dict(t0=23.6, t1=24.85, kind='inv', text=' OPEN SOURCE ', x=40, y=1056, size=52),
    dict(t0=24.9, kind='text', text='FREE EMAIL APP', x=480, y=200, size=92, anchor='ma'),
    dict(t0=24.9, kind='inv', text=' $0 APP ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=24.95, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=26.2, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=26.6, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=26.6, kind='cursor', x=760, y=820, size=132),
    dict(t0=28.8, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
