import asyncio
import json
from extract_cards import get_links
from playwright.async_api import async_playwright

car_info = []
async def scraping_data():
    async with async_playwright() as p:
        links_with_locators = await get_links()
        browser = await p.chromium.launch()
        for item in links_with_locators:
            url = item["url"]
            site_locators = item["locators"]
            print(f"Processing {url}")
            try:
                page = await browser.new_page()
                await page.goto(url)
                
                if site_locators["use_nth"]:
                    names = await page.locator(site_locators["name_locator"]).inner_text()
                    prices = None
                    for locator in site_locators["price_locator"]:
                        try:
                            prices = await page.locator.site((locator)).inner_text()
                            if prices:
                                break
                        except Exception as e:
                            print(f"Price locator {locator} failed: {e}")
                            continue
                    year = await page.locator(site_locators["year_locator"]).nth(site_locators["year_index"]).inner_text()
                    km = await page.locator(site_locators["km_locator"]).nth(site_locators["km_index"]).inner_text()
                    color = await page.locator(site_locators["color_locator"]).nth(site_locators["color_index"]).inner_text()
                else:
                    names = await page.locator(site_locators["name_locator"]).inner_text()
                    prices = await page.locator(site_locators["price_locator"]).inner_text()
                    year = await page.locator(site_locators["year_locator"]).inner_text()
                    km = await page.locator(site_locators["km_locator"]).inner_text()
                    color = await page.locator(site_locators["color_locator"]).inner_text()
                
                car_info.append({
                    "url": url,
                    "name": names,
                    "price": prices,
                    "year": year,
                    "km": km,
                    "color": color
                })
                await page.close()
            except Exception as e:
                print(f"Error processing {url}: {e}")
                continue
        await browser.close()
    
    with open("output_scraping.json", "w", encoding="utf-8") as f:
        json.dump(car_info, f, ensure_ascii=False, indent=4)
    print("Saved to json successfully")

if __name__ == "__main__":
    asyncio.run(scraping_data())