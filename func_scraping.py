import asyncio
import json
from func_pegar_infos import pegar_links


infos_carros = []
async def scraping_data():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        links_com_locators = await pegar_links()
        browser = await p.chromium.launch()
        for item in links_com_locators:
            url = item["url"]
            site_locators = item["locators"]
            print(f"Processando {url}")
            
            
            page = await browser.new_page()
            await page.goto(url)
            nomes = await page.locator(site_locators["locator_nome"]).inner_text()
            precos = await page.locator(site_locators["locator_preco"]).inner_text()
            ano = await page.locator(site_locators["locator_ano"]).inner_text()
            km = await page.locator(site_locators["locator_km"]).inner_text()
            cor = await page.locator(site_locators["locator_cor"]).inner_text()
            infos_carros.append({
                    "url": url,
                    "nome": nomes,
                    "preco": precos,
                    "ano": ano,
                    "km": km,
                    "cor": cor
                })
            print("Salvo no json com sucesso")
            await page.close()
        await browser.close()
    with open("output_scraping.json", "w", encoding="utf-8") as f:
        json.dump(infos_carros, f, ensure_ascii=False, indent=4)

        


if __name__ == "__main__":
    asyncio.run(scraping_data())

