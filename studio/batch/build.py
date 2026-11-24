import re, sys, asyncio, html as H
sys.path.insert(0, "/home/claude/batch")
from posts import POSTS
WORD = open("/home/claude/carousel/word.svg").read()
MARK = open("/home/claude/carousel/mark_teal.svg").read()
NAVY="#0B1B2E"; SLATE="#4C5F73"; WHITE="#FFFFFF"; LIGHT="#EEF8FB"
GRAD="linear-gradient(150deg, #12D8D0 0%, #0BB2E0 42%, #1670E0 100%)"
GRADH="linear-gradient(120deg, #12D8D0 0%, #0BB2E0 45%, #1670E0 100%)"
NAVYBG=("radial-gradient(900px 700px at 85% 8%, rgba(18,216,208,0.36), transparent 60%), "
        "radial-gradient(900px 800px at 0% 100%, rgba(22,112,224,0.45), transparent 60%), #0B1B2E")
MONO="'Space Mono', 'Courier New', monospace"
_id=[0]
def gid():
    _id[0]+=1; return f"g{_id[0]}"

def mark(size, mono=None, style=""):
    g=gid(); s=MARK.replace('id="lgh"', f'id="{g}"').replace('url(#lgh)', f'url(#{g})')
    if mono: s=s.replace(f'fill="url(#{g})"', f'fill="{mono}"')
    s=re.sub(r'width="[\d.]+" height="[\d.]+"', f'width="{size}" height="{round(size*626/678)}"', s, count=1)
    return s.replace('aria-hidden="true"', f'aria-hidden="true" style="flex-shrink: 0; {style}"', 1)
def word(h, color):
    s=re.sub(r'width="[\d.]+" height="[\d.]+"', f'width="{round(h*9625.19/1390.23)}" height="{h}"', WORD, count=1)
    return s.replace('fill="currentColor"', f'fill="{color}"')

THEMES = {
 "grad":  dict(bg=GRAD, fg=WHITE, sub="rgba(255,255,255,0.92)", logo=WHITE, acc=f"color: {NAVY}",
               card=WHITE, cfg=NAVY, csub=SLATE, ctabg=NAVY, ctafg=WHITE, wm=0.12, hint="rgba(255,255,255,0.22)"),
 "navy":  dict(bg=NAVYBG, fg=WHITE, sub="rgba(255,255,255,0.8)", logo=None,
               acc=f"background: {GRADH}; -webkit-background-clip: text; background-clip: text; color: transparent",
               card=WHITE, cfg=NAVY, csub=SLATE, ctabg=GRADH, ctafg=NAVY, wm=0.06, hint="rgba(255,255,255,0.12)"),
 "light": dict(bg=LIGHT, fg=NAVY, sub=SLATE, logo=None,
               acc=f"background: {GRADH}; -webkit-background-clip: text; background-clip: text; color: transparent",
               card=WHITE, cfg=NAVY, csub=SLATE, ctabg=NAVY, ctafg=WHITE, wm=0.07, hint="#D6E8F0"),
}

def ico(name, color="#fff", size=32):
    paths = {
     "phone":'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
     "note":'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
     "chat":'<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/>',
     "bell":'<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>',
     "check":'<path d="M20 6 9 17l-5-5"/>',
     "cross":'<path d="M18 6 6 18M6 6l12 12"/>',
     "home":'<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
     "plus":'<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>',
     "book":'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
     "car":'<path d="M5 17h14M3 17v-4l2.2-5.2A2 2 0 0 1 7 6.6h10a2 2 0 0 1 1.8 1.2L21 13v4"/><circle cx="7.5" cy="17.5" r="2"/><circle cx="16.5" cy="17.5" r="2"/><path d="M3 13h18"/>',
     "cart":'<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h7.8a2 2 0 0 0 2-1.5L21 7H6"/>',
    }
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'

ICOBG = {"phone":"#1670E0","note":"#0BB2E0","chat":"#12B5AE","bell":"#1385E3","check":"#12B5AE"}
def tile(name, bg=None, size=64, isz=32, radius=18):
    return f'<span style="width: {size}px; height: {size}px; border-radius: {radius}px; background: {bg or ICOBG.get(name, "#1670E0")}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{ico(name, size=isz)}</span>'

def head(text, T, size=None, mt=56):
    a, _, b = text.partition("|")
    n = len(a)+len(b)
    size = size or (92 if n <= 34 else 82 if n <= 46 else 72)
    inner = H.escape(a) + (f'<br><span style="{T["acc"]}">{H.escape(b)}</span>' if b else "")
    return f'<h1 style="position: relative; margin: {mt}px 0 0; font-size: {size}px; line-height: 1.04; font-weight: 700; letter-spacing: -{size/28:.1f}px; color: {T["fg"]}; text-wrap: balance">{inner}</h1>'

def sub(text, T, size=34, mt=26):
    return f'<p style="position: relative; margin: {mt}px 0 0; font-size: {size}px; line-height: 1.4; font-weight: 500; color: {T["sub"]}; max-width: 860px">{H.escape(text)}</p>'

def cta(T, text="Try 10 min free · dynamoasi.com/app"):
    return f'<span style="display: inline-flex; align-items: center; padding: 28px 42px; border-radius: 999px; background: {T["ctabg"]}; color: {T["ctafg"]}; font-size: 30px; font-weight: 700">{text}</span>'

def frame(T, body, footer, wm=True):
    logo = f'{mark(58, mono=T["logo"])}<span style="display: flex; align-items: center; gap: 12px">{word(26, T["fg"])}<span style="font-size: 30px; font-weight: 600; line-height: 1; color: {T["fg"]}">AI</span></span>'
    w = f'<div style="position: absolute; right: -280px; bottom: -160px; opacity: {T["wm"]}">{mark(980, mono=(WHITE if T["fg"]==WHITE else NAVY))}</div>' if wm else ""
    return f'''<div style="position: relative; width: 1080px; height: 1350px; overflow: hidden; box-sizing: border-box; padding: 88px 88px 80px; display: flex; flex-direction: column; background: {T["bg"]}; font-family: 'Poppins', 'Tiro Devanagari Hindi', system-ui, sans-serif; color: {T["fg"]}">
{w}
<div style="position: relative; display: flex; align-items: center; justify-content: space-between"><div style="display: flex; align-items: center; gap: 18px">{logo}</div><span style="font-size: 26px; font-weight: 500; color: {T["sub"]}">@dynamo.asi</span></div>
<div class="bd" style="position: relative; display: flex; flex-direction: column; margin: auto 0; padding: 36px 0 48px">{body}</div>
<div style="position: relative; display: flex; align-items: center; justify-content: space-between; gap: 24px">{footer}</div>
</div>'''

def chip(text, T):
    return f'<span style="position: relative; align-self: flex-start; margin-top: 52px; padding: 10px 24px; border-radius: 999px; border: 2px solid {T["hint"]}; font-size: 24px; font-weight: 600; color: {T["sub"]}">{H.escape(text)}</span>'

# ---------------- templates ----------------
def t_statement(p, T):
    body = head(p["h"], T, size=118, mt=0) + sub(p["sub"], T, size=40, mt=48)
    return frame(T, body, cta(T))

def t_notif(p, T):
    cards = ""
    for i, (ic, title, s, r) in enumerate(p["cards"]):
        cards += f'''<div style="display: flex; align-items: center; gap: 24px; padding: 26px 30px; border-radius: 30px; background: {T["card"]}; box-shadow: 0 24px 48px -24px rgba(6,40,90,0.45); transform: translateX({i*36}px)">
{tile(ic)}<div style="display: flex; flex-direction: column; gap: 4px; min-width: 0; flex: 1"><span style="font-size: 31px; font-weight: 600; color: {NAVY}; line-height: 1.2">{H.escape(title)}</span><span style="font-size: 25px; color: {SLATE}; line-height: 1.3">{H.escape(s)}</span></div>
<span style="font-size: 23px; font-weight: 500; color: {SLATE}; align-self: flex-start; white-space: nowrap">{r}</span></div>'''
    body = chip(p["tag"], T) + head(p["h"], T, size=92, mt=24) + f'<div style="position: relative; margin-top: 64px; display: flex; flex-direction: column; gap: 20px; padding-right: 72px">{cards}</div>'
    return frame(T, body, cta(T))

def t_chat(p, T):
    rows = ""
    for who, text in p["lines"]:
        if who == "s":
            rows += f'<div style="align-self: center; display: flex; align-items: center; gap: 12px; padding: 12px 24px; border-radius: 999px; background: #EEF4F8; color: {SLATE}; font-size: 24px; font-weight: 600">{ico("phone", SLATE, 24)}{H.escape(text)}</div>'
            continue
        d = who == "d"
        style = (f"align-self: flex-end; background: {GRADH}; color: {WHITE}; border-radius: 30px 30px 8px 30px"
                 if d else f"align-self: flex-start; background: #EEF4F8; color: {NAVY}; border-radius: 30px 30px 30px 8px")
        label = "Dynamo AI" if d else "Caller"
        rows += f'''<div style="display: flex; flex-direction: column; gap: 6px; max-width: 690px; {'align-self: flex-end; align-items: flex-end' if d else 'align-self: flex-start'}">
<span style="font-size: 20px; font-weight: 600; color: {SLATE}; padding: 0 10px">{label}</span>
<span style="{style}; padding: 18px 26px; font-size: 27px; line-height: 1.38; font-weight: 500">{H.escape(text)}</span></div>'''
    panel = f'''<div style="position: relative; margin-top: 40px; background: {T["card"]}; border-radius: 40px; padding: 30px 32px 26px; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 40px 80px -36px rgba(6,30,70,0.5)">
<div style="display: flex; align-items: center; gap: 14px; padding-bottom: 14px; border-bottom: 2px solid #E3EBF2">{tile("phone", size=46, isz=24, radius=14)}<span style="font-size: 24px; font-weight: 600; color: {NAVY}">Call transcript</span><span style="margin-left: auto; font-size: 22px; color: {SLATE}">Example call</span></div>
{rows}
<div style="align-self: flex-start; margin-top: 6px; display: flex; align-items: center; gap: 12px; font-size: 24px; font-weight: 600; color: #0E8F8A">{ico("check", "#0E8F8A", 26)}{H.escape(p["foot"])}</div></div>'''
    return frame(T, head(p["h"], T, size=74, mt=0) + panel, cta(T))

def t_myth(p, T):
    myth = f'''<div style="position: relative; margin-top: 110px; display: flex; flex-direction: column; gap: 14px">
<span style="display: flex; align-items: center; gap: 12px; font-family: {MONO}; font-size: 30px; font-weight: 700; letter-spacing: 3px; color: {T["sub"]}">{ico("cross", T["sub"], 32)}MYTH</span>
<span style="font-size: 92px; line-height: 1.08; font-weight: 700; letter-spacing: -3px; color: {T["fg"]}; opacity: 0.82; text-decoration: line-through; text-decoration-thickness: 5px; text-decoration-color: {NAVY if T is THEMES['grad'] else 'rgba(18,216,208,0.85)'}; text-wrap: balance">{H.escape(p["myth"])}</span></div>'''
    fact = f'''<div style="position: relative; margin-top: 80px; background: {T["card"]}; border-radius: 36px; padding: 48px 50px; display: flex; flex-direction: column; gap: 16px; box-shadow: 0 30px 60px -30px rgba(6,30,70,0.45)">
<span style="display: flex; align-items: center; gap: 14px; font-family: {MONO}; font-size: 26px; font-weight: 700; letter-spacing: 3px; color: #1670E0">{tile("check", "#12B5AE", 44, 24, 12)}FACT</span>
<span style="font-size: 44px; line-height: 1.36; font-weight: 600; color: {NAVY}">{H.escape(p["fact"])}</span></div>'''
    return frame(T, myth + fact, cta(T))

def t_number(p, T):
    ncol = WHITE if T is THEMES["grad"] else None
    nstyle = f"color: {WHITE}" if ncol else T["acc"]
    body = f'''<div style="position: relative; margin-top: 130px; font-size: {300 if len(p["n"])<=3 else 250}px; line-height: 0.95; font-weight: 700; letter-spacing: -12px; {nstyle}">{H.escape(p["n"])}</div>
<div style="position: relative; margin-top: 20px; font-size: 64px; line-height: 1.1; font-weight: 700; letter-spacing: -2px; color: {T["fg"]}">{H.escape(p["h"])}</div>''' + sub(p["sub"], T, size=36, mt=34)
    return frame(T, body, cta(T))

def t_list(p, T):
    rows = ""
    for i, it in enumerate(p["items"], 1):
        m = p["mark"]
        if m == "check": badge = tile("check", "#12B5AE", 52, 28, 16)
        elif m == "cross": badge = tile("cross", "#1670E0", 52, 28, 16)
        elif m == "box": badge = f'<span style="width: 46px; height: 46px; margin: 3px; border-radius: 12px; border: 4px solid #0BB2E0; flex-shrink: 0; box-sizing: border-box"></span>'
        else: badge = f'<span style="width: 52px; height: 52px; border-radius: 50%; background: {GRADH}; color: {WHITE}; display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: 700; flex-shrink: 0">{i}</span>'
        line = f'text-decoration: line-through; text-decoration-color: #0BB2E0; text-decoration-thickness: 3px' if m == "cross" else ""
        rows += f'<div style="display: flex; align-items: center; gap: 24px; padding: 22px 0; {"border-top: 2px solid #E3EBF2" if i>1 else ""}">{badge}<span style="font-size: 34px; line-height: 1.3; font-weight: 600; color: {NAVY}; {line}">{H.escape(it)}</span></div>'
    panel = f'<div style="position: relative; margin-top: 56px; background: {T["card"]}; border-radius: 36px; padding: 18px 44px; box-shadow: 0 30px 60px -30px rgba(6,30,70,0.45)">{rows}</div>'
    note = sub(p["note"], T, size=34, mt=36) if p.get("note") else ""
    return frame(T, head(p["h"], T, size=96, mt=70) + panel + note, cta(T))

def t_split(p, T):
    def col(label, text, good):
        bg = T["card"] if good else ("rgba(255,255,255,0.12)" if T["fg"]==WHITE else "#E1ECF2")
        fg = NAVY if good else T["fg"]
        lab = f'<span style="display: flex; align-items: center; gap: 12px; font-size: 26px; font-weight: 700; color: {"#1670E0" if good else T["sub"]}">{tile("check","#12B5AE",42,22,12) if good else tile("cross", "#6B7F93", 42, 22, 12)}{label}</span>'
        border = f"border: 4px solid transparent; background: linear-gradient({bg},{bg}) padding-box, {GRADH} border-box" if good else f"background: {bg}"
        return f'<div style="flex: 1; min-width: 0; border-radius: 34px; padding: 38px 34px; {border}; display: flex; flex-direction: column; gap: 26px; {"box-shadow: 0 30px 60px -30px rgba(6,30,70,0.5)" if good else ""}">{lab}<span style="font-size: 40px; line-height: 1.25; font-weight: 700; letter-spacing: -1px; color: {fg}">{H.escape(text)}</span></div>'
    body = (f'<span style="position: relative; margin-top: 110px; font-size: 30px; font-weight: 600; color: {T["sub"]}">The situation</span>'
            + head(p["sit"]+".", T, size=84, mt=12)
            + f'<div style="position: relative; margin-top: 60px; display: flex; gap: 24px; align-items: stretch">{col("Without Dynamo AI", p["no"], False)}{col("With Dynamo AI", p["yes"], True)}</div>')
    return frame(T, body, cta(T))

def t_question(p, T):
    opts = "".join(f'''<div style="display: flex; align-items: center; gap: 26px; padding: 24px 30px; border-radius: 26px; background: {T["card"]}; box-shadow: 0 20px 40px -26px rgba(6,30,70,0.45)">
<span style="width: 58px; height: 58px; border-radius: 16px; background: {GRADH}; color: {WHITE}; display: flex; align-items: center; justify-content: center; font-size: 30px; font-weight: 700; flex-shrink: 0">{L}</span>
<span style="font-size: 36px; font-weight: 600; color: {NAVY}">{H.escape(o)}</span></div>''' for L, o in zip("ABCD", p["opts"]))
    body = head(p["h"], T, size=88, mt=90) + f'<div style="position: relative; margin-top: 64px; display: flex; flex-direction: column; gap: 20px">{opts}</div>'
    foot = cta(T, "Comment A, B, C or D") + f'<span style="font-size: 26px; font-weight: 600; color: {T["sub"]}; text-align: right">dynamoasi.com</span>'
    return frame(T, body, foot)

def t_industry(p, T):
    rows = "".join(f'<div style="display: flex; align-items: center; gap: 22px">{tile("check", "#12B5AE", 48, 26, 14)}<span style="font-size: 36px; line-height: 1.3; font-weight: 600; color: {T["fg"]}">{H.escape(it)}</span></div>' for it in p["items"])
    body = (f'<div style="position: relative; margin-top: 96px; display: flex; align-items: center; gap: 24px">{tile(p["ico"], GRADH, 104, 54, 30)}<span style="font-size: 38px; font-weight: 700; color: {T["sub"]}">For {H.escape(p["ind"])}</span></div>'
            + head(p["h"], T, size=88, mt=40)
            + f'<div style="position: relative; margin-top: 60px; display: flex; flex-direction: column; gap: 30px">{rows}</div>')
    return frame(T, body, cta(T))

def t_tip(p, T):
    body = (f'<div style="position: relative; margin-top: 120px; display: flex; align-items: baseline; gap: 18px"><span style="font-size: 150px; line-height: 0.8; font-weight: 700; {T["acc"] if T is not THEMES["grad"] else f"color: {NAVY}"}">#{p["n"]}</span><span style="font-size: 34px; font-weight: 600; color: {T["sub"]}">Call tip</span></div>'
            + head(p["h"], T, size=84, mt=56) + sub(p["sub"], T, size=36, mt=36))
    foot = cta(T, "Save this for later") + f'<span style="font-size: 26px; font-weight: 600; color: {T["sub"]}; text-align: right">More tips at<br>@dynamo.asi</span>'
    return frame(T, body, foot)

TPL = dict(statement=t_statement, notif=t_notif, chat=t_chat, myth=t_myth, number=t_number,
           list=t_list, split=t_split, question=t_question, industry=t_industry, tip=t_tip)

def page(inner):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}} .bd>*:first-child{{margin-top:0!important}}</style></head><body>{inner}</body></html>'

async def main(only=None):
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, p in enumerate(POSTS, 1):
            if only and i not in only: continue
            T = THEMES[p["th"]]
            await pg.set_content(page(TPL[p["t"]](p, T)))
            await pg.wait_for_timeout(150)
            await pg.screenshot(path=f"/home/claude/batch/png/Dynamo-AI-Post-{i:02d}.png", clip={"x":0,"y":0,"width":1080,"height":1350})
        await b.close()

if __name__ == "__main__":
    only = {int(x) for x in sys.argv[1:]} or None
    asyncio.run(main(only))
    print("rendered")
