import sys, asyncio
sys.path.insert(0, "/home/claude/batch")
import build
from build import THEMES, frame, head, sub, cta, page, tile, ico, NAVY, SLATE, WHITE, GRADH, GRAD

def plan_math():
    T = THEMES["grad"]
    rows = [("2,000 minutes", "of calls answered, at ₹4 a minute"), ("+ 200 minutes free", "10% extra on 2,000+ minute plans"),
            ("₹0 salary", "no seat fee, no leave, no notice period")]
    R = "".join(f'''<div style="display:flex;align-items:baseline;justify-content:space-between;gap:24px;padding:26px 0;border-bottom:2px solid #E3EBF2">
<span style="font-size:44px;font-weight:700;color:{'#1670E0' if k == 1 else NAVY};white-space:nowrap">{a}</span><span style="font-size:27px;color:{SLATE};text-align:right;line-height:1.3">{b}</span></div>''' for k, (a, b) in enumerate(rows))
    big = (f'<div style="position:relative;margin-top:10px;font-size:190px;font-weight:700;letter-spacing:-8px;line-height:1;color:#fff">₹8,000</div>'
           f'<div style="position:relative;font-size:46px;font-weight:600;color:rgba(255,255,255,.95);margin-top:8px">gets your business:</div>')
    card = f'<div style="position:relative;margin-top:46px;background:#fff;border-radius:36px;padding:20px 44px 18px;box-shadow:0 30px 60px -30px rgba(6,30,70,.45)">{R}</div>'
    note = f'<div style="position:relative;margin-top:26px;font-size:26px;font-weight:500;color:rgba(255,255,255,.9)">Plans start at 2,000 minutes. Answers 24×7, on the first ring.</div>'
    return frame(T, big + card + note, cta(T))

def myth_fact():
    T = THEMES["navy"]
    rows = [("AI calling is only for big companies.", "₹4 a minute. No salary, no seat fee. Built for small and growing businesses."),
            ("I'd need a tech team to set it up.", "The Dynamo team sets it up and tests it before it goes live."),
            ("My customers speak Hindi, not English.", "Dynamo AI talks in Hindi, English and regional languages."),
            ("AI can't handle a customer who wants a person.", "It transfers the call to you or your team, mid-call.")]
    R = "".join(f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div style="display:flex;gap:16px;align-items:flex-start;padding:24px 24px;border-radius:26px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.12)">
<span style="flex-shrink:0;margin-top:2px">{ico("cross", "#FF8A8A", 30)}</span><span style="font-size:27px;font-weight:600;line-height:1.3;color:rgba(255,255,255,.8);text-decoration:line-through;text-decoration-color:rgba(255,138,138,.7)">{m}</span></div>
<div style="display:flex;gap:16px;align-items:flex-start;padding:24px 24px;border-radius:26px;background:#fff">
<span style="flex-shrink:0;margin-top:2px">{ico("check", "#12B5AE", 30)}</span><span style="font-size:27px;font-weight:600;line-height:1.3;color:{NAVY}">{f}</span></div></div>''' for m, f in rows)
    lab = f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;font-size:24px;font-weight:700;letter-spacing:1px;color:{T["sub"]}"><span>Myth</span><span>Fact</span></div>'
    body = head("4 myths about|AI receptionists.", T, size=84, mt=0) + f'<div style="position:relative;margin-top:50px;display:flex;flex-direction:column;gap:18px">{lab}{R}</div>'
    return frame(T, body, cta(T))

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for name, fn in [("Day3-Post", plan_math), ("Day4-Post", myth_fact)]:
            await pg.set_content(page(fn())); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"/home/claude/batch1/Dynamo-AI-{name}.png", clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        await b.close()
asyncio.run(main()); print("ok")
