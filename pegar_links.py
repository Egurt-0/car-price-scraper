from pymongo import MongoClient
import json
import asyncio
async def pegar_links():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://napista.com.br/busca/carro/ate-30000-reais?utm_source=GoogleAds&utm_medium=PMax&utm_campaign=PMax&gclsrc=aw.ds&utm_source=google&utm_medium=cpc&gad_source=1&gad_campaignid=22474505263&gclid=CjwKCAiA-__MBhAKEiwASBmsBGwllQ9e-AUFWUYrmqTDlTrCdKabk8AuHS4pLKGLhdDh3EMEJGfUyxoCAVEQAvD_BwE&pn=1",
            wait_until="load", timeout=60000)
        page.set_default_timeout(timeout=60000)
        locator_dos_links = page.locator('a.styles_listingCard__TnL78')
        await locator_dos_links.first.wait_for()
        todos_links = await locator_dos_links.all()
        for link in todos_links:
            link_final = await link.get_attribute('href') # os atributos de link sao sempre href, recomendo olhar no html do site
            print(f"napista.com.br{link_final}")
        # outro site
        page = await browser.new_page() # nesse caso nao precisei nem fechar o browser antigo nem abrir outro, reutilizo o browser aberto e apenas abro outra page com o link do outro site
        await page.goto('https://seminovos.localiza.com/carros/pr-curitiba?page=26', wait_until='load', timeout=60000)
        page.set_default_timeout(timeout=60000)
        locator_dos_links = page.locator("div.MuiGrid2-root a")
        await locator_dos_links.first.wait_for()
        todos_links = await locator_dos_links.all()
        for link in todos_links:
            link_final = await link.get_attribute('href')
            print(f"https://seminovos.localiza.com{link_final}")
        browser.close()
        # outro site
        page = await browser.new_page()
        await page.goto('https://seminovos.localiza.com/carros/pr-curitiba?page=26', wait_until='load', timeout=60000)
        page.set_default_timeout(timeout=60000)
        

asyncio.run(pegar_links())