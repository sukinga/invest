# -*- coding: utf-8 -*-
__author__ = 'lixin'

import smtplib
import email
import sys
from email.mime.text import MIMEText

#========================================
#需要配置
send_mail_host="mail.baofeng.com"      # 发送的smtp
send_mail_user="lixin@baofeng.com"
send_mail_user_name="前海理想金融"
send_mail_pswd=""
send_mail_postfix="baofeng.com"  #发邮件的域名

#get_mail_user="13581798781@139.com"

#以下不用配置=============================

get_mail_postfix="139.com"
get_mail_host="pop.139.com"


#========================================
def semd_mail(get_mail_user,sub,content):
    '''
    sub:主题
    content:内容
    send_mail("xxxxx@xxx.xxx","主题","内容")
    '''
    send_mail_address=send_mail_user_name+"<"+send_mail_user+"@"+send_mail_postfix+">"
    msg=email.mime.text.MIMEText(content)
    msg['Subject']=sub
    msg['From']=send_mail_address
    msg['to']=to_adress="139SMSserver<"+get_mail_user+"@"+get_mail_postfix+">"
    try:
        stp = smtplib.SMTP()
        stp.connect(send_mail_host)
        stp.login(send_mail_user,send_mail_pswd)
        stp.sendmail(send_mail_address, to_adress, msg.as_string())
        stp.close()
        return True
    except Exception, e:
        print str(e)
        return False

'''
if __name__ == '__main__':

    if semd_mail('13581798781@139.com','A',''):
        print "发送成功"
    else:
        print '发送失败'
'''
