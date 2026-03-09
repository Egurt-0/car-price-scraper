from pymongo import MongoClient
import json
import asyncio

napista = {
    "URL": "https://napista.com.br/busca/carro/ate-30000-reais?utm_source=GoogleAds&utm_medium=PMax&utm_campaign=PMax&gclsrc=aw.ds&utm_source=google&utm_medium=cpc&gad_source=1&gad_campaignid=22474505263&gclid=CjwKCAiA-__MBhAKEiwASBmsBGwllQ9e-AUFWUYrmqTDlTrCdKabk8AuHS4pLKGLhdDh3EMEJGfUyxoCAVEQAvD_BwE&pn=1",
    "locator_dos_links": "a.styles_listingCard__TnL78",
    "prefixo": "napista.com.br",
    "locator_preco": "div.sc-9bde1185-0 elZSMH",
    "locator_nome": "h1.sc-9bde1185-0 kqJXUE",
    "locator_ano": "div.sc-9bde1185-0 iQEUaK",
    "locator_km": "div.sc-9bde1185-0 iQEUaK",
    "locator_cor": "div.sc-9bde1185-0 iQEUaK",
    "usa_nth": True,
    "indice_ano": 1,
    "indice_km": 2,
    "indice_cor": 4
}

seminovos_localiza = {
    "URL": "https://seminovos.localiza.com/carros/pr-curitiba?page=26",
    "locator_dos_links": "div.MuiGrid2-root a",
    "prefixo": "https://seminovos.localiza.com",
    "locator_preco": "div.MuiTypography-root.mui-12d4xyd p",
    "locator_nome": "div.MuiTypography-root.mui-1w8tuy p",
    "locator_ano": "div.MuiTypography-root.mui-1k7px3r p",
    "locator_km": "div.MuiTypography-root.mui-1k7px3r p",
    "locator_cor": "h6.MuiTypography-root.mui-1phhdp6",
    "usa_nth": True,
    "indice_ano": 2 ,
    "indice_km": 3,
    "indice_cor": 4,
}

autox_veiculos = {
    "URL" : "https://autoxveiculos.com.br/estoque?utm_source=GoogleAds&utm_medium=Kayron&utm_campaign=SEARCH&ad_id=789081271408&gad_source=1&gad_campaignid=23385700981&gclid=CjwKCAiAnoXNBhAZEiwAnItcG_9aICDqfBno0m_OL_rJq7wgnTMwsEwvBZlvNoBHT3PYMKiqz60L8hoCg-sQAvD_BwE",
    "locator_dos_links": "div.col-md-6 a",
    "prefixo": "",  # esse site nao precisa de prefixo
    "locator_preco": "span.price-solo",
    "locator_nome": "div.title h3",
    "locator_ano": "div.col-6 p",
    "locator_km": "div.col-6 p",
    "locator_cor": "div.col-6 p" ,
    "usa_nth": True,
    "indice_ano": 2,
    "indice_km": 3,
    "indice_cor": 4
}

sites = [napista,seminovos_localiza,autox_veiculos] # lembra de adicionar o site a lista
async def pegar_links():
    links_com_locators = []
    for site in sites:
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(site["URL"],wait_until="load", timeout=60000)
            page.set_default_timeout(timeout=60000)
            locator_dos_links = page.locator(site["locator_dos_links"])
            await locator_dos_links.first.wait_for()
            todos_links = await locator_dos_links.all()
            # informação opcional; comente se não quiser ver contagem de links
            # print(len(todos_links))
            for link in todos_links:
                link_final = await link.get_attribute('href') # os atributos de link sao sempre href, recomendo olhar no html do site
                url_completa = f"{site['prefixo']}{link_final}"
                site_locators = {
                    "locator_preco": site["locator_preco"],
                    "locator_nome": site["locator_nome"],
                    "locator_ano": site["locator_ano"],
                    "locator_km": site["locator_km"],
                    "locator_cor": site["locator_cor"],
                    "usa_nth": site["usa_nth"],
                    "indice_ano": site["indice_ano"],
                    "indice_km": site["indice_km"],
                    "indice_cor": site["indice_cor"]
                }
                links_com_locators.append({
                    "url": url_completa,
                    "locators": site_locators
                })
            await browser.close()
    return links_com_locators


if __name__ == "__main__":
    asyncio.run(pegar_links())