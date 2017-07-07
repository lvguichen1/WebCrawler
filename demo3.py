#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 引入相关模块
import requests
from bs4 import BeautifulSoup
import json

url = "http://news.qq.com/"
#获取txt文本e
webdata = requests.get(url).text
#对获取的文本进行解析
soup = BeautifulSoup(webdata, 'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.text > em.f14 > a.linkto")
# 对返回的列表进行遍历
for n in news_titles:
    #提取出标题和链接信息
    title = n.get_text()
    link = n.get("href")
    data = {"标题":title, "链接":link}
    # 如果直接打印打印出的是一堆码点
    print data
    # 要正常显示中文，可以借助json模块
    print json.dumps(data, ensure_ascii=False, encoding='UTF-8')