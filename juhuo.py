# -*- coding: utf-8 -*-
__author__ = 'lixin'

from selenium import webdriver
import time
import os

file_object = open('juhuo.txt')
juhuo_info = {}
for i in file_object:
    juhuo_info[i.split('=')[0].strip()] = i.split('=')[1].strip()
print juhuo_info


option = webdriver.ChromeOptions()
option.add_argument('test-type')
browser =webdriver.Chrome(chrome_options=option)
browser.maximize_window()

#登录操作
browser.get("https://www.juhuotz.com/toLoginPage")
browser.find_element_by_id("userName").send_keys(juhuo_info['username'])
browser.find_element_by_id("password").send_keys(juhuo_info['passwd'])
browser.find_element_by_id("submit").click()
time.sleep(5)
#进入投标页面
print '进入投标页面：',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
browser.get(juhuo_info['tag_url'])
time.sleep(1)
#刷新页面，判断是否可以投标
for i in range(int(juhuo_info['repeat_times'])):
    print '判断是否可以投标：',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),':',i
    if(browser.page_source.encode('utf-8').find('开始投标')>0):
        break
    else:
        browser.refresh()
#出现开始投标信息，判断可以开始投标
print '开始投标：',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
browser.find_element_by_link_text('开始投标').click()
browser.find_element_by_id("myinvest").send_keys(int(juhuo_info['invest_num']))
browser.find_element_by_id("investButton").click()
#跳转到支付页面
print '开始支付：',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
time.sleep(1)
browser.find_element_by_id("btn").click()
browser.find_element_by_id("passWord").send_keys(juhuo_info['pay_passwd'])

