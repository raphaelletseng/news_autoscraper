import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

lm_url = "https://www.lemonde.fr/en/"
lm_response = requests.get(lm_url)
lm_soup = BeautifulSoup(lm_response.content, "html.parser")

lm_second_headlines = lm_soup.select_one("section.area--headlines").select("p.article__title")
data = {
    'org': lm_url,
    'scraped_at': datetime.datetime.now(),
    'headline_1': lm_soup.select_one("section.area--main").select_one("p.article__title-label"),
    'headline_2': lm_second_headlines[0].text,
    'headline_3': lm_second_headlines[1].text,
}
headlines=[]

df = pd.DataFrame(data, index=[0])
print(df.head())

try:
    existing_df = pd.read_csv("updated_headlines.csv")
except:
    existing_df = pd.DataFrame([])

combined = pd.concat([df, existing_df], ignore_index=True)

combined.to_csv("updated_headlines.csv", index=False)
