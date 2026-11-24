import re
exec(open("/home/claude/reel11/_parts.py").read())
SEP = "#C9A46A"  # sepia ink
head = HEAD.replace("</style>", """
.paper{background:radial-gradient(ellipse at 50% 40%,#3A2A18,#140E08 72%)}
.hand{font-family:'DejaVu Serif',Georgia,serif;font-style:italic}
.stamp{border:10px solid #3FE6F0;border-radius:24px;color:#3FE6F0;font-weight:900;letter-spacing:6px;text-align:center;background:rgba(5,11,22,.6)}
</style>""")

PHONE_1876 = f'''<svg width="420" height="560" viewBox="0 0 420 560">
<rect x="40" y="470" width="340" height="60" rx="12" fill="#6B4423"/><rect x="60" y="455" width="300" height="24" rx="8" fill="#8A5A30"/>
<rect x="196" y="230" width="28" height="235" fill="#B08850"/><rect x="150" y="380" width="120" height="70" rx="10" fill="#4A3A28"/>
<circle cx="210" cy="415" r="20" fill="#C9A46A"/><path d="M210 230 L120 70 Q210 30 300 70 Z" fill="#C9A46A"/><ellipse cx="210" cy="70" rx="92" ry="24" fill="#8A6A3A"/>
<ellipse cx="210" cy="70" rx="70" ry="16" fill="#2A1E12"/><path d="M380 500 Q420 400 400 300" fill="none" stroke="#C9A46A" stroke-width="6"/></svg>'''
MAN = '''<svg width="300" height="640" viewBox="0 0 300 640"><path d="M150 60 C118 60 100 88 104 118 C106 140 116 154 128 162 L120 200 C150 214 168 210 182 196 L176 160 C190 150 198 132 198 112 C200 82 182 60 150 60 Z" fill="#120C07"/>
<path d="M112 140 C112 200 130 228 150 232 C172 228 190 200 188 140 C178 176 122 176 112 140 Z" fill="#120C07"/>
<path d="M50 640 L66 300 C72 240 108 214 150 214 C192 214 228 240 234 300 L250 640 Z" fill="#120C07"/></svg>'''

def room(x, label):
    return (f'<div class="abs" style="left:{x}px;top:640px;width:420px;height:620px;border:8px solid {SEP};border-radius:16px;background:rgba(40,28,16,.5)"></div>'
            f'<div class="abs" style="left:{x}px;top:580px;width:420px;text-align:center;font-size:40px;font-weight:800;color:{SEP};letter-spacing:4px">{label}</div>')

words = ["Mr.", "Watson,", "come", "here.", "I", "want", "to", "see", "you."]
W = "".join(f'<span id="w{i+1}" style="display:inline-block;margin:0 14px;opacity:0">{w}{"”" if i == 8 else ""}</span>' for i, w in enumerate(words))

A = f'''<!-- A: nine words -->
<div id="sA" class="sc paper">
  <div id="aPh" class="abs" style="left:330px;top:640px">{PHONE_1876}</div>
  <div id="a9" class="big" style="top:250px;font-size:300px;color:{SEP};opacity:0">9</div>
  <div id="aW" class="big" style="top:550px;font-size:90px;letter-spacing:12px;color:#EDE3CC;opacity:0">WORDS</div>
</div>'''
B = f'''<!-- B: March 10, 1876 -->
<div id="sB" class="sc paper">
  <div id="cal" class="abs" style="left:300px;top:200px;width:480px;height:420px;border-radius:24px;background:#EDE3CC;color:#2A1E12;box-shadow:0 30px 70px rgba(0,0,0,.6);overflow:hidden;opacity:0">
    <div style="height:110px;background:#8A3A2A;color:#EDE3CC;font-size:64px;font-weight:900;letter-spacing:10px;display:flex;align-items:center;justify-content:center">MARCH</div>
    <div style="text-align:center;font-size:200px;font-weight:900;line-height:1.1">10</div>
    <div id="yr" style="text-align:center;font-size:56px;font-weight:800;margin-top:-20px">1876</div></div>
  <div id="bMan" class="abs" style="left:170px;top:760px;opacity:0">{MAN}</div>
  <div id="bPh" class="abs" style="left:480px;top:760px;transform:scale(.85);transform-origin:0 0">{PHONE_1876}</div>
  <div id="bWaves" class="abs" style="inset:0"></div>
  <div id="bBos" class="abs" style="left:0;right:0;top:650px;text-align:center;font-size:40px;font-weight:800;letter-spacing:8px;color:{SEP};opacity:0">BOSTON · BELL'S LAB</div>
</div>'''
C = f'''<!-- C: the nine words, written out -->
<div id="sC" class="sc" style="background:#E8DCC2">
  <div class="abs" style="inset:0;background:repeating-linear-gradient(#E8DCC2 0 86px,#B9C7D4 86px 89px)"></div>
  <div class="abs" style="left:150px;top:0;width:4px;height:1920px;background:#C86A5A"></div>
  <div class="abs hand" style="left:190px;top:200px;font-size:40px;color:#6B5A44">Notebook · March 10, 1876</div>
  <div class="abs hand" style="left:160px;right:60px;top:430px;font-size:110px;line-height:1.35;color:#1E2A3A;font-weight:700">“{W}</div>
  <div id="cCount" class="abs" style="right:70px;top:190px;padding:14px 28px;border-radius:999px;background:#1E2A3A;color:#EDE3CC;font-size:44px;font-weight:900">0 / 9</div>
</div>'''
D = f'''<!-- D: next room -->
<div id="sD" class="sc paper">
  {room(60, "BELL")}{room(600, "WATSON")}
  <div class="abs" style="left:150px;top:1000px;transform:scale(.62);transform-origin:0 0">{MAN}</div>
  <div id="dWat" class="abs" style="left:720px;top:1000px;transform-origin:0 0">{MAN}</div>
  <svg class="abs" style="left:0;top:0" width="1080" height="1920"><path d="M300 900 C420 760 660 760 780 900" fill="none" stroke="{SEP}" stroke-width="8" stroke-dasharray="4 14" stroke-linecap="round"/></svg>
  <div id="dPulse" class="abs" style="width:46px;height:46px;border-radius:50%;background:#3FE6F0;box-shadow:0 0 40px 14px rgba(63,230,240,.6);opacity:0"></div>
  <div id="dEar" class="abs" style="left:770px;top:880px;width:170px;height:170px;border-radius:50%;border:8px solid #3FE6F0;opacity:0"></div>
</div>'''
E = f'''<!-- E: answered -->
<div id="sE" class="sc" style="background:#E8DCC2">
  <div class="abs" style="inset:0;background:repeating-linear-gradient(#E8DCC2 0 86px,#B9C7D4 86px 89px)"></div>
  <div class="abs hand" style="left:120px;right:80px;top:330px;font-size:70px;line-height:1.3;color:#1E2A3A">“To my delight he came…”<div style="font-size:40px;color:#6B5A44;margin-top:14px">A. G. Bell, lab notebook</div></div>
  <div id="eSt" class="abs stamp" style="left:150px;right:150px;top:760px;padding:34px 10px;font-size:84px;background:rgba(232,220,194,.85);transform:rotate(-8deg);opacity:0">CALL #1<br>ANSWERED ✓</div>
</div>'''
F = f'''<!-- F: 150 years later -->
<div id="sF" class="sc" style="background:radial-gradient(ellipse at 50% 35%,#0E3550,#050B16 70%)">
  <div id="fYr" class="big" style="top:190px;font-size:230px"><span class="gtext" id="fYrN">1876</span></div>
  <div id="fLab" class="big" style="top:440px;font-size:56px;letter-spacing:6px;color:#9FB6CC;opacity:0">150 YEARS LATER</div>
  <div id="fPh" class="abs" style="left:300px;top:580px;width:480px;height:760px;border-radius:72px;background:#0A0F18;padding:16px;box-shadow:0 60px 120px rgba(0,0,0,.6),0 0 0 4px #1F3550;opacity:0">
    <div style="position:relative;width:100%;height:100%;border-radius:58px;overflow:hidden;background:linear-gradient(#13243A,#0B1626)">
      <div class="abs" style="left:0;right:0;top:120px;text-align:center;font-size:32px;font-weight:700;color:#9FB6CC">Incoming call…</div>
      <div class="abs" style="left:0;right:0;top:180px;text-align:center;font-size:52px;font-weight:900">New customer</div>
      <div id="fQ" class="abs" style="left:60px;right:60px;top:400px;padding:26px;border-radius:30px;border:4px dashed #3FE6F0;text-align:center;font-size:56px;font-weight:900;color:#3FE6F0;opacity:0">Answered?</div>
    </div></div>
  <div id="fRings" class="abs" style="inset:0"></div>
</div>'''

G2 = G.replace("Incoming call · 11:42 PM", "Incoming call · new customer")
I2 = I.replace("Never let a call go dark.", "Every call, answered.")
body = '<div id="stage" class="abs" style="inset:0">\n' + A + B + C + D + E + F + G2 + I2 + '</div>\n'

js_new = r'''
  if(inA){const n=seg(t,K.nine-0.1,K.nine+0.25);$('a9').style.opacity=n;$('a9').style.transform=`scale(${n>0?back(n):0})`;
    const w=seg(t,K.words-0.1,K.words+0.2);$('aW').style.opacity=w;$('aW').style.transform=`translateY(${(1-eo(w))*40}px)`;
    $('aPh').style.transform=`translateY(${Math.sin(t*1.5)*6}px) scale(${1+0.03*t/3})`;}
  if(inB){const c=seg(t,K.date-0.1,K.date+0.3);$('cal').style.opacity=c;$('cal').style.transform=`rotate(${(1-eo(c))*-12}deg) scale(${c>0?0.6+0.4*back(c):0.6})`;
    $('yr').style.color=t>=K.year?'#8A3A2A':'#2A1E12';$('bBos').style.opacity=seg(t,K.year,K.year+0.3);
    const m=seg(t,K.bell-0.1,K.bell+0.4);$('bMan').style.opacity=m;$('bMan').style.transform=`translateX(${(1-eo(m))*-120}px)`;
    let w='';if(t>K.inv-0.2){for(let k=0;k<3;k++){const q=((t-K.inv)*0.9+k/3)%1;w+=`<div class="abs" style="left:${700-q*260}px;top:${830-q*260}px;width:${80+q*520}px;height:${80+q*520}px;border-radius:50%;border:6px solid rgba(201,164,106,${(1-q)*0.6})"></div>`;}}$('bWaves').innerHTML=w;}
  if(inC){let n=0;for(let i=1;i<=9;i++){const p=seg(t,K['w'+i]-0.08,K['w'+i]+0.12);const e=$('w'+i);e.style.opacity=p;e.style.transform=`translateY(${(1-eo(p))*30}px)`;if(t>=K['w'+i]-0.05)n=i;}
    $('cCount').textContent=n+' / 9';$('cCount').style.background=n==9?'#0BB2E0':'#1E2A3A';}
  if(inD){const p=seg(t,K.room,K.heard);const a=p*Math.PI;const x=540-240*Math.cos(a),y=900-150*Math.sin(a)*1.1;
    $('dPulse').style.opacity=p>0&&p<1?1:0;$('dPulse').style.left=(x-23)+'px';$('dPulse').style.top=(y-23)+'px';
    const h=seg(t,K.heard,K.heard+0.25);$('dEar').style.opacity=h*(1-seg(t,K.came,K.came+0.3));$('dEar').style.transform=`scale(${0.8+0.3*Math.sin(t*12)*h})`;
    const c=seg(t,K.came-0.2,S.E);$('dWat').style.transform=`translateX(${-200*eio(c)}px) scale(.62)`;}
  if(inE){const s=seg(t,K.ans-0.1,K.ans+0.15);$('eSt').style.opacity=s;$('eSt').style.transform=`rotate(-8deg) scale(${s>0?2.2-1.2*eo(s):2.2})`;}
  if(inF){const y=seg(t,K.years-0.1,K.later);$('fYrN').textContent=Math.round(1876+150*eio(y));$('fLab').style.opacity=seg(t,K.later-0.2,K.later+0.2);
    const ph=seg(t,K.still-0.2,K.still+0.2);$('fPh').style.opacity=ph;$('fPh').style.transform=`translateY(${(1-eo(ph))*120}px) translateX(${t<K.ans2?Math.sin(t*70)*6*(Math.sin(t*5)>0?1:0):0}px)`;
    const q=seg(t,K.does-0.1,K.does+0.25);$('fQ').style.opacity=q;$('fQ').style.transform=`scale(${q>0?back(q)*(1+0.05*Math.sin(t*8)):0})`;
    let r='';if(ph>0){for(let k=0;k<3;k++){const z=((t-K.still)*0.9+k/3)%1;r+=`<div class="abs" style="left:${540-260-z*260}px;top:${960-260-z*260}px;width:${520+z*520}px;height:${520+z*520}px;border-radius:50%;border:5px solid rgba(63,230,240,${(1-z)*0.4})"></div>`;}}$('fRings').innerHTML=r;}
'''
scr = SCR
a = scr.index("  if(inA){"); b = scr.index("  if(inG){")
scr = scr[:a] + js_new + scr[b:]
scr = scr.replace("const a=t>=K.first;", "const a=t>=K.ring;").replace("seg(t,K.first,K.first+0.3)", "seg(t,K.ring,K.ring+0.3)")
scr = scr.replace("const wB=$('windB').getContext('2d'),smD=$('smokeD').getContext('2d');", "")
scr = scr.replace("stars('starsA',260,1200);stars('starsE',220,1100);", "")
html = head + body + '<div id="cap" class="abs"></div>\n<div id="vig"></div>\n<canvas id="grain" width="270" height="480"></canvas>\n' + scr
open("/home/claude/reel11/reel.html", "w").write(html)
print("ok")
