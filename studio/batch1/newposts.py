import sys, asyncio, html as H
sys.path.insert(0, "/home/claude/batch")
import build
from build import THEMES, frame, head, sub, cta, page, tile, ico, NAVY, SLATE, WHITE, GRADH

def says_does():
    T = THEMES["navy"]
    rows = [("“Price kya hai?”", "Shares your prices, from what you taught it", "note"),
            ("“Kal visit kar sakta hoon?”", "Books the visit and alerts your team", "check"),
            ("“Owner se baat karni hai.”", "Transfers the call to you, right away", "phone"),
            ("“Address bhej do.”", "Sends it on WhatsApp after the call", "chat")]
    R = "".join(f'''<div style="display:grid;grid-template-columns:1fr 64px 1fr;align-items:center;gap:18px">
<div style="padding:24px 26px;border-radius:26px 26px 26px 8px;background:rgba(255,255,255,0.10);border:2px solid rgba(255,255,255,0.14);font-size:30px;font-weight:600;line-height:1.3">{a}</div>
<div style="display:flex;justify-content:center">{ico("check", "#3FE6F0", 34) if False else '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#3FE6F0" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'}</div>
<div style="display:flex;align-items:center;gap:16px;padding:20px 22px;border-radius:26px;background:#FFFFFF;color:{NAVY}">{tile(i, None, 54, 28, 16)}<span style="font-size:27px;font-weight:600;line-height:1.3">{b}</span></div></div>''' for a, b, i in rows)
    lab = f'<div style="display:grid;grid-template-columns:1fr 64px 1fr;gap:18px;font-size:24px;font-weight:700;letter-spacing:1px;color:{T["sub"]}"><span>Caller says</span><span></span><span>Dynamo AI does</span></div>'
    body = head("Your callers talk.|Dynamo AI acts.", T, size=86, mt=0) + f'<div style="position:relative;margin-top:60px;display:flex;flex-direction:column;gap:24px">{lab}{R}</div>'
    return frame(T, body, cta(T))

def day_in_life():
    T = THEMES["light"]
    ev = [("8:02 AM", "Clinic appointment request", "Saved, front desk alerted"),
          ("1:15 PM", "New lead from your Instagram ad", "Called back within a minute"),
          ("6:40 PM", "Customer ready to buy", "Transferred to your sales team"),
          ("11:30 PM", "Price enquiry after closing", "Answered, details on WhatsApp"),
          ("3:10 AM", "Late-night caller", "Answered on the first ring")]
    R = "".join(f'''<div style="display:grid;grid-template-columns:200px 36px 1fr;gap:22px;align-items:start">
<span style="font-size:32px;font-weight:700;color:#1670E0;padding-top:6px;text-align:right">{t}</span>
<span style="display:flex;flex-direction:column;align-items:center;height:100%"><span style="width:28px;height:28px;border-radius:50%;background:{GRADH};margin-top:12px;box-shadow:0 0 0 8px rgba(18,216,208,.18)"></span>{"" if k == len(ev) - 1 else '<span style="flex:1;width:4px;background:#C9DCE6;margin-top:8px"></span>'}</span>
<div style="padding-bottom:30px"><div style="font-size:36px;font-weight:700;color:{NAVY};line-height:1.2">{a}</div><div style="font-size:28px;color:{SLATE};margin-top:6px">{b}</div></div></div>''' for k, (t, a, b) in enumerate(ev))
    body = head("A day in the life of|your AI receptionist.", T, size=80, mt=0) + f'<div style="position:relative;margin-top:56px;background:#FFFFFF;border-radius:36px;padding:44px 40px 14px;box-shadow:0 30px 60px -30px rgba(6,30,70,0.35)">{R}</div>'
    return frame(T, body, cta(T, "Hire yours · dynamoasi.com/app"))

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for name, fn in [("Day1-Post", says_does), ("Day2-Post", day_in_life)]:
            await pg.set_content(page(fn())); await pg.wait_for_timeout(200)
            await pg.screenshot(path=f"/home/claude/batch1/Dynamo-AI-{name}.png", clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        await b.close()
asyncio.run(main()); print("ok")
