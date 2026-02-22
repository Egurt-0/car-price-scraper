from bs4 import BeautifulSoup
import httpx
site1 = httpx.get("https://books.toscrape.com")
soup1 = BeautifulSoup(site1, features='html.parser')
site2 = httpx.get("https://quotes.toscrape.com")
soup2 = BeautifulSoup(site2, features='html.parser')

print(soup1.find_all())
print(f"{soup1.prettify()}\n")
print(soup2.prettify())
 