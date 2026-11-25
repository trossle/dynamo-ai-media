import asyncio, subprocess, os
from playwright.async_api import async_playwright
FPS=30
SCENES=[(0, 173), (173, 323), (323, 468), (468, 597), (597, 835), (835, 986), (986, 1224), (1224, 1353)]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto("file:///home/claude/reel17/reel_built.html"); await pg.wait_for_timeout(1000)
        for k,(a,z) in enumerate(SCENES):
            if os.path.exists(f"scene{k}.mp4"): continue
            tmp=f"scene{k}.tmp.mp4"
            ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
                "-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r",str(FPS),tmp],stdin=subprocess.PIPE)
            for f in range(a,z):
                await pg.evaluate(f"render({f/FPS},{f})")
                ff.stdin.write(await pg.screenshot(type="jpeg",quality=92))
            ff.stdin.close()
            if ff.wait()==0: os.replace(tmp,f"scene{k}.mp4"); print("scene",k,"ok",flush=True)
        await b.close()
asyncio.run(main())
