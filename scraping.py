import asyncio
from playwright.async_api import async_playwright
import regex as re

async def site_personagens():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?utm_source=%20&utm_medium=cpc&utm_campaign=sebrissud_gg_pc_os_tf_ao_wb_at_ol_pf&gad_source=1",
                        wait_until="domcontentloaded", timeout=120000)
        page.set_default_timeout(timeout=120000)
        links = page.locator("a")   
        for i in range(await links.count()):
            href = await links.nth(i).get_attribute("href")
            print(href)
        await browser.close()
asyncio.run(site_personagens())