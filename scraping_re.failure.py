import asyncio
import re
from playwright.async_api import async_playwright

async def site_auto_pecas():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?utm_source=%20&utm_medium=cpc&utm_campaign=sebrissud_gg_pc_os_tf_ao_wb_at_ol_pf&gad_source=1"
        await page.goto(url, wait_until="domcontentloaded", timeout=120000)
        general_locator = page.locator("a")
        total = await general_locator.count()
        links = []
        for i in range(total):
            href = await general_locator.nth(i).get_attribute('href')
            if href and re.compile(r"https:\/\/[a-z]{2}\..*").search(href):
                links.append(href)
        for link in links:
            print(link)
        await browser.close()

# Executa o script
if __name__ == "__main__":
    asyncio.run(site_auto_pecas())