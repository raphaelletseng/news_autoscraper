# news_autoscraper

A daily scraper for the top 3 news headlines from:
- [Al Jazeera](https://www.aljazeera.com/)
- [BBC](https://www.bbc.com/)
- [Le Monde](https://www.lemonde.fr/en/)
- [The Economist](https://www.economist.com/)


`[news_org]_scraper.py` scrapes the news organisation's home page using BeautifulSoup every day at 5.30 UTC. The data gets appended to `updated_headlines.csv`

Resources: [https://jonathansoma.com/](https://jonathansoma.com/)


### Analysis

Take a look at [`pie_charts.ipynb`](https://github.com/raphaelletseng/news_autoscraper/blob/main/pie_charts.ipynb) for basic counts of most occuring words between two dates, after removing stopwords:
![top_10_count_fig](top_10_words_2024-11-01.png)