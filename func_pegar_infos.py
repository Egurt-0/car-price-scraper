import asyncio
olx = {
    "URL": "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?utm_source=%20&utm_medium=cpc&utm_campaign=sebrissud_gg_pc_os_tf_ao_wb_at_ol_pf&gad_source=1",
    "locator_dos_links": "/html/body/div/div[2]/main/div[3]/div[1]/main/div[9]/section[3]/div[1]/div[1]/a",
    "prefixo": "https://pr.olx.com.br",
    "locator_preco": "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div/span/span",
    "locator_nome": "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/h1",
    "locator_ano": "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[5]/div/div[2]/div[5]/div[2]/a",
    "locator_km": "/html/body/div/div/div[2]/div/div[1]/div[2]/div[6]/div/div[2]/div[6]/div[2]/span[2]",
    "locator_cor": "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/ul/li[2]/span"

}
napista = {
    "URL": "https://napista.com.br/busca/carro/ate-30000-reais?utm_source=GoogleAds&utm_medium=PMax&utm_campaign=PMax&gclsrc=aw.ds&utm_source=google&utm_medium=cpc&gad_source=1&gad_campaignid=22474505263&gclid=CjwKCAiA-__MBhAKEiwASBmsBGwllQ9e-AUFWUYrmqTDlTrCdKabk8AuHS4pLKGLhdDh3EMEJGfUyxoCAVEQAvD_BwE&pn=1",
    "locator_dos_links": "/html/body/div[1]/main/div/div[2]/div[3]/div/div[2]/div/div[2]/ul/li[2]/a",
    "prefixo": "https://napista.com.br",
    "locator_preco": "/html/body/div[1]/main/div/div[1]/div/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div/div[1]/div[1]/div/div",
    "locator_nome": '/html/body/div[1]/main/div/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/h1',
    "locator_ano": '/html/body/div[1]/main/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/div[1]/ul/li[1]/div[2]',
    "locator_km": '/html/body/div[1]/main/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/div[1]/ul/li[2]/div[2]',
    "locator_cor": '/html/body/div[1]/main/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/div[1]/ul/li[5]/div[2]'
}

seminovos_localiza = {
    "URL": "https://seminovos.localiza.com/carros/pr-curitiba?page=26",
    "locator_dos_links": "/html/body/div[2]/main/div[4]/div[7]/div[2]/div[1]/div/a",
    "prefixo": "https://seminovos.localiza.com",
    "locator_preco": "/html/body/div[2]/main/div[5]/div/div[2]/div[3]/div[2]/p",
    "locator_nome": "/html/body/div[2]/main/div[5]/div/div[2]/div[1]/p",
    "locator_ano": "/html/body/div[2]/main/div[5]/div/div[7]/div/div[2]/div/h6",
    "locator_km": "/html/body/div[2]/main/div[5]/div/div[7]/div/div[1]/div/h6",
    "locator_cor": "/html/body/div[2]/main/div[5]/div/div[7]/div/div[8]/div/h6"
}

autox_veiculos = {
    "URL" : "https://autoxveiculos.com.br/estoque?utm_source=GoogleAds&utm_medium=Kayron&utm_campaign=SEARCH&ad_id=789081271408&gad_source=1&gad_campaignid=23385700981&gclid=CjwKCAiAnoXNBhAZEiwAnItcG_9aICDqfBno0m_OL_rJq7wgnTMwsEwvBZlvNoBHT3PYMKiqz60L8hoCg-sQAvD_BwE",
    "locator_dos_links": "/html/body/div[3]/div/div[2]/div[1]/div/a",
    "prefixo": "",  # esse site nao precisa de prefixo
    "locator_preco": "/html/body/div[3]/div[4]/div[1]/div[1]/div[1]/div[2]/strong",
    "locator_nome": "/html/body/div[3]/div[4]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/h3",
    "locator_ano": "/html/body/div[3]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/p",
    "locator_km": "/html/body/div[3]/div[4]/div[1]/div[1]/div[2]/div[1]/div[3]/p",
    "locator_cor": "/html/body/div[3]/div[4]/div[1]/div[1]/div[2]/div[1]/div[4]/p"
}

sites = [napista,autox_veiculos,seminovos_localiza,olx] # lembra de adicionar o site a lista
async def pegar_links():
    links_e_locators = []
    for site in sites:
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(site["URL"],wait_until="domcontentloaded", timeout=20000)
            page.set_default_timeout(timeout=20000)
            locator_dos_links = page.locator(site["locator_dos_links"])
            await locator_dos_links.first.wait_for()
            todos_links = await locator_dos_links.all()
            # informação opcional; comente se não quiser ver contagem de links
            # print(len(todos_links))
            for link in todos_links:
                link = site["locator_dos_links"]
                url_completa = f"{site['prefixo']}{link}"
                site_locators = {
                    "locator_preco": site["locator_preco"],
                    "locator_nome": site["locator_nome"],
                    "locator_ano": site["locator_ano"],
                    "locator_km": site["locator_km"],
                    "locator_cor": site["locator_cor"]
                }
                links_e_locators.append({
                    "url": url_completa,
                    "locators": site_locators
                })
            await browser.close()
    return links_e_locators


if __name__ == "__main__":
    asyncio.run(pegar_links())