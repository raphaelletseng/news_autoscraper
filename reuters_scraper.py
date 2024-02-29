import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
from playwright.async_api import async_playwright
import asyncio


async def main():
    # playwright = await async_playwright().start()
    # browser = await playwright.chromium.launch(headless=False)
    # page = await browser.new_page()
    # await page.goto("https://www.reuters.com/")
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.reuters.com/")
        await page.wait_for_timeout(1000)
        print('hello')
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.select('ul'))
        

if __name__ == '__main__':
    asyncio.run(main())

#https://github.com/oxylabs/playwright-web-scraping
#https://jonathansoma.com/everything/scraping/solving-captchas-in-playwright-with-nopecha/
#https://jsoma.github.io/advanced-scraping-with-playwright/



# reuters_headlines = soup.select('div')
# print(reuters_headlines)
#te_h3 = reuters_headlines.find_all('h3')

# data = {
#     'org': url,
#     'scraped_at': datetime.datetime.now(),
#     'headline_1': '',
#     'headline_2': '',
#     'headline_3': '',
# }

# headlines = []
# for idx, h in enumerate(te_h3[:3]):
#     try:
#         headlines.append(h.text)
#     except: 
#         pass

# for i in range(0, len(headlines)):
#     key = f'headline_{i+1}'
#     value = headlines[i]
#     data[key] = value

# df = pd.DataFrame(data, index= [0])
# print(df.head())

# try:
#     existing_df = pd.read_csv("updated_headlines.csv")
# except:
#     existing_df = pd.DataFrame([])

# combined = pd.concat([df, existing_df], ignore_index=True)

# combined.to_csv("updated_headlines.csv", index=False)
