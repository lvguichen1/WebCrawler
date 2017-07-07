#!/usr/bin/python
# -*- utf-8 -*-


import requests
import json

url = 'http://www.toutiao.com/api/pc/focus/'
webdata = requests.get(url).text

data = json.loads(webdata)
news = data['data']['pc_feed_focus']
for n in news:
    title = n['title']
    image_url = n['image_url']
    url = n['media_url']
    print(title,image_url,url)