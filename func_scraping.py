import asyncio
import json
from func_pegar_links2 import pegar_links


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
            
            try:
                page = await browser.new_page()
                await page.goto(url)
                
                if site_locators["usa_nth"] == True:
                    nomes = await page.locator(site_locators["locator_nome"]).inner_text()
                    precos = await page.locator(site_locators["locator_preco"]).inner_text()
                    ano = await page.locator(site_locators["locator_ano"]).nth(site_locators["indice_ano"]).inner_text()
                    km = await page.locator(site_locators["locator_km"]).nth(site_locators["indice_km"]).inner_text()
                    cor = await page.locator(site_locators["locator_cor"]).nth(site_locators["indice_cor"]).inner_text()
                else:
                    nomes = await page.locator(site_locators["locator_nome"]).text_content()
                    precos = await page.locator(site_locators["locator_preco"]).text_content()
                    ano = await page.locator(site_locators["locator_ano"]).text_content()
                    km = await page.locator(site_locators["locator_km"]).text_content()
                    cor = await page.locator(site_locators["locator_cor"]).text_content()
                infos_carros.append({
                    "url": url,
                    "nome": nomes,
                    "preco": precos,
                    "ano": ano,
                    "km": km,
                    "cor": cor
                })
                await page.close()
            except Exception as e:
                print(f"Erro ao processar {url}: {e}")
                continue
                        
        await browser.close()
    with open("output_scraping.json", "w", encoding="utf-8") as f:
        json.dump(infos_carros, f, ensure_ascii=False, indent=4)

        


if __name__ == "__main__":
    asyncio.run(scraping_data())

