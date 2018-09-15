import requests
from bs4 import BeautifulSoup
import json
import os

req = requests.get("https://comic.naver.com/webtoon/list.nhn?titleId=679519&weekday=mon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
table_css = soup.find_all(("td", {"class": "title"}))
title_list = list()
for index in table_css:
    info_soup = index.find("a")
    if info_soup is not None:
        if info_soup.string is not None:
            print(info_soup.string)
            title_list.append(info_soup.string)

print(title_list)