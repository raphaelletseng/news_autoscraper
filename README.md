# aj_autoscraper

A daily scraper for the top 3 news headlines from:
- [Al Jazeera](https://www.aljazeera.com/)
- [BBC](https://www.bbc.com/)


- `[news_org]_scraper.py` scrapes the news organisation's home page using BeautifulSoup every day at 5.30 UTC
- The data gets appended to `updated_headlines.csv`