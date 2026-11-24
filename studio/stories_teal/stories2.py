import sys
from playwright.sync_api import sync_playwright
from brand import *
OUT = S / "out"; OUT.mkdir(parents=True, exist_ok=True)
BGS = {"ink": (INK, "#FFFFFF"), "gold": ("linear-gradient(160deg,#12D8D0 0%,#0BB2E0 45%,#1670E0 100%)", "#FFFFFF"), "warm": (WARM, INK)}
CSS = f"body{{margin:0}}*{{box-sizing:border-box}}.gt{{{GT}}}.mono{{font-family:'DejaVu Sans Mono',monospace}}.em{{font-family:'Noto Color Emoji'}}"

def story(bg, tag, h1, body, foot="", uid="s", hsize=104, top=330):
    b, tx = BGS[bg]
    sub = G3 if bg == "ink" else ("rgba(255,255,255,.85)" if bg == "gold" else G2)
    glow = f'<div style="position:absolute;right:-300px;top:-200px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(18,216,208,.20),transparent 65%)"></div>' if bg == "ink" else ""
    wm = wordmark(30, bg == "ink", uid) if bg != "gold" else f'<div style="display:flex;align-items:center;gap:16px">{logo(56, uid, "#FFFFFF")}<div style="display:flex;align-items:center;gap:13px">{dword(22, "#FFFFFF")}<span style="font-size:30px;font-weight:700;letter-spacing:6px;line-height:1;color:#FFFFFF;opacity:.7">AI</span></div></div>'
    chipc = "#24405C" if bg == "ink" else ("rgba(255,255,255,.45)" if bg == "gold" else "#C9DCE6")
    return f'''<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div style="width:1080px;height:1920px;background:{b};color:{tx};font-family:Poppins,sans-serif;position:relative;overflow:hidden">{glow}
<div style="position:absolute;left:84px;right:84px;top:210px;display:flex;align-items:center;justify-content:space-between">{wm}<span style="padding:10px 22px;border-radius:999px;border:2px solid {chipc};font-size:21px;font-weight:700;letter-spacing:4px;color:{sub}">{tag}</span></div>
<h1 style="position:absolute;left:84px;right:84px;top:{top}px;margin:0;font-size:{hsize}px;line-height:1.04;letter-spacing:-3.5px;font-weight:700">{h1}</h1>
{body}
{foot}
</div></body></html>'''

def cta(text, bg="ink", y=1560):
    if bg == "gold": s = f"background:{INK};color:#fff"
    else: s = f"background:{GRAD};color:{INK}"
    return f'<div style="position:absolute;left:0;right:0;top:{y}px;display:flex;justify-content:center"><span style="padding:28px 50px;border-radius:999px;{s};font-size:36px;font-weight:700">{text}</span></div>'
def nxt(bg="ink", y=1600):
    c = G3 if bg == "ink" else ("rgba(255,255,255,.85)" if bg == "gold" else G2)
    return f'<div style="position:absolute;left:0;right:0;top:{y}px;text-align:center;font-size:26px;font-weight:600;color:{c};letter-spacing:2px">TAP FOR NEXT →</div>'
def at(x, y, html, w=None):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;{f"width:{w}px;" if w else ""}">{html}</div>'
PH = lambda c, s=40, r=0: f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" style="transform:rotate({r}deg);flex-shrink:0"><path d="M5 4 H8.5 L10.5 9 L8.2 10.4 A11 11 0 0 0 13.6 15.8 L15 13.5 L20 15.5 V19 A2 2 0 0 1 18 21 A15 15 0 0 1 3 6 A2 2 0 0 1 5 4 Z" fill="{c}"/></svg>'
def tick(s=40):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" style="flex-shrink:0"><defs><linearGradient id="tk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#12D8D0"/><stop offset="1" stop-color="#1670E0"/></linearGradient></defs><circle cx="12" cy="12" r="11" fill="url(#tk)"/><path d="M7.5 12.5 L10.5 15.5 L16.5 9" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def phone(inner, w=560, h=1000, x=260, y=560, light=False):
    return at(x, y, f'<div style="width:{w}px;height:{h}px;border-radius:84px;background:#0A0A0A;padding:18px;box-shadow:0 60px 120px rgba(0,0,0,.45),0 0 0 3px #2B2B2B"><div style="position:relative;width:100%;height:100%;border-radius:68px;overflow:hidden;background:{"#F3F8FB" if light else "#0F2133"}"><div style="position:absolute;left:50%;top:18px;width:150px;height:40px;margin-left:-75px;border-radius:20px;background:#000;z-index:3"></div>{inner}</div></div>')
def bars(n=28, col=AMBER, h=90):
    import math
    return '<div style="display:flex;align-items:center;gap:7px;height:%dpx">' % h + "".join(f'<i style="display:block;width:9px;border-radius:5px;height:{int(h*(.25+.75*abs(math.sin(i*1.7)*math.cos(i*.6))))}px;background:{col}"></i>' for i in range(n)) + "</div>"
def bub(who, t, me, dark=True, size=34, maxw=760):
    bg = (GRAD if me else CHAR2) if dark else ("#FFFFFF" if not me else INK)
    col = (INK if me else "#fff") if dark else (INK if not me else "#fff")
    lab = ("#063A5C" if me else G3) if dark else (AMBER if me else G3)
    return f'<div style="display:flex;justify-content:{"flex-end" if me else "flex-start"};margin-bottom:20px"><div style="max-width:{maxw}px;padding:26px 32px;border-radius:{"34px 34px 8px 34px" if me else "34px 34px 34px 8px"};background:{bg};color:{col};font-size:{size}px;font-weight:500;line-height:1.35;{"box-shadow:0 16px 34px rgba(10,40,70,.10);" if not dark else ""}"><div style="font-size:19px;font-weight:700;letter-spacing:.14em;color:{lab};margin-bottom:6px">{who}</div>{t}</div></div>'

ST = []
# ---------------- DEMO ----------------
call = (f'<div style="position:absolute;inset:0;background:radial-gradient(600px 500px at 50% 30%,#123A4F,#0F2133 70%)"></div>'
        f'<div style="position:absolute;left:0;right:0;top:120px;display:flex;flex-direction:column;align-items:center;color:#fff">'
        f'<div style="width:190px;height:190px;border-radius:50%;background:{CHAR2};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 14px rgba(18,216,208,.14),0 0 0 30px rgba(18,216,208,.07)">{logo(110, "dc")}</div>'
        f'<div style="margin-top:44px;font-size:52px;font-weight:700">Dynamo AI</div><div class="mono" style="margin-top:8px;font-size:26px;color:{AMBER}">● On call · 00:12</div>'
        f'<div style="margin-top:44px">{bars(26)}</div>'
        f'<div style="margin-top:40px;padding:22px 30px;border-radius:28px;background:{CHAR2};font-size:26px;line-height:1.35;max-width:440px">“Namaste! Main Dynamo bol rahi hoon. Bataiye, kaise madad karoon?”</div></div>'
        f'<div style="position:absolute;left:0;right:0;bottom:44px;display:flex;justify-content:center;gap:90px"><span style="width:110px;height:110px;border-radius:50%;background:#1B3149;display:flex;align-items:center;justify-content:center">{PH("#fff", 44)}</span><span style="width:110px;height:110px;border-radius:50%;background:#E5484D;display:flex;align-items:center;justify-content:center">{PH("#fff", 44, 135)}</span></div>')
ST.append(("Demo", 1, story("ink", "DEMO", 'Hear Dynamo<br><span class="gt">answer a call.</span>', phone(call, 560, 1000, 260, 600), cta("Tap the link · Book a demo", "ink", 1650), "d1")))
steps = [("1", "Send “DEMO” on WhatsApp", "Tap the link or message +91 95096 84181."), ("2", "Tell us your business", "Real estate, clinic, dealer, coaching, anything."), ("3", "Talk to Dynamo", "Call it like your customer would, in Hindi, English or a regional language.")]
sh = "".join(f'<div style="display:flex;gap:34px;align-items:flex-start;padding:40px 44px;border-radius:40px;background:{"#FFFFFF" if True else CHAR};margin-bottom:24px;box-shadow:0 18px 40px rgba(10,40,70,.10)"><span class="gt" style="font-size:120px;font-weight:700;line-height:.85;width:80px">{n}</span><div><div style="font-size:44px;font-weight:700;line-height:1.15">{a}</div><div style="font-size:30px;color:{G2};margin-top:10px;line-height:1.35">{b}</div></div></div>' for n, a, b in steps)
ST.append(("Demo", 2, story("warm", "DEMO", 'How the demo<br><span class="gt">works.</span>', at(84, 640, sh, 912), cta("DM “DEMO” to start", "warm", 1620), "d2")))
# ---------------- FEATURES ----------------
f1 = (f'<div style="position:absolute;left:0;right:0;top:120px;text-align:center;color:{G3};font-size:26px" class="mono">9:47 PM · Office closed</div>'
      f'<div style="position:absolute;left:40px;right:40px;top:200px;padding:34px;border-radius:44px;background:{CHAR2}"><div style="display:flex;align-items:center;gap:22px"><span style="width:90px;height:90px;border-radius:50%;background:#2FB45A;display:flex;align-items:center;justify-content:center">{PH("#fff", 44)}</span><div style="color:#fff"><div style="font-size:24px;color:{G3}">Incoming call</div><div style="font-size:38px;font-weight:700">+91 98290 •••••</div></div></div></div>'
      f'<div style="position:absolute;left:0;right:0;top:470px;text-align:center;font-size:60px;color:{AMBER}">↓</div>'
      f'<div style="position:absolute;left:40px;right:40px;top:580px;padding:34px;border-radius:44px;background:{GRAD}"><div style="display:flex;align-items:center;gap:22px"><span style="width:90px;height:90px;border-radius:50%;background:{INK};display:flex;align-items:center;justify-content:center">{logo(52, "f1")}</span><div style="color:{INK}"><div style="font-size:24px;font-weight:600">Answered by Dynamo</div><div style="font-size:38px;font-weight:700">First ring · 0:01</div></div></div></div>')
ST.append(("Features", 1, story("ink", "FEATURES · 1/5", 'Picks up on the<br><span class="gt">first ring.</span>', phone(f1, 560, 1000, 260, 600) + "", nxt("ink", 1660), "f1")))
f2 = (f'<div style="position:absolute;left:84px;right:84px;top:620px;padding:36px 40px;border-radius:40px;background:#fff;color:{INK};box-shadow:0 30px 60px rgba(0,0,0,.25)"><div style="font-size:24px;color:{G3};font-weight:700;letter-spacing:.1em">NEW ENQUIRY · INSTAGRAM AD · NOW</div><div style="font-size:46px;font-weight:700;margin-top:8px">Rohan · 3BHK · Whitefield</div></div>'
      f'<div style="position:absolute;left:0;right:0;top:880px;text-align:center"><div class="mono gt" style="font-size:250px;font-weight:700;letter-spacing:-8px;line-height:1">00:38</div><div style="margin-top:10px;display:inline-flex;align-items:center;gap:16px;padding:20px 34px;border-radius:999px;background:{CHAR};font-size:34px;font-weight:600">{PH(AMBER, 36)} Dynamo is calling Rohan</div></div>'
      f'<div style="position:absolute;left:84px;right:84px;top:1330px;display:flex;flex-direction:column;gap:18px">' + "".join(f'<div style="display:flex;align-items:center;gap:20px;font-size:34px;font-weight:600">{tick()}{t}</div>' for t in ["Asks budget, location and timeline", "Books the site visit or callback"]) + '</div>')
ST.append(("Features", 2, story("ink", "FEATURES · 2/5", 'Calls new leads<br><span class="gt">within a minute.</span>', f2, nxt("ink", 1660), "f2")))
node = lambda ic, lab, hi=False: f'<div style="display:flex;flex-direction:column;align-items:center;gap:18px"><div style="width:190px;height:190px;border-radius:50%;background:{INK if hi else "#FFFFFF"};display:flex;align-items:center;justify-content:center;box-shadow:0 20px 40px rgba(6,40,80,.22)">{ic}</div><span style="font-size:32px;font-weight:700">{lab}</span></div>'
USER = f'<svg width="84" height="84" viewBox="0 0 24 24" fill="none" stroke="{INK}" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>'
TEAM = f'<svg width="90" height="90" viewBox="0 0 24 24" fill="none" stroke="{INK}" stroke-width="1.8"><circle cx="9" cy="8" r="3.4"/><circle cx="17" cy="9" r="2.6"/><path d="M2.5 20c1-3.6 3.6-5.4 6.5-5.4s5.5 1.8 6.5 5.4M15 14.6c2.6 0 4.9 1.5 6 4.6"/></svg>'
dash = f'<div style="flex:1;height:5px;margin:0 6px 60px;background:repeating-linear-gradient(90deg,{INK} 0 16px,transparent 16px 30px);opacity:.6"></div>'
f3 = (at(84, 680, f'<div style="display:flex;align-items:center;width:912px">{node(USER, "Customer")}{dash}{node(logo(110, "f3"), "Dynamo", True)}{dash}{node(TEAM, "Your team")}</div>')
      + at(84, 1040, bub("CUSTOMER", "Kya main kisi person se baat kar sakta hoon?", False, False, 34, 820) + bub("DYNAMO", "Bilkul! Abhi aapko hamari team se connect kar rahi hoon.", True, False, 34, 820), 912))
ST.append(("Features", 3, story("gold", "FEATURES · 3/5", "Hands over to<br>your team.", f3, nxt("gold", 1660), "f3")))
wa = (f'<div style="position:absolute;left:0;right:0;top:0;height:200px;background:#075E54;display:flex;align-items:flex-end;padding:0 34px 26px;gap:20px;color:#fff"><span style="width:76px;height:76px;border-radius:50%;background:{INK};display:flex;align-items:center;justify-content:center">{logo(44, "wa")}</span><div><div style="font-size:34px;font-weight:700">Dynamo AI</div><div style="font-size:22px;opacity:.8">online</div></div></div>'
      f'<div style="position:absolute;left:0;right:0;top:200px;bottom:0;background:#ECE5DD;padding:40px 30px">'
      f'<div style="background:#fff;border-radius:30px 30px 30px 8px;padding:26px 30px;font-size:30px;line-height:1.4;color:{INK};max-width:440px">Hi Rohan, thanks for calling! 🙏<br><br>Site visit: <b>Sat, 11 AM</b><br>Location pin and brochure below.<div style="text-align:right;font-size:20px;color:{G3}">9:49 PM ✓✓</div></div>'
      f'<div style="margin-top:22px;background:#fff;border-radius:30px;padding:22px 26px;display:flex;gap:18px;align-items:center;max-width:440px"><span style="width:70px;height:80px;border-radius:12px;background:#E5484D;color:#fff;font-weight:800;font-size:22px;display:flex;align-items:center;justify-content:center">PDF</span><div style="font-size:26px;font-weight:600;color:{INK}">Project-Brochure.pdf</div></div></div>')
ST.append(("Features", 4, story("ink", "FEATURES · 4/5", 'Follows up on<br><span class="gt">WhatsApp.</span>', phone(wa, 560, 1000, 260, 600) + "", nxt("ink", 1660), "f4")))
crm_rows = [("Name", "Rohan Sharma"), ("Interest", "3BHK · Whitefield"), ("Budget", "₹1.2 Cr"), ("Next step", "Site visit · Sat 11 AM"), ("Language", "Hindi")]
crm = "".join(f'<div style="display:flex;justify-content:space-between;padding:22px 0;{"border-top:2px solid #E1ECF2;" if i else ""}font-size:32px"><span style="color:{G2}">{a}</span><b>{b}</b></div>' for i, (a, b) in enumerate(crm_rows))
f5 = at(84, 640, f'<div style="padding:40px 44px;border-radius:44px;background:#fff;box-shadow:0 24px 50px rgba(10,40,70,.12)"><div style="display:flex;align-items:center;justify-content:space-between"><span class="mono" style="font-size:24px;color:{G3};letter-spacing:.12em">CALL SUMMARY · 2:14</span><span style="padding:12px 24px;border-radius:999px;background:{GRAD};font-size:26px;font-weight:700">Saved to CRM</span></div><div style="margin-top:20px">{crm}</div>'
             f'<div style="margin-top:20px;padding:26px 30px;border-radius:28px;background:{CARD};font-size:28px;line-height:1.45;color:{G1}">“Wants a 3BHK near Whitefield, budget ₹1.2 Cr, ready to visit this weekend.”</div></div>', 912)
ST.append(("Features", 5, story("warm", "FEATURES · 5/5", 'Every call,<br><span class="gt">summarised.</span>', f5, cta("DM “DEMO” to see it live", "warm", 1640), "f5")))
# ---------------- PRICING ----------------
p1 = (at(0, 600, f'<div style="text-align:center;font-size:520px;font-weight:700;letter-spacing:-30px;line-height:1;color:#FFFFFF">₹4</div>', 1080)
      + at(0, 1150, f'<div style="text-align:center;font-size:64px;font-weight:700">per minute of call time</div><div style="margin-top:40px;display:flex;justify-content:center;gap:16px">' + "".join(f'<span style="padding:16px 28px;border-radius:999px;background:{INK};color:#fff;font-size:30px;font-weight:600">{t}</span>' for t in ["No salary", "No seat fee", "Setup included"]) + '</div>', 1080))
ST.append(("Pricing", 1, story("gold", "PRICING · 1/3", "Simple pricing.", p1, nxt("gold", 1660), "p1")))
rows = [("100 min", "₹400"), ("500 min", "₹2,000"), ("1,000 min", "₹4,000"), ("5,000 min", "₹20,000")]
tbl = "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:34px 0;{"border-top:2px solid #24405C;" if i else ""}"><span style="font-size:46px;font-weight:600">{a}</span><span class="gt" style="font-size:64px;font-weight:700;letter-spacing:-1px">{b}</span></div>' for i, (a, b) in enumerate(rows))
ST.append(("Pricing", 2, story("ink", "PRICING · 2/3", 'What it costs<br><span class="gt">each month.</span>', at(84, 650, f'<div style="padding:10px 50px;border-radius:44px;background:{CHAR}">{tbl}</div><div style="margin-top:30px;font-size:28px;color:{G3}">Example figures at ₹4 per minute. Your quote depends on your call volume.</div>', 912), nxt("ink", 1660), "p2")))
cmp = [("Hours", "Office hours", "24×7"), ("Cost", "Fixed salary", "₹4 / min"), ("New leads", "When free", "In a minute"), ("Follow-ups", "From memory", "Every call"), ("Records", "Notes, if any", "Recording + CRM")]
ct = (f'<div style="display:grid;grid-template-columns:1.1fr 1fr 1fr;border-radius:44px;overflow:hidden;background:#fff;box-shadow:0 24px 50px rgba(10,40,70,.12)">'
      f'<div style="padding:30px 32px"></div><div style="padding:30px 20px;font-size:24px;font-weight:700;color:{G3};letter-spacing:.08em">TELECALLER</div><div style="padding:30px 20px;background:{INK};font-size:24px;font-weight:700;letter-spacing:.08em" class="gt">DYNAMO</div>'
      + "".join(f'<div style="padding:30px 32px;border-top:2px solid #E1ECF2;font-size:30px;font-weight:700">{a}</div><div style="padding:30px 20px;border-top:2px solid #E1ECF2;font-size:28px;color:{G2}">{b}</div><div style="padding:30px 20px;background:{INK};color:#fff;font-size:28px;font-weight:600;border-top:2px solid #22384F">{c}</div>' for a, b, c in cmp) + '</div>')
ST.append(("Pricing", 3, story("warm", "PRICING · 3/3", 'Hire a caller,<br><span class="gt">or hire Dynamo?</span>', at(84, 640, ct, 912), cta("DM “DEMO” for a quote", "warm", 1640), "p3")))
# ---------------- LANGUAGES ----------------
l1 = at(84, 620, bub("CALLER · HINDI", "नमस्ते, ये फ्लैट अभी available है?", False) + bub("DYNAMO", "जी हाँ! आप visit कब करना चाहेंगे?", True) + bub("CALLER · ENGLISH", "What are your clinic timings today?", False) + bub("DYNAMO", "We're open till 8 PM. Shall I book a slot?", True) + bub("CALLER · HINDI", "Price thoda kam ho sakta hai kya?", False) + bub("DYNAMO", "Main aapki baat sales team tak pahuncha deti hoon.", True), 912)
ST.append(("Languages", 1, story("ink", "LANGUAGES · 1/2", 'Talks the way<br><span class="gt">callers talk.</span>', l1, nxt("ink", 1700), "l1")))
lc = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:40px 44px;border-radius:40px;background:{INK};color:#fff;margin-bottom:22px"><div><div style="font-size:60px;font-weight:700;line-height:1.1">{a}</div><div style="font-size:28px;color:{G3};margin-top:6px">{b}</div></div><span style="font-size:72px;font-weight:700" class="gt">{c}</span></div>' for a, b, c in [("Hindi", "For callers who prefer Hindi", "अ"), ("English", "For English-speaking callers", "A"), ("Regional", "Ask us about your callers' language", "भा")])
ST.append(("Languages", 2, story("gold", "LANGUAGES · 2/2", "Your caller picks<br>the language.", at(84, 660, lc, 912), cta("DM “DEMO” to hear it", "gold", 1620), "l2")))
# ---------------- 24x7 ----------------
night = [("9:42 PM", "Incoming enquiry", "Answered"), ("11:18 PM", "New website lead", "Called in 40s"), ("2:06 AM", "Pricing question", "Lead qualified"), ("6:55 AM", "Follow-up call", "Saved to CRM")]
nt = "".join(f'<div style="display:flex;gap:30px;align-items:flex-start"><div style="display:flex;flex-direction:column;align-items:center"><span style="width:30px;height:30px;border-radius:50%;background:{GRAD};margin-top:12px;box-shadow:0 0 0 8px rgba(18,216,208,.16)"></span>{"" if i == 3 else f"""<span style="width:3px;height:120px;background:#24405C"></span>"""}</div><div><div class="mono" style="font-size:30px;color:{AMBER};font-weight:700">{a}</div><div style="font-size:46px;font-weight:700;margin-top:4px">{b}</div><div style="display:inline-block;margin-top:12px;padding:10px 22px;border-radius:999px;background:{CHAR2};font-size:26px;color:{G4};font-weight:600">{c}</div></div></div>' for i, (a, b, c) in enumerate(night))
moon = '<div style="position:absolute;right:90px;top:560px;width:150px;height:150px;border-radius:50%;box-shadow:-34px 18px 0 0 #12D8D0;transform:rotate(-20deg)"></div>'
ST.append(("24x7", 1, story("ink", "24×7 · 1/2", 'Your office closes.<br><span class="gt">Dynamo doesn\'t.</span>', moon + at(84, 690, nt, 912), nxt("ink", 1700), "n1", hsize=96)))
cal = "".join(f'<div style="padding:34px 20px;border-radius:36px;background:{INK if hi else "#FFFFFF"};color:{"#fff" if hi else INK};text-align:center;box-shadow:0 18px 40px rgba(6,40,80,.18)"><div style="font-size:24px;font-weight:700;letter-spacing:.12em;color:{AMBER if hi else G3}">{d}</div><div style="font-size:40px;font-weight:700;margin-top:10px;line-height:1.15">{n}</div><div style="margin-top:16px;font-size:24px;font-weight:600">✓ Answered</div></div>' for d, n, hi in [("SUNDAY", "Weekend<br>enquiries", False), ("DIWALI", "Festive<br>rush", True), ("3 AM", "Late-night<br>callers", True), ("LUNCH", "Busy<br>front desk", False)])
ST.append(("24x7", 2, story("gold", "24×7 · 2/2", "No leave.<br>No sick days.", at(84, 660, f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{cal}</div>', 912), cta("DM “DEMO”", "gold", 1620), "n2")))
# ---------------- FAQ ----------------
FQ = [("What is Dynamo AI?", "An AI calling agent for Indian businesses. It answers your calls, calls your leads, follows up on WhatsApp and updates your CRM."),
      ("Will callers know it's AI?", "It sounds natural and introduces itself as your AI assistant. We recommend being upfront, and set it up that way by default."),
      ("How long does setup take?", "We learn how your business handles calls, build your agent and test it with you before it goes live. No tech team needed."),
      ("What if it can't answer?", "It's trained on your information. Beyond that, it takes the caller's details or transfers the call to your team."),
      ("Are calls recorded?", "Yes, so you can review any call. Callers are told calls may be recorded, and you can ask us to delete your data anytime."),
      ("How much does it cost?", "₹4 for every minute Dynamo is on a call. No salary, no seat fee. Send DEMO for a quote for your call volume.")]
for i, (q, a) in enumerate(FQ, 1):
    bg = "ink" if i % 2 else "warm"
    qcol = "#fff" if bg == "ink" else INK; acol = G4 if bg == "ink" else G1
    wm = f'<div style="position:absolute;right:-60px;bottom:120px;font-size:900px;font-weight:700;line-height:1;opacity:{.10 if bg == "ink" else .14};{GT}">?</div>'
    body = wm + at(84, 600, f'<div style="font-size:30px;font-weight:700;letter-spacing:.14em" class="gt">QUESTION {i} / {len(FQ)}</div><div style="font-size:100px;font-weight:700;letter-spacing:-3.5px;line-height:1.04;margin-top:20px;color:{qcol}">{q}</div>'
                   f'<div style="margin-top:60px;padding:46px 48px;border-radius:44px;background:{CHAR if bg == "ink" else "#FFFFFF"};{"box-shadow:0 24px 50px rgba(10,40,70,.10);" if bg == "warm" else ""}font-size:44px;line-height:1.45;color:{acol}">{a}</div>', 912)
    foot = cta("Ask us anything · DM", bg, 1640) if i == len(FQ) else nxt(bg, 1700)
    ST.append(("FAQ", i, story(bg, "FAQ", "", body, foot, f"q{i}")))

if __name__ == "__main__":
    only = sys.argv[1:]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for hl, n, html in ST:
            if only and hl not in only: continue
            pg.set_content(html); pg.wait_for_timeout(220)
            pg.screenshot(path=str(OUT / f"Dynamo-AI-Story-{hl}-{n}.jpg"), type="jpeg", quality=92)
        b.close()
    print(len(ST))
