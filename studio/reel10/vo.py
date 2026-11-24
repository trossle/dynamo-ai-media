import json, re, numpy as np, soundfile as sf, subprocess
from kokoro_onnx import Kokoro
k=Kokoro("/home/claude/reel5/models/kokoro-v1.0.fp16.onnx","/home/claude/reel5/models/voices-v1.0.bin")
V="am_michael"; SP=1.08
LINES=[
 "For centuries, someone stayed awake all night, at the top of every lighthouse.",
 "The lighthouse keeper. Their one job: never let the light go out.",
 "Every few hours, they climbed the tower, to wind the clockwork that kept the lens turning.",
 "They trimmed the wicks so often, sailors called them wickies.",
 "From sunset to sunrise, the light stayed on. Because one dark night could mean one missed ship.",
 "Your business has ships passing too. Every call that rings out is a customer sailing past.",
 "Dynamo AI keeps your line on, 24×7.|twenty-four-seven. It answers on the first ring, in Hindi, English, and regional languages.",
 "Try it free, for 10|ten minutes.",
]
out=[]
for i,L in enumerate(LINES):
    toks=[]
    for w in L.split():
        d,s=(w.split("|")+[None])[:2]; s=s or d; toks.append((d,s.replace("-"," ")))
    spoken=" ".join(s for _,s in toks).replace("…",",")
    a,sr=k.create(spoken,voice=V,speed=SP,lang="en-us"); a=np.asarray(a,dtype=np.float32)
    ab=np.abs(a); thr=0.02*ab.max(); idx=np.where(ab>thr)[0]; a=a[max(0,idx[0]-int(0.02*sr)):idx[-1]+int(0.06*sr)]
    sf.write(f"raw{i}.wav",a,sr)
    # gaps
    hop=int(0.01*sr); e=np.array([np.sqrt(np.mean(a[j:j+hop]**2)) for j in range(0,len(a)-hop,hop)]); th=0.06*e.max()
    sil=e<th; gaps=[]; j=0
    while j<len(sil):
        if sil[j]:
            k2=j
            while k2<len(sil) and sil[k2]: k2+=1
            if j>5 and k2<len(sil)-3 and (k2-j)>=11: gaps.append((j*0.01,k2*0.01))
            j=k2
        else: j+=1
    dur=len(a)/sr
    bidx=[n for n,(d,s) in enumerate(toks[:-1]) if re.search(r'[,.?…]$',d)]
    # phrases
    bounds=[]
    if len(gaps)>=len(bidx) and bidx:
        g=sorted(sorted(gaps,key=lambda x:x[1]-x[0],reverse=True)[:len(bidx)])
        spans=[]; st=0.0
        for (gs,ge) in g: spans.append((st,gs)); st=ge
        spans.append((st,dur-0.04))
    else:
        spans=None
    phr=[]; cur=[]
    for n,tk in enumerate(toks):
        cur.append(tk)
        if n in bidx: phr.append(cur); cur=[]
    phr.append(cur)
    if spans and len(spans)==len(phr):
        for p,(a0,a1) in zip(phr,spans):
            if (a1-a0) < 0.045*sum(len(x) for _,x in p): spans=None; break
    if not spans or len(spans)!=len(phr):
        tot=sum(len(s)+2 for p in phr for _,s in p); spans=[]; st=0.02
        for p in phr:
            w=sum(len(s)+2 for _,s in p)/tot*(dur-0.06); spans.append((st,st+w)); st+=w
    words=[]
    for p,(a0,a1) in zip(phr,spans):
        tot=sum(len(s.replace(" ",""))+1.5 for _,s in p); t=a0
        for d,s in p:
            words.append({"d":d,"t":round(t,3)}); t+=(a1-a0)*(len(s.replace(" ",""))+1.5)/tot
    out.append({"i":i,"dur":dur,"words":words,"gaps":len(gaps),"bounds":len(bidx)})
    print(i,round(dur,2),"gaps",len(gaps),"bounds",len(bidx))
json.dump(out,open("vo.json","w"),ensure_ascii=False,indent=1)
