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
# vinyl-style crackle under the 1876 scenes
L=S["F"];n=int(L*SR);cr=np.zeros(n);idx=rng.integers(0,n,int(L*60));cr[idx]=rng.standard_normal(len(idx))*0.8
add(sfx,np.convolve(cr,np.ones(3)/3,'same')+noise(L,200)*0.15,0,0.25)
# A: whoosh slide + hay thump
add(sfx,noise(1.5,20)*np.sin(np.linspace(0,np.pi,int(1.5*SR)))**2,0.0,0.12)
boom(K["hay"],0.4)
boom(K["yrs"],0.35)
# horses snort / hooves in the firehouse
for q in range(4): add(sfx,noise(0.05,3)*np.exp(-np.arange(int(0.05*SR))/SR/0.01),K["horses"]+q*0.18,0.10)
# C: alarm bell clanging
st=K["alarm"]
while st<S["D"]-0.1:
    add(sfx,tone(1760,0.5,0.25,((1,1),(2.76,.5),(5.4,.25))),st,0.07);st+=0.18
# D: stairs cross, slide whoosh, landing thud
add(sfx,np.sign(np.sin(2*np.pi*110*np.arange(int(0.3*SR))/SR))*np.exp(-np.arange(int(0.3*SR))/SR/0.12),K["stairs"],0.05)
L=K["down"]+0.3-K["slid"];n=int(L*SR);add(sfx,noise(L,8)*np.linspace(0.3,1,n),K["slid"],0.18)
boom(K["down"]+0.25,0.55)
# E: pole installed clank, stamp
add(sfx,tone(nf(57),0.8,0.3,((1,1),(2.3,.5),(4.1,.3))),K["perm"],0.10)
boom(K["first4"],0.55);add(sfx,noise(0.2,3)*np.exp(-np.arange(int(0.2*SR))/SR/0.05),K["first4"],0.25)
# F: three phones ring, one answered
st=K["calls"]
while st<K["every"]+0.6:
    for q in range(6): add(sfx,tone(1320 if q%2==0 else 1046.5,0.07,0.03),st+q*0.07,0.05)
    st+=1.2
add(sfx,tone(nf(76),0.4,0.15),K["firstA"],0.09);add(sfx,tone(nf(83),0.6,0.2),K["firstA"]+0.1,0.09)
# G
boom(K["dyn"],0.6)
for f in [880,1108.7,1318.5,1760,2217.5]: add(sfx,tone(f,2.5,1.2),K["dyn"],0.035)
add(sfx,tone(nf(76),0.5,0.2),K["ring"],0.09);add(sfx,tone(nf(83),0.7,0.25),K["ring"]+0.12,0.09)
for k2,m2 in [("247",79),("hindi",76),("eng",79),("reg",83)]: add(sfx,tone(nf(m2),0.4,0.12),K[k2],0.07)
for i in range(5): add(sfx,tone(nf(76+i*2),0.4,0.12),S["I"]+0.25+i*0.35,0.045)
bed=mus+sfx;bed*=np.clip((D-t)/1.0,0,1)
vo,_=sf.read("vo.wav")
if vo.ndim>1: vo=vo.mean(1)
vo=np.pad(vo,(0,max(0,N-len(vo))))[:N]
mix=vo*1.0+np.tanh(bed*1.1)*0.55
mix/=np.max(np.abs(mix))/0.92
sf.write("mix.wav",np.stack([mix,mix],1),SR);print("ok",D)
