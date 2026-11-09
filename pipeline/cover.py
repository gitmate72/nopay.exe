import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
# usage: cover.py <frame.jpg> <out.jpg> <num> <BRAND> <domain> <BADGE> <line1> <line2>
src, out, NUM, BRAND, DOMAIN, BADGE, L1, L2 = sys.argv[1:9]
F='/home/claude/nopay.exe/pipeline/engine/fonts/'
W,H=1080,1920; G=(57,255,110); D=(4,14,8)
img=Image.new('RGB',(W,H),D); d=ImageDraw.Draw(img)
vt=lambda s: ImageFont.truetype(F+'VT323.ttf',s)
def ctext(y,t,s,fill=G,inv=False,pad=18):
    f=vt(s); w=d.textlength(t,font=f); x=(W-w)/2
    if inv:
        bb=d.textbbox((x,y),t,font=f); d.rectangle((bb[0]-pad,bb[1]-pad//2,bb[2]+pad,bb[3]+pad//2),fill=G); d.text((x,y),t,font=f,fill=D)
    else: d.text((x,y),t,font=f,fill=fill)
    return d.textbbox((x,y),t,font=f)
# top bar (outside grid crop, decorative)
d.rectangle((40,60,W-40,120),fill=G); d.text((60,62),f'nopay.exe #{NUM}',font=vt(52),fill=D); 
f=vt(52); d.text((W-60-d.textlength('FREE AI',font=f),62),'FREE AI',font=f,fill=D)
# headline (inside 3:4 grid crop y 240..1680)
ctext(300,'STOP PAYING FOR',96)
bb=ctext(410,BRAND,190 if len(BRAND)<=10 else int(1900/len(BRAND)))
d.line((bb[0]-20,(bb[1]+bb[3])//2+8,bb[2]+20,(bb[1]+bb[3])//2+8),fill=(255,70,70),width=16)
# real screenshot window, original colours
shot=Image.open(src).convert('RGB'); sw=960; sh=int(shot.height*sw/shot.width); shot=shot.resize((sw,sh))
y0=660; d.rectangle((60-6,y0-50,60+sw+6,y0+sh+6),outline=G,width=4); d.rectangle((60-6,y0-50,60+sw+6,y0),fill=G)
d.text((76,y0-50),f' {DOMAIN} ',font=vt(46),fill=D)
img.paste(shot,(60,y0))
yb=y0+sh+60
ctext(yb,f' {BADGE} ',120,inv=True,pad=24)
ctext(yb+170,L1,64)
ctext(yb+240,L2,64)
# CRT: scanlines + glow + vignette
a=np.asarray(img).astype(np.float32)
glow=np.asarray(img.filter(ImageFilter.GaussianBlur(10))).astype(np.float32)
a=np.clip(a+0.45*glow,0,255)
a[1::3]*=0.78
yy,xx=np.mgrid[0:H,0:W]; v=1-0.35*(((xx-W/2)/(W/2))**2+((yy-H/2)/(H/2))**2)
a*=np.clip(v,0.5,1)[...,None]
Image.fromarray(a.astype(np.uint8)).save(out,quality=92)
