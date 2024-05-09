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
    'headline_1': str(lm_soup.select_one("section.area--main").select_one("p.article__title-label").text) + ', ' + str(lm_soup.select_one("section.area--main").select_one("a")['href']),
    'headline_2': str(lm_second_headlines[0].text) + ', ' + str(lm_soup.select_one("section.area--headlines").select("a")[0]['href']),
    'headline_3': str(lm_second_headlines[1].text) + ', ' + str(lm_soup.select_one("section.area--headlines").select("a")[1]['href']),
}
headlines=[]

df = pd.DataFrame(data, index=[0])
#print(df.to_string())

try:
    existing_df = pd.read_csv("updated_headlines.csv")
except:
    existing_df = pd.DataFrame([])

combined = pd.concat([df, existing_df], ignore_index=True)

combined.to_csv("updated_headlines.csv", index=False)
