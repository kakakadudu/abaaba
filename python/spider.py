#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
res = requests.get("http://dybxdaaaaaa.top/note")
res.encoding="utf-8"
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
# open('./my.html', 'w', encoding='utf-8').write(soup.prettify())
# print(soup)
arti = soup.find_all('article')
# print(arti)
for a in arti:
    open('./test_file_copy.txt', 'a', encoding='utf-8').write(a.getText() + '\n')