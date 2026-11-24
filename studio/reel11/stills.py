import asyncio,sys
from playwright.async_api import async_playwright
ts=[float(x) for x in sys.argv[1:]]
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto("file:///home/claude/reel11/reel_built.html"); await pg.wait_for_timeout(800)
        for t in ts:
            await pg.evaluate(f"render({t},{int(t*30)})")
            await pg.screenshot(path=f"/tmp/st_{t}.jpg",type="jpeg",quality=80)
        await b.close()
asyncio.run(m())
