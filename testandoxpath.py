import asyncio
import json
from pymongo import MongoClient

async def coletando_precos_localiza_seminovos():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://napista.com.br/anuncios/28a32b72-1642-4f57-b2e6-a03c0e2f78f1",
            wait_until="load", timeout=60000)
        page.set_default_timeout(timeout=60000)
        price =  await page.locator("//div[contains(text(),'km')]").inner_text()
        print(price)

asyncio.run(coletando_precos_localiza_seminovos())
