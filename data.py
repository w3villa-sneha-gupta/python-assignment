import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.amazon.com/s?k=oppo&crid=A3Y84LEZMYY7&sprefix=oppo%2Caps%2C368&ref=nb_sb_noss_1"
proxies={
    "http": "http://67.213.212.39"
}

response=requests.get(url,proxies=proxies)
soup= BeautifulSoup(response.text , "html.parser")

for data in soup.find_all(class_="a-size-medium"):
    print(data.text)
for data in soup.find_all(class_="a-price-whole"):
    print(data.text)