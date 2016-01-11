# -*- coding: utf-8 -*-
__author__ = 'lixin'

import httplib2
from bs4 import BeautifulSoup
import mail139

h = httplib2.Http("",timeout=15)
transfer_url = 'http://www.id68.cn/transfer'
resp, content = h.request(transfer_url,"GET",
                          headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'})
soup = BeautifulSoup(content,"html.parser",from_encoding="utf-8")

new_list = []
for i in soup.find_all('ul','ideal_con')[1].find_all('li'):
    item = i.find_all('span')
    id = item[0].encode('utf8').split('/transfer/')[1].split('.html')[0]
    mouth = item[1].encode('utf8').split('">')[1].split('</')[0].strip()
    rate = item[2].encode('utf8').split('">')[1].split('</')[0]
    count = item[5].encode('utf8').split('">')[1].split('</')[0]
    if(len(i.find_all('input'))==1):
        new_list.append([int(id),mouth,rate,count])

old_list = []
file_object = open('id68.txt')
for i in file_object:
    old_list.append(int(i))
file_object.close()
for temp in new_list:
    if temp[0] not in old_list:
        title = '编号:'+str(temp[0])+';期限:'+temp[1]+';利率:'+temp[2]+';额度:'+temp[3]
        if(mail139.semd_mail('13581798781@139.com',title,'') and mail139.semd_mail('13810090086@139.com',title,'')):
        #if(mail139.semd_mail('13581798781@139.com',title,'')):
            file_object = open('id68.txt','a')
            file_object.write('\n')
            file_object.write(str(temp[0]))
            file_object.close()