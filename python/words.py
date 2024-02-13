#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# -*- coding: utf-8 -*-

import openpyxl as op

import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.sohu.com/a/485193126_121124286")
res.encoding="utf-8"
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
# open('./my.html', 'w', encoding='utf-8').write(soup.prettify())
# print(soup)
arti = soup.find_all('tr')

list = []
# 处理数据
for i in arti:
  # print(i.getText())
  list.append([i.getText().split('\n')[1] ,""])

# print(list)
  

# 写入 xlsx 数据
def op_toelcel(data, filename):
  wb = op.Workbook() # 创建工作簿对象
  ws = wb.active # 创建工作表对象
  ws.title = filename
  for a in range(len(data)):
    for b in range(len(data[a])):
      ws.cell(row=a+1, column=b+1, value=data[a][b])
  wb.save(filename + '.xlsx')
  print("数据写入成功！")

op_toelcel(list, 'words')