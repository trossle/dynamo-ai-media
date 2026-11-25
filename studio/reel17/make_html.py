exec(open("/home/claude/reel17/_parts.py").read())
SEP = "#C9A46A"; INK = "#120C07"; RED = "#D2553F"
head = HEAD.replace("</style>", """
.paper{background:radial-gradient(ellipse at 50% 40%,#3A2A18,#140E08 72%)}
.serif{font-family:'DejaVu Serif',Georgia,serif}
.lab{font-family:'DejaVu Serif',Georgia,serif;font-weight:700;letter-spacing:6px;color:#C9A46A;text-align:center}
.stamp{border:10px solid #3FE6F0;border-radius:24px;color:#3FE6F0;font-weight:900;letter-spacing:6px;text-align:center;background:rgba(5,11,22,.6)}
</style>""")

PHONE = f'''<svg width="300" height="560" viewBox="0 0 300 560">
<ellipse cx="150" cy="530" rx="120" ry="22" fill="#6B4423"/><rect x="120" y="180" width="60" height="350" rx="12" fill="#2A1E12"/>
<rect x="128" y="190" width="10" height="330" fill="#4A3A28"/><ellipse cx="150" cy="170" rx="80" ry="40" fill="#2A1E12"/><ellipse cx="150" cy="160" rx="62" ry="26" fill="#4A3A28"/>
<rect x="210" y="260" width="22" height="120" rx="8" fill="{SEP}"/><rect x="226" y="250" width="40" height="40" rx="10" fill="#2A1E12"/>
<path d="M200 300 Q260 300 262 360 L262 420" fill="none" stroke="#2A1E12" stroke-width="10"/><ellipse cx="262" cy="440" rx="30" ry="22" fill="#2A1E12"/></svg>'''
HATMAN = f'''<svg width="300" height="700" viewBox="0 0 300 700"><rect x="100" y="0" width="100" height="90" rx="6" fill="{INK}"/><rect x="76" y="82" width="148" height="16" rx="8" fill="{INK}"/>
<path d="M150 96 C118 96 100 124 104 154 C106 176 116 190 128 198 L120 236 C150 250 168 246 182 232 L176 196 C190 186 198 168 198 148 C200 118 182 96 150 96 Z" fill="{INK}"/>
<path d="M50 700 L66 340 C72 280 108 252 150 252 C192 252 228 280 234 340 L250 700 Z" fill="{INK}"/></svg>'''
WOMAN = f'''<svg width="300" height="640" viewBox="0 0 300 640"><circle cx="150" cy="70" r="34" fill="{INK}"/>
<path d="M150 90 C118 90 102 118 106 148 C108 172 120 188 134 194 L128 226 C150 238 168 236 178 224 L172 192 C188 182 196 164 196 144 C198 114 182 90 150 90 Z" fill="{INK}"/>
<path d="M40 640 L60 330 C66 270 104 240 150 240 C196 240 234 270 240 330 L260 640 Z" fill="{INK}"/>
<path d="M120 300 L60 420" stroke="{INK}" stroke-width="26" stroke-linecap="round"/></svg>'''
JACKS = "".join(f'<circle cx="{60+c*80}" cy="{70+r*80}" r="16" fill="#140E08" stroke="{SEP}" stroke-width="4"/>' for r in range(5) for c in range(8))
BOARD = f'''<svg width="720" height="560" viewBox="0 0 720 560"><rect x="0" y="0" width="720" height="560" rx="20" fill="#5A3A1E" stroke="#3A2410" stroke-width="10"/>
<rect x="20" y="20" width="680" height="420" rx="10" fill="#3A2614"/>{JACKS}<rect x="0" y="460" width="720" height="100" fill="#6B4423"/>
{"".join(f'<rect x="{50+k*70}" y="480" width="18" height="60" rx="6" fill="{SEP}"/>' for k in range(9))}</svg>'''

def person(x, y, label, sc=.55, svg=None, idn=""):
    return (f'<div id="{idn}" class="abs" style="left:{x}px;top:{y}px;width:{300*sc:.0f}px">'
            f'<div style="transform:scale({sc});transform-origin:0 0;width:300px;height:0">{svg or HATMAN}</div>'
            f'<div class="lab" style="position:absolute;left:-60px;right:-60px;top:{700*sc+14:.0f}px;font-size:34px">{label}</div></div>')

DIAL = f'''<svg width="560" height="560" viewBox="0 0 560 560"><circle cx="280" cy="280" r="270" fill="#2A1E12" stroke="{SEP}" stroke-width="10"/>
<g id="dialR">{"".join(f'<circle cx="{280+190*__import__("math").cos((k*30-60)*3.14159/180):.0f}" cy="{280+190*__import__("math").sin((k*30-60)*3.14159/180):.0f}" r="44" fill="#140E08" stroke="{SEP}" stroke-width="5"/>' for k in range(10))}</g>
<circle cx="280" cy="280" r="96" fill="{SEP}"/><text x="280" y="296" text-anchor="middle" font-family="DejaVu Serif" font-weight="700" font-size="44" fill="#2A1E12">AUTO</text>
<path d="M470 420 L520 470" stroke="{SEP}" stroke-width="16" stroke-linecap="round"/></svg>'''

A = f'''<!-- A: hook -->
<div id="sA" class="sc paper">
  <div id="aSign" class="abs" style="left:150px;top:230px;width:780px;padding:26px 0;border:8px solid {SEP};border-radius:14px;background:#2A1E12;transform-origin:50% -60px">
    <div class="lab" style="font-size:66px">A. B. STROWGER</div><div class="lab" style="font-size:40px;margin-top:6px">UNDERTAKER</div></div>
  <div class="abs" style="left:300px;top:150px;width:4px;height:90px;background:{SEP}"></div><div class="abs" style="left:776px;top:150px;width:4px;height:90px;background:{SEP}"></div>
  <div id="aPh" class="abs" style="left:390px;top:620px">{PHONE}</div>
  <div id="aRings" class="abs" style="inset:0"></div>
  <div id="aGear" class="abs" style="left:110px;top:640px;font-size:150px;opacity:0;color:{SEP}">⚙</div>
  <div id="aZero" class="abs" style="left:640px;top:700px;padding:16px 30px;border-radius:999px;background:{RED};font-size:48px;font-weight:900;opacity:0">0 calls</div>
</div>'''
B = f'''<!-- B: Kansas City, 1880s -->
<div id="sB" class="sc paper">
  <div id="bYr" class="big serif" style="top:170px;font-size:200px;color:{SEP};opacity:0">1880s</div>
  <div id="bKC" class="big lab" style="top:420px;font-size:56px;opacity:0">KANSAS CITY</div>
  <div id="bMan" class="abs" style="left:150px;top:640px;opacity:0;transform-origin:0 0">{HATMAN}</div>
  <div id="bShop" class="abs" style="left:520px;top:700px;width:420px;height:560px;border:8px solid {SEP};border-radius:12px;background:rgba(40,28,16,.6);opacity:0">
    <div class="lab" style="margin-top:30px;font-size:36px">FUNERAL<br>PARLOR</div>
    <div style="position:absolute;left:130px;bottom:0;width:160px;height:250px;border:6px solid {SEP};border-bottom:0;border-radius:80px 80px 0 0"></div></div>
</div>'''
C = f'''<!-- C: the operator -->
<div id="sC" class="sc paper">
  <div class="big lab" style="top:170px;font-size:48px">TELEPHONE EXCHANGE</div>
  <div id="cBoard" class="abs" style="left:180px;top:280px">{BOARD}</div>
  <div id="cOp" class="abs" style="left:390px;top:780px;transform-origin:0 0">{WOMAN}</div>
  <div id="cLab" class="big lab" style="top:1250px;font-size:42px;opacity:0">THE OPERATOR</div>
  <div id="cRival" class="abs" style="left:800px;top:740px;opacity:0">{person(0,0,"HER HUSBAND",.5)}</div>
  <svg class="abs" style="left:0;top:0" width="1080" height="1920"><path id="cLink" d="M600 980 Q700 820 810 860" fill="none" stroke="{RED}" stroke-width="8" stroke-dasharray="4 14" stroke-linecap="round" opacity="0"/></svg>
</div>'''
D = f'''<!-- D: calls re-routed -->
<div id="sD" class="sc paper">
  <div class="abs" style="left:60px;top:300px;width:200px;height:200px;border-radius:50%;border:8px solid {SEP};display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:900;color:{SEP}" class="lab">CALLER</div>
  <div class="abs" style="left:390px;top:330px;width:300px;height:140px;border-radius:16px;background:#5A3A1E;border:6px solid #3A2410;display:flex;align-items:center;justify-content:center"><div class="lab" style="font-size:32px;color:#EDE3CC">OPERATOR</div></div>
  {person(160, 760, "STROWGER", .55, None, "dS")}
  {person(760, 760, "RIVAL", .55, None, "dR")}
  <svg class="abs" style="left:0;top:0" width="1080" height="1920">
    <path d="M260 400 L390 400" stroke="{SEP}" stroke-width="8" stroke-dasharray="4 14" stroke-linecap="round"/>
    <path id="dP1" d="M500 470 Q400 600 245 740" fill="none" stroke="{SEP}" stroke-width="8" stroke-dasharray="4 14" stroke-linecap="round" opacity=".5"/>
    <path id="dP2" d="M580 470 Q700 600 845 740" fill="none" stroke="#3FE6F0" stroke-width="10" stroke-linecap="round" stroke-dasharray="1000" stroke-dashoffset="1000"/></svg>
  <div id="dX" class="abs" style="left:300px;top:520px;font-size:150px;font-weight:900;color:{RED};opacity:0">✕</div>
  <div id="dPulse" class="abs" style="width:46px;height:46px;border-radius:50%;background:#3FE6F0;box-shadow:0 0 40px 14px rgba(63,230,240,.6);opacity:0"></div>
</div>'''
E = f'''<!-- E: the machine -->
<div id="sE" class="sc paper">
  <div id="eDial" class="abs" style="left:260px;top:430px;opacity:0">{DIAL}</div>
  <div id="eYr" class="big serif" style="top:150px;font-size:200px;color:{SEP};opacity:0">1892</div>
  <div id="eLab" class="big lab" style="top:1060px;font-size:40px;line-height:1.5;opacity:0">LA PORTE, INDIANA<br>FIRST AUTOMATIC EXCHANGE</div>
  <div id="eSt" class="abs stamp" style="left:170px;right:170px;top:640px;padding:30px 10px;font-size:80px;background:rgba(20,14,8,.85);transform:rotate(-8deg);opacity:0">NO OPERATOR</div>
</div>'''
def lost(i, label, sub, y):
    return (f'<div id="fL{i}" class="card" style="top:{y}px;opacity:0;display:flex;align-items:center;gap:30px">'
            f'<span style="width:100px;height:100px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:rgba(255,77,77,.16);border:4px solid #FF6B6B;font-size:52px;color:#FF6B6B">✕</span>'
            f'<div><div style="font-size:54px;font-weight:900">{label}</div><div style="font-size:32px;color:#9FB6CC;font-weight:700;margin-top:4px">{sub}</div></div></div>')
F = f'''<!-- F: calls still get lost -->
<div id="sF" class="sc" style="background:radial-gradient(ellipse at 50% 35%,#0E3550,#050B16 70%)">
  <div id="fT" class="big" style="top:170px;font-size:120px;opacity:0"><span class="gtext">TODAY</span></div>
  {lost(1, "Line busy", "Missed call · 11:05 AM", 460)}{lost(2, "Lunch break", "Missed call · 1:40 PM", 700)}{lost(3, "Shop closed", "Missed call · 8:20 PM", 940)}
</div>'''

G2 = G.replace("Incoming call · 11:42 PM", "Incoming call · new customer")
I2 = I.replace("Never let a call go dark.", "No call lost again.")
body = '<div id="stage" class="abs" style="inset:0">\n' + A + B + C + D + E + F + G2 + I2 + '</div>\n'

js_new = r'''
  if(inA){const sw=Math.sin(t*2.2)*3*(1-seg(t,0,4));$('aSign').style.transform=`rotate(${sw}deg)`;
    const silent=seg(t,K.cust-0.6,K.cust);let r='';for(let k=0;k<3;k++){const q=((t*1.1)+k/3)%1;const a=(1-q)*0.55*(1-silent);r+=`<div class="abs" style="left:${540-80-q*240}px;top:${790-80-q*240}px;width:${160+q*480}px;height:${160+q*480}px;border-radius:50%;border:6px solid rgba(201,164,106,${a})"></div>`;}$('aRings').innerHTML=r;
    $('aPh').style.transform=`rotate(${silent<1?Math.sin(t*40)*2*(1-silent):0}deg)`;
    const g=seg(t,K.machine-0.1,K.machine+0.25);$('aGear').style.opacity=g;$('aGear').style.transform=`rotate(${t*90}deg) scale(${g>0?back(g):0})`;
    const z=seg(t,K.cust,K.cust+0.25);$('aZero').style.opacity=z;$('aZero').style.transform=`scale(${z>0?back(z):0})`;
    $('sA').style.transform+=` scale(${1+0.03*t/5})`;}
  if(inB){const y=seg(t,K.yrs-0.1,K.yrs+0.25);$('bYr').style.opacity=y;$('bYr').style.transform=`scale(${y>0?back(y):0})`;
    $('bKC').style.opacity=seg(t,K.kc-0.1,K.kc+0.25);
    const m=seg(t,K.almon-0.1,K.almon+0.4);$('bMan').style.opacity=m;$('bMan').style.transform=`translateX(${(1-eo(m))*-120}px) scale(.8)`;
    const s=seg(t,K.funeral-0.1,K.funeral+0.4);$('bShop').style.opacity=s;$('bShop').style.transform=`translateY(${(1-eo(s))*60}px)`;}
  if(inC){$('cOp').style.transform=`translateY(${Math.sin(t*1.5)*4}px)`;
    $('cLab').style.opacity=seg(t,K.oper-0.15,K.oper+0.2);
    const w=seg(t,K.wife-0.1,K.wife+0.35);$('cRival').style.opacity=w;$('cRival').style.transform=`translateX(${(1-eo(w))*120}px)`;$('cLink').style.opacity=w;
    $('cBoard').querySelectorAll('circle').forEach((c,i)=>{const on=((Math.floor(t*4)+i*7)%23)==0;c.setAttribute('fill',on?'#3FE6F0':'#140E08');});}
  if(inD){const p=seg(t,K.through,K.husb+0.2);$('dP2').style.strokeDashoffset=1000*(1-eo(p));
    const a=seg(t,K.asked-0.2,K.through);const q=a<1?a:0;$('dPulse').style.opacity=a>0&&a<1?1:(p>0&&p<1?1:0);
    let x,y;if(a<1){x=160+q*380;y=400;}else{const u=eo(p);x=580+(845-580)*u;y=470+(740-470)*u-60*Math.sin(u*Math.PI);}
    $('dPulse').style.left=(x-23)+'px';$('dPulse').style.top=(y-23)+'px';
    const xx=seg(t,K.through,K.through+0.25);$('dX').style.opacity=xx;$('dX').style.transform=`scale(${xx>0?back(xx):0})`;
    $('dS').style.opacity=1-0.5*seg(t,K.husb,K.husb+0.4);$('dR').style.filter=`drop-shadow(0 0 ${30*seg(t,K.husb,K.husb+0.3)}px rgba(63,230,240,.8))`;}
  if(inE){const d=seg(t,K.built-0.1,K.built+0.35);$('eDial').style.opacity=d;$('eDial').style.transform=`scale(${d>0?0.6+0.4*back(d):0.6})`;
    $('dialR').setAttribute('transform',`rotate(${Math.sin(t*2.4)*40+(t-K.built)*20} 280 280)`);
    const st=seg(t,K.cut,K.cut+0.18);$('eSt').style.opacity=st*(1-seg(t,K.yr2-0.3,K.yr2));$('eSt').style.transform=`rotate(-8deg) scale(${st>0?2.2-1.2*eo(st):2.2})`;
    const y=seg(t,K.yr2-0.1,K.yr2+0.25);$('eYr').style.opacity=y;$('eYr').style.transform=`scale(${y>0?back(y):0})`;
    $('eLab').style.opacity=seg(t,K.auto-0.1,K.auto+0.3);}
  if(inF){const ti=seg(t,S.F,S.F+0.4);$('fT').style.opacity=ti;$('fT').style.transform=`scale(${ti>0?back(ti):0})`;
    [['fL1','busy'],['fL2','lunch'],['fL3','closed']].forEach(([id,k])=>{const q=seg(t,K[k]-0.15,K[k]+0.2);$(id).style.opacity=q;$(id).style.transform=`translateX(${(1-eo(q))*-300}px)`;});}
'''
scr = SCR
import re as _re
scr = scr.replace("const i=seg(t,a,a+0.22)","const i=a<=0?1:seg(t,a,a+0.22)")
a = scr.index("  if(inA){"); b = scr.index("  if(inG){")
scr = scr[:a] + js_new + scr[b:]
scr = scr.replace("const a=t>=K.first;", "const a=t>=K.ring;").replace("seg(t,K.first,K.first+0.3)", "seg(t,K.ring,K.ring+0.3)")
scr = scr.replace("const wB=$('windB').getContext('2d'),smD=$('smokeD').getContext('2d');", "")
scr = scr.replace("stars('starsA',260,1200);stars('starsE',220,1100);", "")
html = head + body + '<div id="cap" class="abs"></div>\n<div id="vig"></div>\n<canvas id="grain" width="270" height="480"></canvas>\n' + scr
open("/home/claude/reel17/reel.html", "w").write(html)
print("ok")
