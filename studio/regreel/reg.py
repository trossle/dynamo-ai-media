import asyncio, subprocess, sys, os, re, json, math
import numpy as np, soundfile as sf
from playwright.async_api import async_playwright
MARK = open("/home/claude/carousel/mark_teal.svg").read(); WORD = open("/home/claude/carousel/word.svg").read()
def mark(size, gid, mono=None):
    s = MARK.replace('id="lgh"', f'id="{gid}"').replace('url(#lgh)', f'url(#{gid})')
    if mono: s = s.replace(f'fill="url(#{gid})"', f'fill="{mono}"')
    return re.sub(r'width="[\d.]+" height="[\d.]+"', f'width="{size}" height="{round(size*626/678)}"', s, count=1)
def word(h, color):
    s = re.sub(r'width="[\d.]+" height="[\d.]+"', f'width="{round(h*9625.19/1390.23)}" height="{h}"', WORD, count=1)
    return s.replace('fill="currentColor"', f'fill="{color}"')
NAVY = "#0B1B2E"; SLATE = "#4C5F73"
GRAD = "linear-gradient(150deg,#12D8D0 0%,#0BB2E0 42%,#1670E0 100%)"
GRADH = "linear-gradient(120deg,#12D8D0 0%,#0BB2E0 45%,#1670E0 100%)"
NAVYBG = ("radial-gradient(900px 900px at 85% 8%, rgba(18,216,208,0.36), transparent 60%), "
          "radial-gradient(900px 1000px at 0% 100%, rgba(22,112,224,0.45), transparent 60%), #0B1B2E")
ICO = {"phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
       "note": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
       "chat": '<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/>'}
def ico(n, s=40): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{ICO[n]}</svg>'
def tile(n, bg): return f'<span style="width:84px;height:84px;border-radius:24px;background:{bg};display:flex;align-items:center;justify-content:center;flex-shrink:0">{ico(n)}</span>'
HEADER = lambda col, gid: f'<div class="abs" style="left:84px;right:84px;top:150px;display:flex;align-items:center;justify-content:space-between"><div style="display:flex;align-items:center;gap:20px">{mark(70, gid, "#FFFFFF")}<span style="display:flex;align-items:center;gap:14px">{word(30, col)}<span style="font-size:36px;font-weight:600;color:{col}">AI</span></span></div><span style="font-size:32px;font-weight:500;color:rgba(255,255,255,.85)">@dynamo.asi</span></div>'
END = f'''<div id="end" class="abs" style="inset:0;background:{NAVYBG};opacity:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px">
<div style="filter:drop-shadow(0 0 50px rgba(18,216,208,.5))">{mark(220, "ge")}</div>
<div style="font-size:86px;font-weight:700;letter-spacing:-3px;text-align:center;line-height:1.05;padding:0 80px">__ENDLINE__</div>
<div style="font-size:44px;font-weight:600;color:#9FB6CC">₹4 per minute · answers 24×7</div>
<div style="padding:34px 60px;border-radius:999px;background:{GRADH};color:#04263F;font-size:50px;font-weight:800">Try 10 minutes free</div>
<div style="font-size:50px;font-weight:700">dynamoasi.com/app</div></div>'''
CSS = """*{box-sizing:border-box;margin:0;padding:0}html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:Poppins,'Inter',sans-serif;color:#fff;position:relative}.abs{position:absolute}"""
JS = """const $=id=>document.getElementById(id);const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));const seg=(t,a,b)=>cl((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3);const back=x=>{const c=1.8;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
function pop(id,t,a,dx=0,dy=60){const p=seg(t,a,a+0.35);const e=$(id);e.style.opacity=p;e.style.transform=`translate(${(1-eo(p))*dx}px,${(1-eo(p))*dy}px) scale(${p>0?0.85+0.15*back(p):0.85})`;}
function endc(t,a){const p=seg(t,a,a+0.4);$('end').style.opacity=p;$('end').style.transform=`scale(${1.06-0.06*eo(p)})`;}"""

# ---------- reel 1: 9:47 PM ----------
cards = [("phone", "#1670E0", "Dynamo AI answered", "Incoming call · Hindi · 2 min 14 s", "9:47 PM"),
         ("note", "#0BB2E0", "Call summary saved", "Wants a visit Saturday, 11 AM", "9:49 PM"),
         ("chat", "#12B5AE", "WhatsApp follow-up sent", "Lead added to your sheet", "9:49 PM")]
C = "".join(f'''<div id="c{i}" style="opacity:0;display:flex;align-items:center;gap:28px;padding:32px 36px;border-radius:38px;background:rgba(255,255,255,.95);box-shadow:0 30px 60px -28px rgba(6,40,90,.6);margin-left:{i*44}px">
{tile(ic, bg)}<div style="flex:1;min-width:0"><div style="font-size:40px;font-weight:600;color:{NAVY}">{a}</div><div style="font-size:31px;color:{SLATE};margin-top:4px">{b}</div></div><span style="font-size:28px;color:{SLATE};align-self:flex-start">{r}</span></div>''' for i, (ic, bg, a, b, r) in enumerate(cards))
R1 = dict(name="Dynamo-AI-Reel-947PM", dur=13.0, events=[0.3, 1.2, 3.2, 4.7, 6.2, 8.6, 9.6],
  html=f'''<div class="abs" style="inset:0;background:{GRAD}"></div>{HEADER("#FFFFFF","g1")}
<div id="clk" class="abs" style="left:84px;top:330px;font-size:200px;font-weight:700;letter-spacing:-8px;line-height:1;opacity:0">9:47 PM</div>
<div id="h1" class="abs" style="left:84px;right:84px;top:560px;font-size:68px;font-weight:700;letter-spacing:-2px;line-height:1.1;opacity:0">Shop closed. Team gone home.<br>The phone rings…</div>
<div class="abs" style="left:84px;right:160px;top:860px;display:flex;flex-direction:column;gap:26px">{C}</div>
<div id="h2" class="abs" style="left:84px;right:84px;top:1520px;font-size:64px;font-weight:700;letter-spacing:-2px;opacity:0">…and the customer still gets an answer.</div>''' + END.replace("__ENDLINE__", "Every call answered.<br>Even at 9:47 PM."),
  js="""window.render=function(t){const p=seg(t,0.3,0.7);$('clk').style.opacity=p;$('clk').style.transform=`translateX(${(1-eo(p))*-80}px) translateX(${t<3.2?Math.sin(t*60)*5*(Math.sin(t*6)>0?1:0):0}px)`;
pop('h1',t,1.2);pop('c0',t,3.2,200,0);pop('c1',t,4.7,200,0);pop('c2',t,6.2,200,0);pop('h2',t,7.4);endc(t,9.6);}""")

# ---------- reel 2: hired ----------
rows = [("ROLE", "Front desk + telecaller"), ("SHIFT", "24×7. Sundays and festivals too."), ("LANGUAGES", "Hindi, English and regional languages"),
        ("PICKS UP", "On the first ring"), ("FOLLOW-UP", "WhatsApp, the same minute"), ("SALARY", "₹4 per minute of calls")]
RW = "".join(f'''<div id="r{i}" style="opacity:0;display:grid;grid-template-columns:270px 1fr;gap:24px;align-items:baseline;padding:22px 0;border-bottom:2px solid #E3EBF2">
<span style="font-family:'DejaVu Sans Mono',monospace;font-size:26px;color:{SLATE}">{k}</span><span style="font-size:40px;font-weight:600;color:{'#1670E0' if k == 'SALARY' else NAVY};line-height:1.25">{v}</span></div>''' for i, (k, v) in enumerate(rows))
R2 = dict(name="Dynamo-AI-Reel-Hired", dur=13.5, events=[0.3, 1.4, 2.4, 3.1, 3.8, 4.5, 5.2, 5.9, 7.2, 10.0],
  html=f'''<div class="abs" style="inset:0;background:{NAVYBG}"></div>{HEADER("#FFFFFF","g2")}
<div id="h1" class="abs" style="left:84px;right:84px;top:300px;font-size:100px;font-weight:700;letter-spacing:-4px;line-height:1.04;opacity:0">Hiring a receptionist?<br><span style="background:{GRADH};-webkit-background-clip:text;background-clip:text;color:transparent">Read this first.</span></div>
<div id="card" class="abs" style="left:84px;right:84px;top:640px;background:#fff;border-radius:40px;padding:44px 52px 30px;box-shadow:0 40px 80px -30px rgba(0,0,0,.6);transform:rotate(-1.5deg);opacity:0">
<div style="display:flex;justify-content:space-between;font-family:'DejaVu Sans Mono',monospace;font-size:28px;font-weight:700;color:{NAVY};padding-bottom:8px"><span>JOB CARD #001</span><span id="status" style="color:{SLATE};font-weight:400">Status: open</span></div>{RW}
<div id="stamp" class="abs" style="right:-30px;bottom:-60px;border:9px solid #1670E0;border-radius:26px;padding:12px 34px 8px;color:#1670E0;background:#fff;font-family:'DejaVu Sans Mono',monospace;font-weight:700;font-size:92px;letter-spacing:8px;opacity:0;box-shadow:0 20px 40px -16px rgba(0,0,0,.5)">HIRED</div></div>
<div id="h2" class="abs" style="left:84px;right:84px;top:1560px;font-size:56px;font-weight:600;color:rgba(255,255,255,.9);opacity:0">No leave. No notice period. No missed calls.</div>''' + END.replace("__ENDLINE__", "Hire Dynamo AI."),
  js="""window.render=function(t){pop('h1',t,0.3);pop('card',t,1.4,0,120);for(let i=0;i<6;i++)pop('r'+i,t,2.4+i*0.7,60,0);
const s=seg(t,7.2,7.45);$('stamp').style.opacity=s;$('stamp').style.transform=`rotate(-12deg) scale(${s>0?2.4-1.4*eo(s):2.4})`;
$('status').textContent=t>=7.2?'Status: filled':'Status: open';const sh=t>=7.2?Math.exp(-(t-7.2)*8):0;$('card').style.transform=`rotate(-1.5deg) translate(${Math.sin(t*90)*14*sh}px,${Math.cos(t*80)*10*sh}px)`;
pop('h2',t,8.0);endc(t,10.0);}""")

SR = 44100
def music(dur, events, out):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n); rng = np.random.default_rng(4)
    nf = lambda m: 440 * 2 ** ((m - 69) / 12)
    def add(s, st, g):
        i = int(st * SR); j = min(n, i + len(s))
        if 0 <= i < n: x[i:j] += s[:j - i] * g
    def tone(f, L, d, h=((1, 1),)):
        m = int(L * SR); tt = np.arange(m) / SR; e = np.clip(tt / 0.003, 0, 1) * np.exp(-tt / d)
        return sum(g * np.sin(2 * np.pi * f * k * tt) for k, g in h) * e
    bpm = 112; b = 60 / bpm
    chords = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
    for k in range(int(dur / b) + 1):
        st = k * b
        kick = np.sin(2 * np.pi * np.cumsum(np.linspace(140, 45, int(0.25 * SR))) / SR) * np.exp(-np.arange(int(0.25 * SR)) / SR / 0.09)
        add(kick, st, 0.55)
        hat = rng.standard_normal(int(0.04 * SR)) * np.exp(-np.arange(int(0.04 * SR)) / SR / 0.01)
        add(hat, st + b / 2, 0.08)
        if k % 2 == 1: add(rng.standard_normal(int(0.15 * SR)) * np.exp(-np.arange(int(0.15 * SR)) / SR / 0.05), st, 0.12)
        c = chords[(k // 4) % 4]
        add(tone(nf(c[0] - 12), b * 0.9, 0.25, ((1, 1), (2, .3))), st, 0.30)
        for q, m in enumerate(c): add(tone(nf(m + 12), 0.25, 0.08, ((1, 1), (2, .2))), st + q * b / 3, 0.06)
    for e in events:
        m = int(0.3 * SR); add(np.convolve(rng.standard_normal(m), np.ones(25) / 25, 'same') * np.sin(np.linspace(0, np.pi, m)) ** 2, e - 0.18, 0.5)
        add(tone(nf(84), 0.25, 0.08), e, 0.08)
    x *= np.clip(t / 0.3, 0, 1) * np.clip((dur - t) / 1.0, 0, 1)
    x = np.tanh(x * 1.2); x /= np.max(np.abs(x)) / 0.9
    sf.write(out, np.stack([x, x], 1), SR)

async def render(R):
    os.makedirs("/home/claude/regreel/out", exist_ok=True)
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{R["html"]}<script>{JS}{R["js"]}</script></body></html>'
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.set_content(html); await pg.wait_for_timeout(500)
        tmp = f"/home/claude/regreel/{R['name']}.v.mp4"
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", "30", "-c:v", "mjpeg", "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
        for f in range(int(R["dur"] * 30)):
            await pg.evaluate(f"render({f/30})"); ff.stdin.write(await pg.screenshot(type="jpeg", quality=90))
        ff.stdin.close(); ff.wait(); await b.close()
    wav = f"/home/claude/regreel/{R['name']}.wav"; music(R["dur"], R["events"], wav)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", f"/home/claude/regreel/out/{R['name']}.mp4"], check=True)
    print("done", R["name"])

if __name__ == "__main__":
    for R in [R1, R2]: asyncio.run(render(R))
