import asyncio
from playwright.async_api import async_playwright

dict = {
    "Nome": str,
    "Preco": int
}

async def coletando_precos():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.webmotors.com.br/carros/estoque/jeep/commander?autocomplete=jeep%20comander%20T270&autocompleteTerm=Jeep%20Commander&tipoveiculo=carros&marca1=JEEP&modelo1=COMMANDER&page=1",
            wait_until="load", timeout=60000)
        page.set_default_timeout(timeout=60000)
        card_locator = page.locator('._BodyItemSpaceBetween_1wsqi_75') # ele ainda nao procurou nada, por isso nao tem await nem inner_text
        todos_carros = await card_locator.all() # apartir daqui ele varre o hmtl e transforma em uma lista
        print(f"foram encotrados {len(todos_carros)} cards de carros")
        for carro in todos_carros:
            precos = await carro.locator('p._web-subtitle-medium_qtpsh_69:has-text("R$")').inner_text()
            print(f"Preco Atual: {precos}")
        await browser.close()
asyncio.run(coletando_precos())