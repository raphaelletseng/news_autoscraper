import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

aj_url = "https://www.aljazeera.com"
aj_response = requests.get(aj_url)
ajSoup = BeautifulSoup(aj_response.content, "html.parser")

headlines2 = ajSoup.select(".article-card")
data = {
    'org': aj_url,
    'scraped_at': datetime.datetime.now(),
    'headline_1': '',
    'headline_2': '',
    'headline_3': '',
}
headlines=[]
for idx, h in enumerate(headlines2[:4]):
    try:
        headline = (h.select('h3.article-card__title')[0].text.replace(u'\xad', ''))
        headlines.append(headline)
    except:
        pass


def dups(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

nHeadlines = dups(headlines)
for i in range(0, len(nHeadlines)):
    key = f'headline_{i+1}'
    value = nHeadlines[i]
    data[key] = value

df = pd.DataFrame(data, index=[0])

try:
    existing_df = pd.read_csv("updated_headlines.csv")
except:
    existing_df = pd.DataFrame([])
print(existing_df.head())

combined = pd.concat([df, existing_df], ignore_index=True)
print(combined.head())

combined.to_csv("updated_headlines.csv", index = False)
