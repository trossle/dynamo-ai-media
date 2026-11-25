import json,re,numpy as np,soundfile as sf,subprocess
from scipy.signal import resample_poly
vo=json.load(open("vo.json"))
gap=[0,0.3,0.3,0.3,0.3,0.45,0.4,0.35]
starts=[];t=0.25
for i,v in enumerate(vo):
    t+=gap[i]; starts.append(round(t,3)); t+=v["dur"]
END=round(starts[-1]+vo[-1]["dur"]+2.6,2)
words=[]
for i,v in enumerate(vo):
    for w in v["words"]: words.append({"d":w["d"],"t":round(starts[i]+w["t"],3),"l":i})
def wt(line,sub):
    for w in words:
        if w["l"]==line and sub.lower() in w["d"].lower(): return w["t"]
    raise Exception(sub)
HL={"undertaker","machine…","customers.","1880s,","strowger","operator.","wife","husband","machine","1892,","automatic","lost.","busy","lunch","closed","dynamo","ai","first","ring,","24×7.","free,","10"}
chunks=[];cur=[]
for n,w in enumerate(words):
    cur.append(w)
    nxt=words[n+1] if n+1<len(words) else None
    if re.search(r'[,.?…]$',w["d"]) or len(cur)>=3 or (nxt and nxt["l"]!=w["l"]):
        chunks.append(cur);cur=[]
if cur: chunks.append(cur)
caps=[]
for k,c in enumerate(chunks):
    a=c[0]["t"]; b=chunks[k+1][0]["t"] if k+1<len(chunks) else starts[-1]+vo[-1]["dur"]+0.3
    lineend=starts[c[-1]["l"]]+vo[c[-1]["l"]]["dur"]+0.25
    b=min(b,lineend) if (k+1<len(chunks) and chunks[k+1][0]["l"]!=c[-1]["l"]) else b
    html=" ".join(f'<span class="y">{w["d"]}</span>' if w["d"].lower() in HL else w["d"] for w in c)
    caps.append([html,round(a-0.03,3),round(b,3)])
S={"A":0,"B":starts[1],"C":starts[2],"D":starts[3],"E":starts[4],"F":starts[5],"G":starts[6],"I":starts[7],"END":END}
K={"under":wt(0,"undertaker"),"machine":wt(0,"machine"),"cust":wt(0,"customers."),
   "yrs":wt(1,"1880s,"),"almon":wt(1,"Almon"),"funeral":wt(1,"funeral"),"kc":wt(1,"Kansas"),
   "story":wt(2,"story"),"wife":wt(2,"wife"),"oper":wt(2,"operator."),
   "asked":wt(3,"asked"),"through":wt(3,"through"),"husb":wt(3,"husband"),
   "built":wt(4,"built"),"cut":wt(4,"cut"),"yr2":wt(4,"1892,"),"auto":wt(4,"automatic"),
   "today":wt(5,"Today,"),"lost":wt(5,"lost."),"busy":wt(5,"busy"),"lunch":wt(5,"lunch"),"closed":wt(5,"closed"),
   "dyn":wt(6,"Dynamo"),"ring":wt(6,"first"),"247":wt(6,"24×7."),"hindi":wt(6,"Hindi,"),"eng":wt(6,"English,"),"reg":wt(6,"regional")}
PUNCH=[K["cust"],K["yrs"],K["oper"],K["husb"],K["yr2"],K["lost"],K["dyn"],K["ring"]]
# VO track
SR2=44100; N2=int(END*SR2); vtrack=np.zeros(N2)
for i in range(len(vo)):
    a,sr=sf.read(f"raw{i}.wav"); a=resample_poly(a,147,80); s=int(starts[i]*SR2); vtrack[s:s+len(a)]+=a[:N2-s]
vtrack/=np.max(np.abs(vtrack))/0.7
sf.write("vo_dry.wav",vtrack,SR2)
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","vo_dry.wav","-af","highpass=f=75,equalizer=f=160:t=q:w=1:g=3,equalizer=f=3200:t=q:w=1.2:g=2.5,acompressor=threshold=-20dB:ratio=3:attack=4:release=90:makeup=2,aecho=0.85:0.5:22|41:0.10|0.06,alimiter=limit=0.9","vo.wav"],check=True)
# amplitude of VO per frame for ducking
v,_=sf.read("vo.wav")
if v.ndim>1: v=v.mean(1)
env=np.array([np.sqrt(np.mean(v[int(f/30*SR2):int((f+1)/30*SR2)]**2)) for f in range(int(END*30))])
json.dump({"S":S,"K":K,"caps":caps,"punch":PUNCH,"starts":starts,"END":END},open("timeline.json","w"),ensure_ascii=False)
np.save("voenv.npy",env)
print("END",END); print({k:round(x,2) for k,x in S.items()}); print(len(caps),"caps")
for c in caps[:6]: print(c)
