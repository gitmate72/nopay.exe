import numpy as np,wave
from scipy.signal import butter,sosfilt,square
SR=48000;D=32.4;N=int(SR*D);out=np.zeros(N);rng=np.random.default_rng(11)
def add(sig,t,g=1.0):
    i=int(max(0,t)*SR);n=min(len(sig),N-i)
    if n>0: out[i:i+n]+=sig[:n]*g
def bp(x,lo,hi):return sosfilt(butter(2,[lo,hi],'band',fs=SR,output='sos'),x)
T=lambda d:np.arange(int(d*SR))/SR
def key():tt=T(0.035);return bp(rng.normal(0,1,len(tt)),1800+rng.uniform(-400,400),7000)*np.exp(-tt*140)*0.8+np.sin(2*np.pi*2400*tt)*np.exp(-tt*300)*0.15
def beep(f=1200,d=0.09):tt=T(d);return square(2*np.pi*f*tt)*0.25*np.minimum(1,(d-tt)/0.01)*np.minimum(1,tt/0.003)
def hit(f=110):
    tt=T(0.9);return (square(2*np.pi*f*tt)*0.25+np.sin(2*np.pi*f/2*tt)*0.6)*np.exp(-tt*4)+bp(rng.normal(0,1,len(tt)),200,4000)*np.exp(-tt*30)*0.5
def roll():
    tt=T(0.42);st=bp(rng.normal(0,1,len(tt)),400,6000)*np.sin(np.pi*tt/0.42)*0.5
    return st+np.sin(2*np.pi*(180-120*tt/0.42)*tt)*np.sin(np.pi*tt/0.42)*0.35
def thunk():tt=T(0.8);return np.sin(2*np.pi*(50+30*np.exp(-tt*8))*tt)*np.exp(-tt*5)*0.9+bp(rng.normal(0,1,len(tt)),60,1200)*np.exp(-tt*20)*0.6
def chime():
    x=np.zeros(int(1.6*SR))
    for i,f in enumerate([523,659,784,1047]):
        s=int(i*0.09*SR);tt=np.arange(len(x)-s)/SR;x[s:]+=square(2*np.pi*f*tt)*0.12*np.exp(-tt*3)
    return x
def tick():tt=T(0.02);return square(2*np.pi*2000*tt)*0.18*np.exp(-tt*150)
def buzz():tt=T(0.16);return square(2*np.pi*140*tt)*0.18*np.exp(-tt*8)
# ambience: mains hum + faint flyback whine
tt=np.arange(N)/SR
bed=(np.sin(2*np.pi*60*tt)*0.5+np.sin(2*np.pi*120*tt)*0.25)*0.05+np.sin(2*np.pi*11500*tt)*0.004
bed[:int(0.24*SR)]*=np.linspace(0,1,int(0.24*SR))
out+=bed
add(thunk(),0.0,1.0)
for t0,n,cps in [(1.61,20,26),(1.99,17,30),(4.7,4,16),(5.86,7,1/0.11),(7.73,23,30),(13.96,22,34),(15.99,17,32),(24.49,17,34),(26.96,16,34),(28.18,8,30),(29.88,16,30)]:
    for i in range(n):
        if i%2==0 or cps<25: add(key(),t0+i/cps,0.55)
for t,f in [(3.26,1200),(6.9,1300),(11.46,900),(12.58,1050),(15.04,1200),(17.56,1100),(22.47,1300),(26.16,1500),(28.49,1500)]: add(beep(f),t,0.8)
add(hit(110),0.86,0.7);add(hit(100),19.33,1.0)
for r in [4.42,15.62,26.86]: add(roll(),r-0.2,0.9)
for i in range(8): add(tick(),20.54+(21.48-20.54)*(1-(1-i/8)**0.7),0.7)
add(chime(),30.7,0.9)
out=out/np.abs(out).max()*0.9
w=wave.open(__import__('sys').argv[1] if len(__import__('sys').argv)>1 else 'fx.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
