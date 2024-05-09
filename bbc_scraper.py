import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

bbc_url = "https://www.bbc.com"
bbc_response = requests.get(bbc_url)
bbc_soup = BeautifulSoup(bbc_response.content, 'html.parser')

bbc_headlines = bbc_soup.select('h2', attrs={'data-testid': 'card-headline'})
bbc_links = bbc_soup.find('div', attrs = {'data-testid': 'vermont-section'})
bbc_a = bbc_links.find_all('a')
#print(bbc_a)

data = {
    'org': bbc_url,
    'scraped_at': datetime.datetime.now(),
    'headline_1': '',
    'headline_2': '',
    'headline_3': '',
}

headlines = []
# Skip first two main headlines in BBC 
for idx, h in enumerate(bbc_headlines[2:5]):
    try:
        headlines.append(h.text)
    except: 
        pass

links = []
for idx, a in enumerate(bbc_a[2:5]):
    try: 
        link = a['href']  
        if(link.startswith(bbc_url)):
            links.append(link)
        else:
            links.append(bbc_url+link)
    except:
        pass

for i in range(0, len(headlines)):
    key = f'headline_{i+1}'
    value = str(headlines[i]) + ', ' + str(links[i])
    data[key] = value

df = pd.DataFrame(data, index= [0])
try:
    existing_df = pd.read_csv("updated_headlines.csv")
except:
    existing_df = pd.DataFrame([])

combined = pd.concat([df, existing_df], ignore_index=True)

combined.to_csv("updated_headlines.csv", index=False)
