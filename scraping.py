import asyncio
import json
from extract_cards import get_links
from playwright.async_api import async_playwright


async def scraping_data():
    car_info = []
    async with async_playwright() as p:
        links_with_locators = await get_links()
        browser = await p.chromium.launch()
        for item in links_with_locators:
            url = item["url"]
            site_locators = item["locators"]
            print(f"Processing {url}")
            
            try:
                page = await browser.new_page() 
                page.set_default_timeout(timeout=20000)
                await page.goto(url)
                if site_locators["use_nth"]:
                    name = await page.locator(site_locators["name_locator"]).inner_text()
                    prices = await page.locator(site_locators["price_locator"]).inner_text()
                    year = await page.locator(site_locators["year_locator"]).nth(site_locators["year_index"]).inner_text()
                    km = await page.locator(site_locators["km_locator"]).nth(site_locators["km_index"]).inner_text()
                    color = await page.locator(site_locators["color_locator"]).nth(site_locators["color_index"]).inner_text()
                else:
                    name = await page.locator(site_locators["name_locator"]).text_content()
                    prices = await page.locator(site_locators["price_locator"]).text_content()
                    year = await page.locator(site_locators["year_locator"]).text_content()
                    km = await page.locator(site_locators["km_locator"]).text_content()
                    color = await page.locator(site_locators["color_locator"]).text_content()
                
                car_info.append({
                    "url": url,
                    "name": name,
                    "price": prices,
                    "year": year,
                    "km": km,
                    "color": color
                })
                await page.close()
            except Exception as e:
                print(f"Error processing {url}: {e}")
        await browser.close()
    with open("output_scraping.json", "w", encoding="utf-8") as f:
        json.dump(car_info, f, ensure_ascii=False, indent=4)
    print("Saved to json successfully")


if __name__ == "__main__":
    asyncio.run(scraping_data())