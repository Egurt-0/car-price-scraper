import asyncio
import json
from func_pegar_infos import pegar_links
from pymongo import MongoClient

conexao = MongoClient('mongodb://localhost:27017')
db = conexao.get_database("carros_info")
colecao = db.get_collection('carros_nomes_precos')



info_carros = []
async def scraping_data():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        links_e_locators = await pegar_links()
        browser = await p.chromium.launch()
        for info in links_e_locators:
            url = info["url"]
            site_locators = info["locators"]
            print(f"Processando {url}")
            
            
            page = await browser.new_page()
            await page.goto(url)
            nomes = await page.locator(site_locators["locator_nome"]).inner_text()
            precos = await page.locator(site_locators["locator_preco"]).inner_text()
            ano = await page.locator(site_locators["locator_ano"]).inner_text()
            km = await page.locator(site_locators["locator_km"]).inner_text()
            cor = await page.locator(site_locators["locator_cor"]).inner_text()
            precos_limpos = precos.replace("R$", "").replace(".", "").strip()
            info_carros.append({
                    "url": url,
                    "nome": nomes,
                    "preco": precos_limpos,
                    "ano": ano,
                    "km": km,
                    "cor": cor
                })
            print("Salvo no json com sucesso")
            await page.close()
        await browser.close()
    colecao.insert_many(info_carros)
    with open("output_scraping.json", "w", encoding="utf-8") as file:
        json.dump(info_carros, file, ensure_ascii=False, indent=4)

        


if __name__ == "__main__":
    asyncio.run(scraping_data())

