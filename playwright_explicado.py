import asyncio # tipo de funcao, todos arquivos de playwirght precisa dessa biblioteca
from playwright.async_api import async_playwright # importanto a "melhor" api que e a async_api

async def main():
    async with async_playwright() as p: # para inicializar o playwright precisa desse "async with" por questoes de seguranca,
        # como arrumar o laboratorio antes de comecar o esperimento
        browser = await p.chromium.launch()# ele vem com headless=True, isso faz nao abrir o navegador, mas caso queiram so colocar no launch(headless=False)
        page = await browser.new_page() # criando a page, que e aonde voce navega,Clica,Le conteudo, executa JavaScript
        await page.goto("https://bileto.sympla.com.br/event/115660/d/362549") # fazendo a requisicao pela url.
        # quando voce nao define wait_until e o timeout, o proprio playwright decide por voce, e o default é await page.goto(url, wait_until="load", timeout=30000) e voce pode mudar caso necessario
        precos = await page.locator('span.range-ticket-price').all_inner_texts() # usar o (.) indica a classe se for id usa (#) EX: span#range-ticket-price
        #precos = await page.locator('span:has-text("R$")').all_inner_texts()  = Busca todos os spans que contenham "R$" no texto
        print(precos)
        await browser.close() # fechando o browser, porque precisamos encerrar o scraping, meio logico
if __name__ == "__main__": # para que a funcao nao seja executada automaticamente quando importada
    asyncio.run(main()) # para executar precisa usar o asyncio, para fazer o script ser executado de maneira assincrona


# tudo que conversa com o navegador é ASSINCRONO
