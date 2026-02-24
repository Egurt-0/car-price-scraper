from bs4 import BeautifulSoup
import httpx
site1 = httpx.get("https://quotes.toscrape.com")
soup1 = BeautifulSoup(site1.text, features='html.parser')

todas_frases = soup1.find_all('div', class_='quote') # nao pode usar so class, tem que usar class_ 

for div in todas_frases:
    texto = div.find('span', class_="text").text
    print(texto)

site2 = httpx.get("https://books.toscrape.com")
soup2 = BeautifulSoup(site2.text, features='html.parser')

todos_titulos = soup2.find_all('article', class_='product_pod')

for i in todos_titulos:
    preco = i.find('p', class_='price_color').text
    print(preco)