import asyncio
from playwright.async_api import async_playwright

async def site_personagens():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.techtudo.com.br/listas/2026/02/10-animes-em-que-o-protagonista-morre-mas-valem-a-pena-assistir-streaming.ghtml?utm_source=SaibaMaisMidArticle_Tech_Tudo&utm_content=TechTudo%252Fmagazine%252FTechTudo&interno_origem=mid-article-saiba-mais-techtudo",
                        wait_until="domcontentloaded", timeout=120000)
        page.set_default_timeout(timeout=120000)
        titulo = await page.title()
        print(titulo)
        await browser.close()
asyncio.run(site_personagens())