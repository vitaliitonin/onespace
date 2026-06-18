import asyncio
from playwright.async_api import async_playwright

SCREENS_DIR = "research/screens"

TARGETS = [
    {
        "name": "imdb_search",
        "url": "https://www.imdb.com/search/title/?title_type=feature,tv_series&genres=action&user_rating=7.0,&sort=user_rating,desc",
        "wait": 4000,
        "filename": "imdb-advanced-search.png",
    },
    {
        "name": "justwatch_discover",
        "url": "https://www.justwatch.com/us/movies?genres=act&min_rating=70&sort_by=popular",
        "wait": 4000,
        "filename": "justwatch-discover.png",
    },
    {
        "name": "tmdb_discover",
        "url": "https://www.themoviedb.org/discover/movie?sort_by=vote_average.desc&vote_count.gte=500",
        "wait": 4000,
        "filename": "tmdb-discover.png",
    },
    {
        "name": "imdb_home",
        "url": "https://www.imdb.com/",
        "wait": 3000,
        "filename": "imdb-home.png",
    },
]


async def capture(playwright, target):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context(
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=True,
        locale="en-US",
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
    )
    page = await context.new_page()
    print(f"  → {target['name']}: {target['url']}")
    try:
        await page.goto(target["url"], wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(target["wait"])
        path = f"{SCREENS_DIR}/{target['filename']}"
        await page.screenshot(path=path, full_page=False)
        print(f"  ✓ {path}")
    except Exception as e:
        print(f"  ✗ {target['name']}: {e}")
    await browser.close()


async def main():
    async with async_playwright() as p:
        for t in TARGETS:
            await capture(p, t)


asyncio.run(main())
