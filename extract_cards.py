import asyncio
from playwright.async_api import async_playwright
autox_vehicles = {
    "URL" : "https://autoxveiculos.com.br/estoque",
    "links_locator": "div.col-md-6 a",
    "prefix": "",  # this site does not need a prefix
    "price_locator": "//span[contains(@class, 'price-solo')]/parent::*",
    "name_locator": "div.title h3",
    "year_locator": "div.col-6 p",
    "km_locator": "div.col-6 p",
    "color_locator": "div.col-6 p" ,
    "use_nth": True,
    "name_index": "",
    "year_index": 1,
    "km_index": 2,
    "color_index": 3
}

sites = [autox_vehicles] # remember to add the site to the list

async def get_links():
    links_with_locators = []
    for site in sites:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            page.set_default_timeout(timeout=20000)
            await page.goto(site["URL"], wait_until="domcontentloaded", timeout=20000)
            links_locator = page.locator(site["links_locator"])
            await links_locator.first.wait_for()
            all_links = await links_locator.all()
            
            # optional information; comment out if you don't want to see link count
            # print(len(all_links))
            
            for link in all_links:
                final_link = await link.get_attribute('href') # link attributes are always href, I recommend checking the site's HTML
                if final_link:
                    full_url = f"{site['prefix']}{final_link}"
                else:
                    raise ValueError("Invalid URL")
                site_locators = {
                    "price_locator": site["price_locator"],
                    "name_locator": site["name_locator"],
                    "year_locator": site["year_locator"],
                    "km_locator": site["km_locator"],
                    "color_locator": site["color_locator"],
                    "use_nth": site["use_nth"],
                    "year_index": site["year_index"],
                    "km_index": site["km_index"],
                    "color_index": site["color_index"]
                }
                links_with_locators.append({
                    "url": full_url,
                    "locators": site_locators
                })
            await browser.close()
    return links_with_locators


if __name__ == "__main__":
    asyncio.run(get_links())