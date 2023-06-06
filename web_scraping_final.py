import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

url = "https://www.pracuj.pl/praca/it%20-%20programowanie%20-%20analiza;kw"
result = requests.get(url)
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

stanowiska = doc.find_all('a', class_='listing_o1dyw02w listing_n194fgoq')
tryb_pracy = doc.find_all('li', class_='listing_isg28kc')
miasta = doc.find_all('h5', class_='listing_rdl5oe8')

table = []
for i in range(len(stanowiska)):
    row = {
        "Stanowisko": stanowiska[i].text.strip(),
        "Tryb pracy": tryb_pracy[i].text.strip(),
        "Miasto": miasta[i].text.strip(),
        "Link": stanowiska[i]['href']
    }
    table.append(row)

df = pd.DataFrame(table)
df.to_excel("wyniki10.xlsx", index=False)
