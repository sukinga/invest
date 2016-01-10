# -*- coding: utf-8 -*-
__author__ = 'lixin'

import httplib2
import json
from bs4 import BeautifulSoup
import time

h = httplib2.Http("")
transfer_url = 'http://www.id68.cn/transfer'
resp, content = h.request(transfer_url,"GET",
                          headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'})
soup = BeautifulSoup(content,"html.parser",from_encoding="utf-8")

for i in soup.find_all('ul','ideal_con')[1].find_all('li'):
    #print bool(i.getText().encode('utf8').count('标满'))
    #x = i.find_all('a')[0].encode('utf8')
    #print type(x)
    #x.find(start='/transfer/',end='.html')
    #print i.find_all('href')
    xx = 'afds'
    xx.find(start='/transfer/',end='.html')