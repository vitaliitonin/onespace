import asyncio
from playwright.async_api import async_playwright

SCREENS_DIR = "research/screens"

TARGETS = [
    {
        "name": "megogo",
        "url": "https://megogo.net/ua",
        "actions": [
            {"type": "screenshot", "filename": "megogo-home.png"},
            {"type": "navigate", "url": "https://megogo.net/ua/search-extended.html"},
            {"type": "screenshot", "filename": "megogo-search.png"},
        ],
    },
    {
        "name": "kino_ua",
        "url": "https://kino.ua/ua/",
        "actions": [
            {"type": "screenshot", "filename": "kino-ua-home.png"},
        ],
    },
    {
        "name": "sweet_tv",
        "url": "https://sweet.tv/ua",
        "actions": [
            {"type": "screenshot", "filename": "sweet-tv-home.png"},
        ],
    },
    {
        "name": "filmix",
        "url": "https://filmix.my/",
        "actions": [
            {"type": "screenshot", "filename": "filmix-home.png"},
            {"type": "navigate", "url": "https://filmix.my/f/"},
            {"type": "screenshot", "filename": "filmix-catalog.png"},
        ],
    },
]


async def capture(playwright, target):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context(
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=True,
        locale="uk-UA",
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
    )
    page = await context.new_page()

    print(f"  → {target['name']}: opening {target['url']}")
    try:
        await page.goto(target["url"], wait_until="networkidle", timeout=30000)
    except Exception as e:
        print(f"  ✗ {target['name']} load error: {e}")
        await browser.close()
        return

    for action in target["actions"]:
        if action["type"] == "screenshot":
            path = f"{SCREENS_DIR}/{action['filename']}"
            await page.screenshot(path=path, full_page=False)
            print(f"  ✓ saved {path}")
        elif action["type"] == "navigate":
            try:
                await page.goto(action["url"], wait_until="networkidle", timeout=20000)
            except Exception as e:
                print(f"  ✗ navigate error: {e}")

    await browser.close()


async def main():
    async with async_playwright() as p:
        for target in TARGETS:
            print(f"\n[{target['name']}]")
            await capture(p, target)


asyncio.run(main())
