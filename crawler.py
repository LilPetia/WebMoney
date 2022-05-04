import requests
from bs4 import BeautifulSoup
import re
import json
def get_value():
    link = "http://cbr.ru/currency_base/daily"
    responce = requests.get(link)
    soup = BeautifulSoup(responce.text, 'html.parser')
    p = []
    for i in soup.find_all('td'):
        p.append(i)
    count = 2
    currency = []
    while count <= len(p):
        d = {}
        d["count"] = int(p[count].string)
        count += 1
        d["currency_name"] = p[count].string
        count += 1
        d["currency"] = float(p[count].string.replace(',','.'))
        count += 3
        currency.append(d)

    with open("currency.txt", "w") as f:
        for i in currency:
            f.write(json.dumps(i, ensure_ascii=False) + "\n")
    return currency