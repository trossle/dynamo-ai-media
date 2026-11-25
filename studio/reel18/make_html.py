exec(open("/home/claude/reel18/_parts.py").read())
SEP = "#C9A46A"; INK = "#120C07"; RED = "#D2553F"; HAY = "#D9B25A"
head = HEAD.replace("</style>", """
.paper{background:radial-gradient(ellipse at 50% 40%,#3A2A18,#140E08 72%)}
.serif{font-family:'DejaVu Serif',Georgia,serif}
.lab{font-family:'DejaVu Serif',Georgia,serif;font-weight:700;letter-spacing:6px;color:#C9A46A;text-align:center}
.stamp{border:10px solid #3FE6F0;border-radius:24px;color:#3FE6F0;font-weight:900;letter-spacing:6px;text-align:center;background:rgba(5,11,22,.6)}
</style>""")

def bale(x, y, w=150, h=90):
    return (f'<g transform="translate({x} {y})"><rect width="{w}" height="{h}" rx="10" fill="{HAY}"/>'
            + "".join(f'<line x1="{6}" y1="{12+k*16}" x2="{w-6}" y2="{14+k*16}" stroke="#A8822E" stroke-width="3"/>' for k in range(5))
            + f'<rect x="{w*0.28}" y="0" width="8" height="{h}" fill="#6B4A1E"/><rect x="{w*0.68}" y="0" width="8" height="{h}" fill="#6B4A1E"/></g>')
FF = f'''<svg width="160" height="330" viewBox="0 0 160 330"><path d="M30 46 Q80 -6 130 46 L140 58 L20 58 Z" fill="{INK}"/><rect x="10" y="52" width="140" height="12" rx="6" fill="{INK}"/>
<circle cx="80" cy="90" r="32" fill="{INK}"/><path d="M28 330 L36 170 C40 136 58 122 80 122 C102 122 120 136 124 170 L132 330 Z" fill="{INK}"/>
<path id="ffArm" d="M118 150 L150 70" stroke="{INK}" stroke-width="22" stroke-linecap="round"/></svg>'''
HORSE = f'''<svg width="260" height="200" viewBox="0 0 300 230"><path d="M58 118 C50 96 70 80 104 80 L196 78 C214 60 226 34 244 22 L262 12 C272 8 282 14 286 24 L298 52 C302 62 296 70 286 68 L266 62 C258 80 250 100 246 120 C244 146 224 154 196 152 L108 154 C78 156 62 142 58 118 Z" fill="{INK}"/>
{"".join(f'<rect x="{x-9}" y="135" width="18" height="80" rx="8" fill="{INK}"/>' for x in (80,100,205,225))}</svg>'''
ENGINE = f'''<svg width="330" height="210" viewBox="0 0 330 210"><rect x="20" y="70" width="230" height="80" rx="10" fill="#8A3A2A"/><rect x="190" y="10" width="60" height="70" rx="20" fill="{SEP}"/>
<rect x="210" y="0" width="20" height="20" fill="#5A3A1E"/><circle cx="70" cy="170" r="36" fill="none" stroke="{INK}" stroke-width="10"/><circle cx="230" cy="170" r="36" fill="none" stroke="{INK}" stroke-width="10"/>
<line x1="250" y1="110" x2="330" y2="110" stroke="{INK}" stroke-width="8"/></svg>'''

# firehouse cross-section: floors at y 400 (loft), 820 (beds), 1240 (ground)
def house(pole=False, diag=False, stairs=True, ff=False, idp=""):
    s = f'<svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">'
    s += f'<rect x="90" y="300" width="900" height="1040" fill="rgba(40,28,16,.55)" stroke="{SEP}" stroke-width="10"/>'
    s += f'<polygon points="70,305 540,150 1010,305" fill="#2A1E12" stroke="{SEP}" stroke-width="10"/>'
    for y in (720, 1030):
        s += f'<rect x="90" y="{y}" width="900" height="14" fill="{SEP}"/>'
    s += f'<rect x="60" y="1340" width="960" height="16" fill="{SEP}"/>'
    s += bale(160, 630) + bale(320, 630) + bale(240, 545) + bale(800, 630)
    s += f'<rect x="170" y="960" width="200" height="54" rx="10" fill="#4A3A28"/><rect x="420" y="960" width="200" height="54" rx="10" fill="#4A3A28"/>'
    if stairs:
        s += "".join(f'<rect x="{830 - (k % 2) * 60}" y="{1030 + k*38}" width="120" height="12" fill="#6B4A1E"/>' for k in range(8))
        s += "".join(f'<rect x="{830 - (k % 2) * 60}" y="{720 + k*38}" width="120" height="12" fill="#6B4A1E"/>' for k in range(8))
    if diag:
        s += f'<line id="{idp}pole" x1="640" y1="430" x2="540" y2="1340" stroke="#B08850" stroke-width="18" stroke-linecap="round"/>'
    if pole:
        s += f'<rect id="{idp}pole" x="584" y="300" width="22" height="1040" fill="url(#brass)"/>'
        s += '<defs><linearGradient id="brass"><stop offset="0" stop-color="#8A6A2A"/><stop offset=".5" stop-color="#F2D27A"/><stop offset="1" stop-color="#8A6A2A"/></linearGradient></defs>'
    s += '</svg>'
    s += f'<div class="abs" style="left:150px;top:1180px">{HORSE}</div><div class="abs" style="left:420px;top:1150px">{ENGINE}</div>'
    return s

BELL = f'''<svg width="260" height="260" viewBox="0 0 260 260"><path d="M130 30 C80 30 60 70 60 120 L50 180 L210 180 L200 120 C200 70 180 30 130 30 Z" fill="{SEP}"/>
<rect x="40" y="176" width="180" height="18" rx="9" fill="#8A6A3A"/><circle cx="130" cy="210" r="20" fill="#8A6A3A"/><rect x="122" y="10" width="16" height="26" rx="6" fill="#8A6A3A"/></svg>'''
CAPT = f'''<svg width="300" height="700" viewBox="0 0 300 700"><path d="M86 70 Q150 20 214 70 L224 86 L76 86 Z" fill="{INK}"/><rect x="66" y="80" width="168" height="16" rx="8" fill="{INK}"/>
<path d="M150 96 C118 96 100 124 104 154 C106 176 116 190 128 198 L120 236 C150 250 168 246 182 232 L176 196 C190 186 198 168 198 148 C200 118 182 96 150 96 Z" fill="{INK}"/>
<path d="M50 700 L66 340 C72 280 108 252 150 252 C192 252 228 280 234 340 L250 700 Z" fill="{INK}"/></svg>'''

A = f'''<!-- A: hook -->
<div id="sA" class="sc paper">
  <div class="abs" style="left:520px;top:0;width:40px;height:1920px;background:linear-gradient(90deg,#8A6A2A,#F2D27A,#8A6A2A);box-shadow:0 0 60px rgba(242,210,122,.35)"></div>
  <canvas id="streakA" class="abs" width="1080" height="1920" style="left:0;top:0"></canvas>
  <div id="aFF" class="abs" style="left:430px;top:0;transform:scale(1.4);transform-origin:80px 0">{FF}</div>
  <svg id="aHay" class="abs" style="left:300px;top:760px;opacity:0;overflow:visible" width="480" height="300">{bale(0,140,220,130)}{bale(240,140,220,130)}{bale(120,10,220,130)}</svg>
</div>'''
B = f'''<!-- B: the firehouse -->
<div id="sB" class="sc paper">
  <div class="abs" style="inset:0;transform:translateY(190px) scale(.84);transform-origin:540px 0">{house()}
  <div id="bTag1" class="abs lab" style="left:600px;top:560px;font-size:34px;opacity:0">HAY LOFT ↓</div>
  <div id="bTag2" class="abs lab" style="left:640px;top:1270px;font-size:34px;opacity:0">HORSES</div></div>
  <div id="bYr" class="big serif" style="top:20px;font-size:140px;color:{SEP};opacity:0">1870s</div>
  <div id="bLab" class="big lab" style="top:180px;font-size:38px;opacity:0;z-index:3">CHICAGO · ENGINE CO. 21</div>
</div>'''
C = f'''<!-- C: the alarm -->
<div id="sC" class="sc paper">
  <div class="abs" style="inset:0;transform:translateY(190px) scale(.84);transform-origin:540px 0">{house()}
  <div id="cFF" class="abs" style="left:560px;top:400px">{FF}</div>
  <div id="cName" class="abs lab" style="left:470px;top:360px;font-size:32px;opacity:0">GEORGE REID</div></div>
  <div id="cBell" class="abs" style="left:410px;top:20px;transform-origin:130px 20px">{BELL}</div>
  <div id="cRings" class="abs" style="inset:0"></div>
</div>'''
D = f'''<!-- D: slide -->
<div id="sD" class="sc paper">
  <div class="abs" style="inset:0;transform:translateY(190px) scale(.84);transform-origin:540px 0">{house(diag=True, idp="d")}
  <div id="dFF" class="abs" style="left:560px;top:400px;transform-origin:80px 165px">{FF}</div>
  <div id="dX" class="abs" style="left:800px;top:780px;font-size:200px;font-weight:900;color:{RED};opacity:0">✕</div>
  <div id="dStairs" class="abs lab" style="left:760px;top:1360px;font-size:34px;opacity:0">STAIRS</div>
  <canvas id="dStreak" class="abs" width="1080" height="1920" style="left:0;top:0"></canvas></div>
</div>'''
E = f'''<!-- E: permanent pole -->
<div id="sE" class="sc paper">
  <div class="abs" style="inset:0;transform:translateY(190px) scale(.84);transform-origin:540px 0">{house(pole=True, stairs=False, idp="e")}
  <div id="eCap" class="abs" style="left:700px;top:820px;transform:scale(.62);transform-origin:0 0;opacity:0">{CAPT}</div>
  <div id="eName" class="abs lab" style="left:650px;top:1280px;font-size:30px;opacity:0;width:320px">CAPT. DAVID KENYON</div></div>
  <div id="eSt" class="abs stamp" style="left:120px;right:120px;top:560px;padding:30px 10px;font-size:68px;background:rgba(20,14,8,.88);transform:rotate(-8deg);opacity:0">OFTEN FIRST<br>ON THE SCENE</div>
</div>'''
def biz(i, label, y):
    return (f'<div id="fB{i}" class="card" style="top:{y}px;opacity:0;display:flex;align-items:center;gap:30px">'
            f'<span id="fI{i}" style="width:100px;height:100px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;border:4px solid #9FB6CC;font-size:46px;color:#9FB6CC">☎</span>'
            f'<div><div style="font-size:50px;font-weight:900">{label}</div><div id="fS{i}" style="font-size:34px;color:#9FB6CC;font-weight:700;margin-top:4px">Ringing…</div></div></div>')
F = f'''<!-- F: first to answer -->
<div id="sF" class="sc" style="background:radial-gradient(ellipse at 50% 35%,#0E3550,#050B16 70%)">
  <div id="fT" class="big" style="top:180px;font-size:84px;line-height:1.1;opacity:0">A customer calls<br><span class="gtext">3 businesses</span></div>
  {biz(1, "Business A", 520)}{biz(2, "Business B", 760)}{biz(3, "Business C", 1000)}
</div>'''

G2 = G.replace("Incoming call · 11:42 PM", "Incoming call · new customer")
I2 = I.replace("Never let a call go dark.", "Be first to answer.")
body = '<div id="stage" class="abs" style="inset:0">\n' + A + B + C + D + E + F + G2 + I2 + '</div>\n'

js_new = r'''
  if(inA){const y=((t*900+800)%2300)-330;$('aFF').style.top=y+'px';const c=$('streakA').getContext('2d');c.clearRect(0,0,1080,1920);
    c.strokeStyle='rgba(242,210,122,.35)';c.lineWidth=5;sd=5;for(let i=0;i<10;i++){const x=440+rnd()*200,yy=((t*1400+rnd()*1920)%2100)-100;c.beginPath();c.moveTo(x,yy);c.lineTo(x,yy-220);c.stroke();}
    const h=seg(t,K.hay-0.1,K.hay+0.3);$('aHay').style.opacity=h;$('aHay').style.transform=`scale(${h>0?back(h):0})`;
    $('sA').style.transform+=` scale(${1+0.03*t/5})`;}
  if(inB){const y=seg(t,K.yrs-0.1,K.yrs+0.25);$('bYr').style.opacity=y;$('bYr').style.transform=`scale(${y>0?back(y):0})`;
    $('bLab').style.opacity=seg(t,K.chi-0.1,K.chi+0.3);$('bTag2').style.opacity=seg(t,K.horses-0.1,K.horses+0.3);$('bTag1').style.opacity=seg(t,K.top-0.1,K.top+0.3);
    $('sB').style.transform+=` scale(${1+0.04*seg(t,S.B,S.C)})`;}
  if(inC){const r=t>K.alarm-0.1;$('cBell').style.transform=`rotate(${r?Math.sin(t*40)*14:0}deg)`;
    let w='';if(r){for(let k=0;k<3;k++){const q=((t-K.alarm)*1.4+k/3)%1;w+=`<div class="abs" style="left:${540-60-q*300}px;top:${150-60-q*300}px;width:${120+q*600}px;height:${120+q*600}px;border-radius:50%;border:6px solid rgba(201,164,106,${(1-q)*0.6})"></div>`;}}$('cRings').innerHTML=w;
    $('cName').style.opacity=seg(t,K.reid-0.1,K.reid+0.3);$('cFF').style.transform=`translateY(${r?Math.sin(t*20)*3:0}px)`;}
  if(inD){const x0=seg(t,K.stairs-0.2,K.stairs+0.15);$('dX').style.opacity=x0;$('dStairs').style.opacity=x0;$('dX').style.transform=`scale(${x0>0?back(x0):0})`;
    const gb=seg(t,K.grab-0.1,K.grab+0.3);const sl=eio(seg(t,K.slid-0.05,K.down+0.25));
    const x=560+(-20)*gb-100*sl, y=400+30*gb+780*sl;$('dFF').style.left=x+'px';$('dFF').style.top=y+'px';$('dFF').style.transform=`rotate(${-6*gb}deg)`;
    const c=$('dStreak').getContext('2d');c.clearRect(0,0,1080,1920);if(sl>0&&sl<1){c.strokeStyle='rgba(242,210,122,.5)';c.lineWidth=6;for(let k=0;k<4;k++){c.beginPath();c.moveTo(x+60+k*14,y-40);c.lineTo(x+60+k*14+22,y-260);c.stroke();}}}
  if(inE){const cp=seg(t,K.kenyon-0.1,K.kenyon+0.4);$('eCap').style.opacity=cp;$('eName').style.opacity=cp;$('eCap').style.transform=`translateX(${(1-eo(cp))*120}px) scale(.62)`;
    const p=seg(t,K.perm-0.1,K.perm+0.4);$('epole').setAttribute('height',1040*eo(p));
    const st=seg(t,K.first4-0.1,K.first4+0.12);$('eSt').style.opacity=st;$('eSt').style.transform=`rotate(-8deg) scale(${st>0?2.2-1.2*eo(st):2.2})`;}
  if(inF){const ti=seg(t,S.F,S.F+0.4);$('fT').style.opacity=ti;$('fT').style.transform=`translateY(${(1-eo(ti))*40}px)`;
    [1,2,3].forEach(i=>{const q=seg(t,K.calls-0.3+i*0.15,K.calls+i*0.15);$('fB'+i).style.opacity=q;$('fB'+i).style.transform=`translateX(${(1-eo(q))*-300}px) translateX(${t<K.firstA?Math.sin(t*60+i)*3:0}px)`;});
    const w=t>=K.firstA;$('fS2').textContent=w?'Answered ✓':'Ringing…';$('fS2').style.color=w?'#3FE6F0':'#9FB6CC';$('fI2').style.borderColor=w?'#3FE6F0':'#9FB6CC';$('fI2').style.color=w?'#3FE6F0':'#9FB6CC';
    $('fB2').style.boxShadow=w?'0 0 0 4px #3FE6F0,0 30px 80px rgba(63,230,240,.25)':'';
    [1,3].forEach(i=>{$('fS'+i).textContent=t>=K.every?'Still ringing…':'Ringing…';$('fS'+i).style.color=t>=K.every?'#FF6B6B':'#9FB6CC';});}
'''
scr = SCR
scr = scr.replace("const i=seg(t,a,a+0.22)", "const i=a<=0?1:seg(t,a,a+0.22)")
a = scr.index("  if(inA){"); b = scr.index("  if(inG){")
scr = scr[:a] + js_new + scr[b:]
scr = scr.replace("const a=t>=K.first;", "const a=t>=K.ring;").replace("seg(t,K.first,K.first+0.3)", "seg(t,K.ring,K.ring+0.3)")
scr = scr.replace("const wB=$('windB').getContext('2d'),smD=$('smokeD').getContext('2d');", "")
scr = scr.replace("stars('starsA',260,1200);stars('starsE',220,1100);", "")
html = head + body + '<div id="cap" class="abs"></div>\n<div id="vig"></div>\n<canvas id="grain" width="270" height="480"></canvas>\n' + scr
open("/home/claude/reel18/reel.html", "w").write(html)
print("ok")
