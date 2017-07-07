#!/usr/bin/python
# -*- utf-8 -*-

##提高爬虫效率—并发爬取智联招聘

import requests
from bs4 import BeautifulSoup
import re

url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=hadoop&sm=0&p=1&source=1'
wbdata = requests.get(url).content
soup = BeautifulSoup(wbdata,'lxml')

items = soup.select("div#newlist_list_content_table > table")
count = len(items) - 1

#每页职位数量
print(count)
job_count = re.findall(r"共<em>(.*?)</em>个职位满足条件",str(soup))[0]

# 搜索结果页数
pages = (int(job_count) // count) + 1
print(pages)
