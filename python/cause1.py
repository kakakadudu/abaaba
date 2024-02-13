#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# -*- coding: utf-8 -*-

import urllib.request as request
import re
import openpyxl as op

# 本地 ssl 报错解决
import ssl
# 方案一 全局取消证书验证
# ssl._create_default_https_context = ssl._create_unverified_context
context = ssl._create_unverified_context()

url ='https://www.douban.com/doulist/44773558/'

# 反爬虫机制 使用伪浏览器
header = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
  'Host':'www.douban.com'
}
req = request.Request(url=url, headers=header);
# 方案二 request.urlopen(url, context=context)
res = request.urlopen(req, context=context);
content = res.read().decode('utf-8')
# print(content)


# 提取信息

pattern = re.compile('<div.*?doulist-item.*?"title">.*?"_blank">(.*?)</a>.*?"rating_nums">(.*?)</span>.*?"abstract">(.*?)</div>.*?"comment">(.*?)</blockquote>.*?</div>', re.S)

data = re.findall(pattern, content)
# print(data)
list = [['书籍', '作者', '出版社', '出版年']]
# 处理数据
for i in data:
  title, score, abstract, commont = i
  author, publisher, pubdate = abstract.split('<br />')
  list.append([title.strip(), author.replace('作者:', '').strip(), publisher.replace('出版社:', '').strip(), pubdate.replace('出版年:', '').strip()])
  # print(title, score, author, publisher, pubdate)

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

op_toelcel(list, 'books')

# op_toelcel([['书籍', '作者', '发布日期'], ['123','hh','2012-09-10'], ['456','hhh','2012-09-10']], 'book')