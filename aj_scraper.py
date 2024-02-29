import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

aj_url = "https://www.aljazeera.com"
aj_response = requests.get(aj_url)
aj_soup = BeautifulSoup(aj_response.content, "html.parser")

aj_headlines = aj_soup.select(".article-card")
data = {
    'org': aj_url,
    'scraped_at': datetime.datetime.now(),
    'headline_1': '',
    'headline_2': '',
    'headline_3': '',
}
headlines=[]
links = []
for idx, h in enumerate(aj_headlines[:4]):
    try:
        headline = (h.select('h3.article-card__title')[0].text.replace(u'\xad', ''))
        headlines.append(headline)
        links.append(h.find('a', href=True))
    except:
        pass

def dups(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

nHeadlines = dups(headlines)
nLinks = dups(links)
for i in range(0, len(nHeadlines)):
    key = f'headline_{i+1}'
    value = str(nHeadlines[i]) + ", " + aj_url + str(nLinks[i]['href'])
    print(value)
    data[key] = value

df = pd.DataFrame(data, index=[0])
print(df.head())

try:
    existing_df = pd.read_csv("updated_headlines.csv")
except:
    existing_df = pd.DataFrame([])

combined = pd.concat([df, existing_df], ignore_index=True)

combined.to_csv("updated_headlines.csv", index = False)
