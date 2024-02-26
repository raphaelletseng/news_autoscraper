import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

lm_url = "https://www.lemonde.fr/en/"
lm_response = requests.get(lm_url)
lm_soup = BeautifulSoup(lm_response.content, "html.parser")

lm_headlines = lm_soup.select("p.article__title")
print(lm_headlines)
data = {
    'org': lm_url,
    'scraped_at': datetime.datetime.now(),
    'headline_1': lm_headlines[0].select('p.article__title-label')[0].text,
    'headline_2': '',
    'headline_3': '',
}
headlines=[]

for idx, h in enumerate(lm_headlines[1:3]):
    print('here')
    try:
        headline = h.select('p.article__title').text
        print(headline)
        print('----')
        headlines.append(h.text)
    except:
        pass

print(headlines)

for i in range(1, len(headlines)):
    key = f'headline_{i+1}'
    value = headlines[i]
    data[key] = value

df = pd.DataFrame(data, index=[0])
print(df.head())

# try:
#     existing_df = pd.read_csv("updated_headlines.csv")
# except:
#     existing_df = pd.DataFrame([])

# combined = pd.concat([df, existing_df], ignore_index=True)

# combined.to_csv("updated_headlines.csv", index=False)
