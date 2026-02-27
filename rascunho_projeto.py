import asyncio
from playwright.async_api import async_playwright
import json

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
            print(f"nome: {nomes} Preco Atual: {precos}")
            dados_do_carro = {
                "nome": nomes,
                "precos": precos
            }
            data.append(dados_do_carro)
            
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
            print(f"nome: {nomes} Preco Atual: {precos}")
            dados_do_carro = {
                "nome": nomes,
                "preco": precos
            }
            data.append(dados_do_carro)

        # <--- MUDANÇA DE IDENTAÇÃO: O bloco abaixo foi movido para fora (para a esquerda)
        with open('output_rascunho.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
        await browser.close()




async def coletando_precos_chave_na_mao():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.chavesnamao.com.br/carros-usados/sp-sao-paulo/?utm_source=google&utm_medium=conversao_veiculos&utm_campaign=roas_dsa_sp_capital&utm_content=&gad_source=1&gad_campaignid=16085875802&gclid=CjwKCAiA2PrMBhA4EiwAwpHyC6FqaivFLMXHitK5i__XfFPehOMRWnXZeIwPm_rATWTN81OXL0VBVxoCwRsQAvD_BwE",
            wait_until="load", timeout=60000)
        page.set_default_timeout(timeout=60000)
        for i in range(8):
            await page.mouse.wheel(0, 3000)
            await page.wait_for_timeout(1000)
        card_locator = page.locator('.style_container__oZoGd')
        todos_carros = await card_locator.all() # all junta tudo carregado em uma lista
        print(f"foram encotrados {len(todos_carros)} cards de carros") # como defini card_locator como lista ele precisa do len, pq nao consegue comparar um numero com uma lista
        for carro in todos_carros[:20]:
            await page.mouse.wheel(0, 4000)
            await page.wait_for_timeout(2000)
            await carro.scroll_into_view_if_needed()
            await page.wait_for_timeout(1000)
            nomes = await carro.locator('b.ellipses').inner_text()
            precos = await carro.locator('p.style_price__e3ffu:has-text("R$")').inner_text()
            print(f"Nome: {nomes} - Preco Atual: {precos}")
            dados_do_carro = {
            "nome": nomes,
            "preco": precos
            }
            data.append(dados_do_carro)

        # <--- MUDANÇA DE IDENTAÇÃO: O bloco abaixo foi movido para fora (para a esquerda)
        with open('output_rascunho.json', 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        await browser.close()




asyncio.run(coletando_precos_napista())
asyncio.run(coletando_precos_localiza_seminovos())
asyncio.run(coletando_precos_chave_na_mao())