# -*- coding: utf-8 -*-
__author__ = 'lixin'

import httplib2
import json
from bs4 import BeautifulSoup
import time

h = httplib2.Http("")

for i in range(1,300):
    print '开始启动第',i,'次抓取：',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    resp, content = h.request("http://www.eloancn.com/new/loadNewUserTender.action","GET",
                          headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'})
    soup = BeautifulSoup(content,"html.parser",from_encoding="utf-8")
    print '首页满标的个数：',len(soup.find_all('a','fast_money_disable mt8')),'：',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())