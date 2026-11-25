# 019 VibeOffice — free, open-source office suite in the browser (Microsoft Office / 365 alt)
# Official site vibeoffice.work (read 2026-11-25): "A free office suite that runs in your browser: a word processor,
#   a spreadsheet and a presentation editor for .docx, .xlsx and .pptx files." "Private by design. Everything runs on
#   this computer: nothing is uploaded, and there is no account to make." Ledger: "Spreadsheets with 519 functions".
# Repo github.com/tcchen2026/VibeOffice (Apache-2.0, 1.4k stars, latest release v2026.11.22): "Nothing to install,
#   no account, and your files never leave your computer." New: listed Oct 2026 on saasisdead.si/new under Microsoft 365.
# Footage: real guest sessions on vibeoffice.work (home, Quire typing, Ledger =SUM, Lectern sample deck) + GitHub repo. No login.
N = 19
DUR = 28.93
ROLLS = [2.1, 8.25, 9.8, 12.65, 17.65, 21.6]
STATUS = [(2.1, 'OFFICE APP'), (6.0, 'SEARCH'), (8.25, 'WORD'), (9.8, 'EXCEL'), (12.65, 'SLIDES'),
          (17.65, 'PRIVACY'), (21.6, 'LICENSE'), (23.45, 'EXIT 0')]
HOOK = dict(lines=[(0.0, 'STOP PAYING FOR')], inverse=(0.9, 'MS OFFICE'), until=2.1)
SEARCH = dict(domain='vibeoffice.work', t0=6.2, t1=7.45, until=8.25)
FIX = {'vibeoffice': 'vibeoffice', '.work.': '.work', 'Vibe': 'Vibe', 'nopay': 'nopay', '519': '519'}
WINDOWS = [
    (2.1, 4.3, 'fr_home', 3.0, 5.2, ' vibeoffice.work '),
    (4.3, 6.0, 'fr_home', 6.0, 7.7, ' vibeoffice.work '),
    (6.0, 8.25, 'gs', 0, 0, ' google.com '),
    (8.25, 9.8, 'fr_doc', 7.5, 10.6, ' vibeoffice.work / quire '),
    (9.8, 12.65, 'fr_xl', 8.8, 12.6, ' vibeoffice.work / ledger '),
    (12.65, 13.95, 'fr_lectern', 15.8, 18.4, ' vibeoffice.work / lectern '),
    (13.95, 17.65, 'fr_lectern', 18.4, 23.0, ' vibeoffice.work / lectern '),
    (17.65, 21.6, 'fr_home', 9.0, 13.0, ' vibeoffice.work '),
    (21.6, 23.45, 'fr_repo', 16.4, 18.4, ' github.com / VibeOffice '),
]
LABELS = [
    dict(t0=2.2, t1=4.3, kind='inv', text=' IN YOUR BROWSER ', x=40, y=110, size=64),
    dict(t0=3.6, t1=4.3, kind='inv', text=' $0 ', x=40, y=992, size=72, hit=True),
    dict(t0=4.5, t1=6.0, kind='inv', text=' VIBEOFFICE ', x=40, y=110, size=72, hit=True),
    dict(t0=4.9, t1=6.0, kind='type', text='> word + excel + slides', x=40, y=210, size=56),
    dict(t0=8.3, t1=9.8, kind='inv', text=' WORD ', x=40, y=110, size=64),
    dict(t0=8.6, t1=9.8, kind='type', text='> type, bold, tables', x=40, y=210, size=56),
    dict(t0=9.9, t1=12.65, kind='inv', text=' EXCEL ', x=40, y=110, size=64),
    dict(t0=10.6, t1=12.65, kind='type', text='> 519 functions', x=40, y=210, size=56),
    dict(t0=11.6, t1=12.65, kind='inv', text=' =SUM() WORKS ', x=40, y=992, size=60, hit=True),
    dict(t0=12.7, t1=13.95, kind='inv', text=' SLIDES ', x=40, y=110, size=64),
    dict(t0=14.0, t1=17.65, kind='inv', text=' OPENS + SAVES ', x=40, y=110, size=64),
    dict(t0=15.1, t1=17.65, kind='type', text='> .docx', x=40, y=210, size=56),
    dict(t0=15.7, t1=17.65, kind='type', text='> .xlsx', x=270, y=210, size=56),
    dict(t0=16.2, t1=17.65, kind='type', text='> .pptx', x=500, y=210, size=56),
    dict(t0=17.7, t1=21.6, kind='type', text='> no install', x=40, y=110, size=56),
    dict(t0=18.7, t1=21.6, kind='type', text='> no account', x=40, y=200, size=56),
    dict(t0=19.9, t1=21.6, kind='inv', text=' FILES STAY ON YOUR PC ', x=40, y=992, size=60, hit=True),
    dict(t0=21.7, t1=23.45, kind='inv', text=' FREE ', x=40, y=110, size=72, hit=True),
    dict(t0=22.2, t1=23.45, kind='inv', text=' OPEN SOURCE ', x=250, y=110, size=64),
    dict(t0=22.6, t1=23.45, kind='type', text='> Apache-2.0', x=40, y=210, size=56),
    dict(t0=23.47, kind='text', text='FREE OFFICE ALT', x=480, y=200, size=76, anchor='ma'),
    dict(t0=23.47, kind='inv', text=' $0 ', x=480, y=340, size=140, anchor='ma'),
    dict(t0=23.55, kind='type', text='> save this reel', x=40, y=620, size=66),
    dict(t0=24.26, kind='type', text='> follow', x=40, y=710, size=66),
    dict(t0=24.56, kind='text', text='nopay.exe', x=480, y=820, size=132, anchor='ma', hit=True),
    dict(t0=24.56, kind='cursor', x=760, y=820, size=132),
    dict(t0=25.9, kind='type', text='for more free AI', x=480, y=990, size=72, anchor='ma', end=True),
]
