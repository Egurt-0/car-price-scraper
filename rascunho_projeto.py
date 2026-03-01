import asyncio
from playwright.async_api import async_playwright
import json
from pymongo import MongoClient

    

conexao = MongoClient('mongodb://localhost:27017')
db = conexao.get_database("carros_info")
colecao = db.get_collection('carros_nomes_precos')

data = []

async def coletando_precos_napista():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://napista.com.br/busca/carro/ate-30000-reais?utm_source=GoogleAds&utm_medium=PMax&utm_campaign=PMax&gclsrc=aw.ds&utm_source=google&utm_medium=cpc&gad_source=1&gad_campaignid=22474505263&gclid=CjwKCAiA-__MBhAKEiwASBmsBGwllQ9e-AUFWUYrmqTDlTrCdKabk8AuHS4pLKGLhdDh3EMEJGfUyxoCAVEQAvD_BwE&pn=1",
            wait_until="load", timeout=60000)
        page.set_default_timeout(timeout=60000)
        card_locator = page.locator('.styles_listingCardContentWrapper__eTihz') # ele ainda nao procurou nada, por isso nao tem await nem inner_text
        todos_carros = await card_locator.all() # apartir daqui ele varre o hmtl e transforma em uma lista
        print(f"foram encotrados {len(todos_carros)} cards de carros")
        for carro in todos_carros:
            nomes = await carro.locator('h2.styles_listingCardContentTitle__AWk2f').inner_text()
            precos = await carro.locator('span.typo--heading:has-text("R$")').inner_text()
            precos_limpos = precos.replace("R$", "").replace(".", "").strip()
            print(f"nome: {nomes} Preco Atual: {precos_limpos}")
            dados_do_carro = {
                "nome": nomes,
                "precos": precos_limpos
            }
            data.append(dados_do_carro)
        if data:
            colecao.insert_many(data)
            print(len(f"{len(data)}, dados salvos no mongodb"))
        # <--- MUDANÇA DE IDENTAÇÃO: O bloco abaixo foi movido para fora (para a esquerda)
        with open('output_rascunho.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
                    
        await browser.close()

 

async def coletando_precos_localiza_seminovos():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://seminovos.localiza.com/carros/pr-curitiba",
            wait_until="load", timeout=60000)
        page.set_default_timeout(timeout=60000)
        card_locator = page.locator('.mui-o9w1ny') # ele ainda nao procurou nada, por isso nao tem await nem inner_text
        todos_carros = await card_locator.all() # apartir daqui ele varre o hmtl e transforma em uma lista
        print(f"foram encotrados {len(todos_carros)} cards de carros")
        for carro in todos_carros:
            nomes = await carro.locator('span.MuiTypography-root').inner_text()
            precos = await carro.locator('h3.MuiTypography-root:has-text("R$")').inner_text()
            precos_limpos = precos.replace("R$", "").replace(".", "").strip()
            print(f"nome: {nomes} Preco Atual: {precos_limpos}")
            dados_do_carro = {
                "nome": nomes,
                "preco": precos_limpos
            }
            data.append(dados_do_carro)
        if data:
            colecao.insert_many(data)
        # <--- MUDANÇA DE IDENTAÇÃO: O bloco abaixo foi movido para fora (para a esquerda)
        with open('output_rascunho.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        await browser.close()



async def coletando_precos_localiza_olx():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://autoxveiculos.com.br/estoque?utm_source=GoogleAds&utm_medium=Kayron&utm_campaign=SEARCH&ad_id=789081271408&gad_source=1&gad_campaignid=23385700981&gclid=CjwKCAiAnoXNBhAZEiwAnItcG_9aICDqfBno0m_OL_rJq7wgnTMwsEwvBZlvNoBHT3PYMKiqz60L8hoCg-sQAvD_BwE",
            wait_until="load", timeout=60000)
        page.set_default_timeout(timeout=60000)
        card_locator = page.locator('.card') # ele ainda nao procurou nada, por isso nao tem await nem inner_text
        todos_carros = await card_locator.all() # apartir daqui ele varre o hmtl e transforma em uma lista
        print(f"foram encotrados {len(todos_carros)} cards de carros")
        for carro in todos_carros:
            nomes = await carro.locator('p.fw-bold').inner_text()
            precos = await carro.locator('strong.fs-4').inner_text()
            precos_limpos = precos.replace("R$", "").replace(".", "").strip()
            print(f"nome: {nomes} Preco Atual: {precos_limpos}")
            dados_do_carro = {
                "nome": nomes,
                "preco": precos_limpos
            }
            data.append(dados_do_carro)
        if data:
            colecao.insert_many(data)
        # <--- MUDANÇA DE IDENTAÇÃO: O bloco abaixo foi movido para fora (para a esquerda)
        with open('output_rascunho.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        await browser.close()





asyncio.run(coletando_precos_napista())
asyncio.run(coletando_precos_localiza_seminovos())
asyncio.run(coletando_precos_localiza_olx())

