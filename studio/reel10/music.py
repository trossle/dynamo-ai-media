import json,numpy as np,soundfile as sf
TL=json.load(open("timeline.json"));S=TL["S"];K=TL["K"];D=TL["END"]
SR=44100;N=int(D*SR);t=np.arange(N)/SR;mus=np.zeros(N);sfx=np.zeros(N);rng=np.random.default_rng(8)
def add(buf,s,st,g=1.0):
    i=int(st*SR);j=min(N,i+len(s))
    if 0<=i<N: buf[i:j]+=s[:j-i]*g
def env(L,a,d): n=int(L*SR);tt=np.arange(n)/SR;return np.clip(tt/max(a,1e-4),0,1)*np.exp(-tt/d),tt
def tone(f,L,d,parts=((1,1),)): e,tt=env(L,0.002,d);return sum(g*np.sin(2*np.pi*f*k*tt) for k,g in parts)*e
def noise(L,sm=1): n=int(L*SR);x=rng.standard_normal(n);return np.convolve(x,np.ones(sm)/sm,'same') if sm>1 else x
nf=lambda m:440*2**((m-69)/12)
G=S["F"]
# part 1 music
B=0.5
for k in range(int(G/B)):
    s0=k*B
    add(mus,tone(2400 if k%2==0 else 1800,0.04,0.008),s0,0.10)
    add(mus,tone(nf(45 if (k//8)%2==0 else 41),0.5,0.18,((1,1),(2,.3))),s0,0.30 if k%2==0 else 0.13)
arp=[57,60,64,69,64,60,64,67];arp2=[53,57,60,65,60,57,60,64]
for k in range(int(G/0.25)):
    m=(arp if (k//16)%2==0 else arp2)[k%8]; add(mus,tone(nf(m+12),0.3,0.07,((1,1),(2,.25))),k*0.25,0.09)
# tape stop
n=int(0.45*SR);tt=np.arange(n)/SR;f=nf(69)*(1-tt/0.5);add(sfx,np.sin(2*np.pi*np.cumsum(f)/SR)*np.clip((0.45-tt)/0.05,0,1),G-0.1,0.16)
# part 2 warm
ch=[[48,52,55,60],[53,57,60,65],[55,59,62,67],[57,60,64,69]]
k=0;s0=G+0.25
while s0<S["I"]:
    L=2.2;n=int(L*SR);tt=np.arange(n)/SR;e=np.clip(tt/0.3,0,1)*np.clip((L-tt)/0.4,0,1);c=ch[k%4]
    add(mus,sum(np.sin(2*np.pi*nf(m)*tt)*0.2 for m in c)*e,s0,0.28);add(mus,np.sin(2*np.pi*nf(c[0]-12)*tt)*e,s0,0.16)
    for b in range(4):
        if s0+b*0.5<S["I"]: add(mus,tone(55,0.3,0.1),s0+b*0.5,0.35 if b%2==0 else 0.15)
    s0+=1.9;k+=1
# end pad
L=D-S["I"];n=int(L*SR);tt=np.arange(n)/SR;e=np.clip(tt/0.6,0,1)*np.clip((L-tt)/1.4,0,1)
add(mus,sum(np.sin(2*np.pi*nf(m)*tt)*g for m,g in [(45,.3),(57,.25),(64,.18),(69,.14),(73,.1)])*e,S["I"],0.25)
# duck music under VO
venv=np.load("voenv.npy");venv=venv/venv.max()
fr=np.clip((t*30).astype(int),0,len(venv)-1);ve=np.convolve(venv,np.ones(6)/6,'same')[fr]
mus*=1-0.62*np.clip(ve*2.5,0,1)
# sfx
def whoosh(st,L=0.4,g=0.5):
    n=int(L*SR);add(sfx,noise(L,30)*np.sin(np.linspace(0,np.pi,n))**2,st-L*0.6,g)
def boom(st,g=0.6): add(sfx,tone(50,1.0,0.3),st,g);add(sfx,tone(100,0.4,0.1),st,g*0.3)
for k2 in ["B","C","D","E","F","G","I"]: whoosh(S[k2]);boom(S[k2],0.35)
for p in TL["punch"]: boom(p,0.45); add(sfx,noise(0.12,2)*np.exp(-np.arange(int(0.12*SR))/SR/0.03),p,0.12)
for c in TL["caps"]: add(sfx,tone(1500,0.05,0.012),c[1],0.03)
# A: ocean + foghorn
def waves(st,L,g):
    n=int(L*SR);tt=np.arange(n)/SR;add(sfx,noise(L,120)*1.6*(0.6+0.4*np.sin(2*np.pi*0.18*tt))*np.clip(tt/0.4,0,1)*np.clip((L-tt)/0.3,0,1),st,g)
waves(0,S["B"],0.30)
add(sfx,tone(110,1.6,0.9,((1,1),(2,.5),(3,.3),(4,.15)))*np.clip(np.arange(int(1.6*SR))/SR/0.15,0,1),K["house"]-0.1,0.16)
# B: wind gust while the flame nearly goes out, whoosh when it recovers
L=K["out"]-K["never"]+0.3;n=int(L*SR);tt=np.arange(n)/SR;add(sfx,noise(L,40)*np.sin(np.pi*tt/L)**2*1.5,K["never"],0.30)
add(sfx,noise(0.5,15)*np.exp(-np.arange(int(0.5*SR))/SR/0.12),K["out"],0.22)
# C: footsteps up the stairs, clock ticks, gear ratchet
k3=0
while S["C"]+0.3+k3*0.33<K["clock"]-0.2:
    add(sfx,noise(0.06,4)*np.exp(-np.arange(int(0.06*SR))/SR/0.015),S["C"]+0.3+k3*0.33,0.16);k3+=1
for k3 in range(int((S["D"]-S["C"])/0.5)): add(sfx,tone(3000,0.03,0.006),S["C"]+k3*0.5,0.05)
for k3 in range(10): add(sfx,tone(1800,0.03,0.008,((1,1),(1.7,.5))),K["clock"]+k3*0.09,0.06)
# D: snip + stamp
add(sfx,noise(0.05,1)*np.exp(-np.arange(int(0.05*SR))/SR/0.01),K["wicks"],0.30);add(sfx,tone(4200,0.08,0.02),K["wicks"],0.08)
boom(K["wickies"],0.55);add(sfx,noise(0.2,3)*np.exp(-np.arange(int(0.2*SR))/SR/0.05),K["wickies"],0.25)
# E: waves, low drone when the light goes dark, warning bell at the ship
waves(S["E"],S["F"]-S["E"],0.26)
L=K["ship"]+0.6-K["dark"];n=int(L*SR);tt=np.arange(n)/SR;add(sfx,np.sin(2*np.pi*55*tt)*np.clip(tt/0.3,0,1)*np.clip((L-tt)/0.3,0,1),K["dark"],0.22)
for k3 in range(2): add(sfx,tone(1046.5,1.4,0.5,((1,1),(2.4,.4),(3.9,.2))),K["ship"]+k3*0.45,0.09)
# F: ringtone until it rings out, then a sad two-note drop
st=S["F"]+0.2
while st<K["rings"]-0.2:
    for q in range(8): add(sfx,tone(1320 if q%2==0 else 1046.5,0.07,0.03),st+q*0.07,0.07)
    st+=1.4
add(sfx,tone(nf(64),0.4,0.15),K["rings"],0.09);add(sfx,tone(nf(59),0.6,0.2),K["rings"]+0.22,0.09)
waves(K["sail"]-0.5,S["G"]-K["sail"]+0.5,0.20)
# G: logo shimmer, pick-up chime, chip pops
boom(K["dyn"],0.6)
for f in [880,1108.7,1318.5,1760,2217.5]: add(sfx,tone(f,2.5,1.2),K["dyn"],0.035)
add(sfx,tone(nf(76),0.5,0.2),K["first"],0.09);add(sfx,tone(nf(83),0.7,0.25),K["first"]+0.12,0.09)
for k2,m2 in [("247",79),("hindi",76),("eng",79),("reg",83)]: add(sfx,tone(nf(m2),0.4,0.12),K[k2],0.07)
for i in range(5): add(sfx,tone(nf(76+i*2),0.4,0.12),S["I"]+0.25+i*0.35,0.045)
bed=mus+sfx;bed*=np.clip((D-t)/1.0,0,1)
vo,_=sf.read("vo.wav")
if vo.ndim>1: vo=vo.mean(1)
vo=np.pad(vo,(0,max(0,N-len(vo))))[:N]
mix=vo*1.0+np.tanh(bed*1.1)*0.55
mix/=np.max(np.abs(mix))/0.92
sf.write("mix.wav",np.stack([mix,mix],1),SR);print("ok",D)
