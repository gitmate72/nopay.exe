# 018 Doory — free, open-source design editor in the browser (Canva alt)
# Official site doory.art (read 2026-11-21): "Free, and no sign-up to start." "No watermark / No ads / Open source".
#   FAQ "Is Doory really free?": "Yes. There are no plans, no paywalls and no ads. Every feature you see is available to everyone."
#   FAQ "Can I download my designs?": "Yes. Export as PNG, JPG, SVG or PDF. ... works for guests too." Share menu also offers Video (MP4 / GIF).
# Repo github.com/shaongitbd/doory (2.8k stars, Attribution Assurance License, v0.3.1 Nov 9 2026). New: listed Oct 2026 on
#   saasisdead.si/new under Canva. README: "young project ... ten starter templates".
# Footage: real guest session on doory.art (template page -> Use this template -> edit text -> panels -> Share menu), no login.
N = 18
DUR = 29.43
ROLLS = [9.6, 12.5, 14.2, 18.5, 24.2]
STATUS = [(1.5, 'DESIGN APP'), (7.6, 'SEARCH'), (9.6, 'TEMPLATE'), (12.5, 'STICKERS'), (14.2, 'EXPORT'),
          (18.5, 'PRICE CHECK'), (24.2, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.86, 'CANVA'), until=1.5)
SEARCH = dict(domain='doory.art', t0=7.8, t1=8.9, until=9.6)
FIX = {'Dory.': 'Doory.', 'Dory': 'Doory', '.art.': '.art', 'nopay': 'nopay'}
WINDOWS = [
    (1.5, 5.0, 'fr_home', 14.2, 17.6, ' doory.art '),
    (5.0, 7.6, 'fr_home', 4.0, 6.6, ' doory.art '),
    (7.6, 9.6, 'gs', 0, 0, ' google.com '),
    (9.6, 10.4, 'fr_editor', 5.2, 6.8, ' doory.art / templates '),
    (10.4, 12.5, 'fr_editor', 14.4, 17.9, ' doory.art / editor '),
    (12.5, 13.4, 'fr_editor', 26.8, 28.6, ' doory.art / editor '),
    (13.4, 14.2, 'fr_editor', 29.3, 31.0, ' doory.art / editor '),
    (14.2, 18.5, 'fr_editor', 32.6, 36.5, ' doory.art / editor '),
    (18.5, 22.6, 'fr_faqfree', 6.6, 10.9, ' doory.art / faq '),
    (22.6, 24.2, 'fr_home', 20.0, 22.0, ' doory.art '),
]
LABELS = [
    dict(t0=1.6, t1=5.0, kind='inv', text=' POSTS ', x=40, y=110, size=64),
    dict(t0=2.3, t1=5.0, kind='inv', text=' POSTERS ', x=270, y=110, size=64),
    dict(t0=2.9, t1=5.0, kind='inv', text=' VIDEOS ', x=560, y=110, size=64),
    dict(t0=4.2, t1=5.0, kind='type', text='> no sign-up', x=40, y=210, size=56),
    dict(t0=5.6, t1=7.6, kind='type', text='> free + open source', x=40, y=210, size=56),
    dict(t0=6.6, t1=7.6, kind='inv', text=' DOORY ', x=40, y=110, size=72, hit=True),
    dict(t0=9.7, t1=12.5, kind='inv', text=' PICK A TEMPLATE ', x=40, y=110, size=64),
    dict(t0=10.5, t1=12.5, kind='type', text='> click any text', x=40, y=210, size=56),
    dict(t0=11.6, t1=12.5, kind='inv', text=' MAKE IT YOURS ', x=40, y=992, size=60, hit=True),
    dict(t0=12.6, t1=14.2, kind='inv', text=' STICKERS ', x=40, y=110, size=64),
    dict(t0=13.4, t1=14.2, kind='inv', text=' ANIMATIONS ', x=340, y=110, size=64),
    dict(t0=14.3, t1=18.5, kind='inv', text=' EXPORT ', x=40, y=110, size=64),
    dict(t0=14.9, t1=18.5, kind='type', text='> PNG', x=40, y=210, size=56),
    dict(t0=15.7, t1=18.5, kind='type', text='> PDF', x=230, y=210, size=56),
    dict(t0=16.4, t1=18.5, kind='type', text='> SVG', x=420, y=210, size=56),
    dict(t0=17.8, t1=18.5, kind='inv', text=' + VIDEO ', x=40, y=992, size=60, hit=True),
    dict(t0=18.6, t1=24.2, kind='inv', text=' $0 ', x=40, y=110, size=72, hit=True),
    dict(t0=19.9, t1=24.2, kind='inv', text=' NO PLANS ', x=200, y=110, size=64),
    dict(t0=20.8, t1=24.2, kind='type', text='> no paywalls', x=40, y=210, size=56),
    dict(t0=21.8, t1=22.6, kind='type', text='> no ads', x=470, y=210, size=56),
    dict(t0=22.8, t1=24.2, kind='inv', text=' NO WATERMARK ', x=40, y=992, size=60, hit=True),
    dict(t0=24.22, kind='text', text='FREE CANVA ALT', x=480, y=200, size=76, anchor='ma'),
    dict(t0=24.22, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=24.3, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=25.06, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=25.32, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=25.32, kind='cursor', x=760, y=820, size=132),
    dict(t0=26.6, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
