import asyncio
import re
from playwright.async_api import *

async def site_auto_pecas():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Acessando a URL (com timeout aumentado para evitar erros de rede)
        url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?utm_source=%20&utm_medium=cpc&utm_campaign=sebrissud_gg_pc_os_tf_ao_wb_at_ol_pf&gad_source=1"
        await page.goto(url, wait_until="domcontentloaded", timeout=120000)
        locator_geral = page.locator("a.adcard-link", timeout=)
        total = await locator_geral.count()
        links = []
        for i in range(total):
            href = await locator_geral.nth(i).get_attribute('href')
            if href and re.compile(r"https:\/\/[a-z]{2}\..*", re.IGNORECASE):
                links.append(href)
        for link in links:
            print(link)
        
        await browser.close()

# Executa o script
if __name__ == "__main__":
    asyncio.run(site_auto_pecas())