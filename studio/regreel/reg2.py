import asyncio, sys
sys.path.insert(0, "/home/claude/regreel")
from reg import *

# ---------- reel 3: Sunday ----------
cards3 = [("phone", "#1670E0", "Dynamo AI answered", "Price enquiry · Hindi · 1 min 52 s", "11:20 AM"),
          ("note", "#0BB2E0", "Visit booked", "Monday, 5 PM · added to your sheet", "11:22 AM"),
          ("chat", "#12B5AE", "Call transferred to you", "Caller asked for the owner", "11:41 AM")]
C3 = "".join(f'''<div id="c{i}" style="opacity:0;display:flex;align-items:center;gap:28px;padding:32px 36px;border-radius:38px;background:rgba(255,255,255,.95);box-shadow:0 30px 60px -28px rgba(6,40,90,.6);margin-left:{i*44}px">
{tile(ic, bg)}<div style="flex:1;min-width:0"><div style="font-size:40px;font-weight:600;color:{NAVY}">{a}</div><div style="font-size:31px;color:{SLATE};margin-top:4px">{b}</div></div><span style="font-size:28px;color:{SLATE};align-self:flex-start">{r}</span></div>''' for i, (ic, bg, a, b, r) in enumerate(cards3))
R3 = dict(name="Dynamo-AI-Reel-Sunday", dur=13.5, events=[0.2, 1.3, 3.4, 4.9, 6.4, 8.0, 10.0],
  html=f'''<div class="abs" style="inset:0;background:{NAVYBG}"></div>{HEADER("#FFFFFF","g3")}
<div id="day" class="abs" style="left:84px;top:320px;font-size:170px;font-weight:700;letter-spacing:-7px;line-height:1;opacity:0"><span style="background:{GRADH};-webkit-background-clip:text;background-clip:text;color:transparent">Sunday.</span></div>
<div id="h1" class="abs" style="left:84px;right:84px;top:530px;font-size:66px;font-weight:700;letter-spacing:-2px;line-height:1.12;opacity:0">You're at a family function.<br>Your phone is in your pocket.</div>
<div class="abs" style="left:84px;right:160px;top:850px;display:flex;flex-direction:column;gap:26px">{C3}</div>
<div id="h2" class="abs" style="left:84px;right:84px;top:1520px;font-size:62px;font-weight:700;letter-spacing:-2px;opacity:0">Customers still got answers.</div>''' + END.replace("__ENDLINE__", "Your Sunday is yours.<br>The calls are ours."),
  js="""window.render=function(t){const p=seg(t,0.15,0.5);$('day').style.opacity=Math.max(p,t<0.15?0.4:0);$('day').style.transform=`scale(${0.8+0.2*back(p)})`;
pop('h1',t,1.3);pop('c0',t,3.4,200,0);pop('c1',t,4.9,200,0);pop('c2',t,6.4,200,0);pop('h2',t,8.0);endc(t,10.0);}""")

# ---------- reel 4: ring 1 ----------
def phone(idn, title):
    return f'''<div id="{idn}" class="abs" style="width:420px;height:760px;border-radius:64px;background:#0A1424;padding:14px;box-shadow:0 50px 100px -30px rgba(0,0,0,.7),0 0 0 3px rgba(255,255,255,.12);opacity:0">
<div style="position:relative;width:100%;height:100%;border-radius:52px;overflow:hidden;background:linear-gradient(#13243A,#0B1626)">
<div style="position:absolute;left:0;right:0;top:70px;text-align:center;font-size:28px;font-weight:600;color:#9FB6CC">{title}</div>
<div style="position:absolute;left:0;right:0;top:120px;text-align:center;font-size:40px;font-weight:700">New customer</div>
<div id="{idn}r" style="position:absolute;left:0;right:0;top:300px;text-align:center;font-size:150px;font-weight:700;letter-spacing:-6px">1</div>
<div style="position:absolute;left:0;right:0;top:470px;text-align:center;font-size:30px;font-weight:600;color:#9FB6CC">RING</div>
<div id="{idn}s" style="position:absolute;left:40px;right:40px;bottom:70px;padding:22px;border-radius:999px;text-align:center;font-size:36px;font-weight:700;background:rgba(255,255,255,.08)">Ringing…</div></div></div>'''
R4 = dict(name="Dynamo-AI-Reel-Ring-1", dur=14.0, events=[0.2, 1.0, 2.0, 3.0, 4.0, 5.0, 5.6, 7.2, 8.0, 11.0],
  html=f'''<div class="abs" style="inset:0;background:{GRAD}"></div>{HEADER("#FFFFFF","g4")}
<div id="h1" class="abs" style="left:84px;right:84px;top:300px;font-size:92px;font-weight:700;letter-spacing:-4px;line-height:1.04;opacity:0">How many rings<br>before they give up?</div>
<div id="pA" class="abs" style="left:84px;top:620px">{phone("a", "Your phone")}</div>
<div id="pB" class="abs" style="left:576px;top:620px">{phone("b", "With Dynamo AI")}</div>
<div id="h2" class="abs" style="left:84px;right:84px;top:1480px;font-size:60px;font-weight:700;letter-spacing:-2px;line-height:1.15;opacity:0">Your customer calls the next shop.<br>Or you pick up on ring 1.</div>''' + END.replace("__ENDLINE__", "Answered on<br>the first ring."),
  js="""window.render=function(t){pop('h1',t,-0.25);pop('a',t,0.4,0,120);
let r=Math.min(5,1+Math.floor(Math.max(0,t-1.0)));$('ar').textContent=r;const miss=t>=5.6;
$('as').textContent=miss?'Missed call':'Ringing…';$('as').style.background=miss?'#FF4D4D':'rgba(255,255,255,.08)';$('ar').style.color=miss?'#FF8A8A':'#fff';
$('a').style.transform+=` translateX(${!miss&&t>1?Math.sin(t*60)*5*(Math.sin(t*6.28)>0?1:0):0}px)`;
pop('b',t,6.6,0,120);const ans=t>=7.2;$('bs').textContent=ans?'Answered ✓':'Ringing…';$('bs').style.background=ans?'linear-gradient(120deg,#12D8D0,#0BB2E0 45%,#1670E0)':'rgba(255,255,255,.08)';
$('bs').style.color=ans?'#04263F':'#fff';$('br').style.color=ans?'#7FF3EE':'#fff';
pop('h2',t,8.0);endc(t,11.0);}""")

if __name__ == "__main__":
    for R in [R3, R4]: asyncio.run(render(R))
