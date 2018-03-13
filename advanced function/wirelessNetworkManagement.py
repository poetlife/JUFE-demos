# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 11:58:30 2018
this file aims to modify the wireless network experience
@author: Administrator
"""

import requests
import lxml.etree  # faster
import webbrowser as browser  # invoking a web browser to get the image captcha

url_0 = "http://172.31.5.249"  # base
url_1 = "http://172.31.5.249/wlan_self/"  # 无线网登录平台
url_2 = "http://172.31.5.249/wlan_self/a.html"  # 登录
url_3 = "http://172.31.5.249/wlan_self/user_login.php"  # 无线网管理平台
url_4 = "http://172.31.5.249/wlan_self/index.php"  # 登录成功后的页面
url_5 = "http://172.31.5.249/wlan_self/user_logout.php?the_type=0"  # logout

login_data = {
        "ykt_user_id": "",
        "ykt_password": "",
        "6_letters_code": "",
        "Submit": "+%C8%B7%B6%A8+"
        }  # 登录的数据

guest_data = {
        "user_id_phone": "",
        "guest_wlan_password":"",
        "guest_fullname" : "exampleName",
        "guest_email": "example@example.com",
        "guest_address": "guestAddress",
        "select_days": "24",
        "6_letters_code": "",  # 验证码
        "Submit": "+%C8%B7%B6%A8+"
        }

repassword_data = {
        "m_password": "",
        "m_password2": "",
        "6_letters_code": "",
        "Submit": "+%C8%B7%B6%A8+"
        }

offline_data = {
        "6_letters_code": "",
        "ip": "",
        "s_id": "",
        "nas_ip": "",
        "Submit": "+%C7%BF%D6%C6%CF%C2%CF%DF+"
        }

configXpath = {
        "login_captcha": '//*[@id="captchaimg"]'
        }

class CrawerWirelessNetWork():
    # 爬虫类
    def __init__(self, username, password):
        self.username = username  # 用户名
        self.password = password  # 密码
        self.s = requests.session()  # 使用自动化储存cookies的技术
        self.headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                }
    
    def login(self):
        # 登录无线网络管理中心
        text_login = self.s.get(url_3, headers=self.headers)
        captcha = url_0 + self.parseHtml(text_login.text).xpath(configXpath.get("login_captcha"))[0].get("src")
        result_captcha = self.parseCaptcha(captcha)
        login_data["ykt_user_id"] = self.username
        login_data["ykt_password"] = self.password
        login_data["6_letters_code"] = result_captcha
        result_login = self.s.post(url_3)
        if result_login.url == url_4:
            print("login successfully...")
        else:
            print("error...exit the program...")
        
    def parseHtml(self, html):
        obj = lxml.etree.HTML(html)
        return obj
    
    def parseCaptcha(self, captcha):
        # 识别验证码，并返回相关数据
        # 这种操作是错误的，因为这种情况下，不同次数访问的验证码仍然是不一样的，因此，这里需要使用session去下载这个验证码
        browser.open_new_tab(captcha)
        print("the browser is open... please enter the verification code ...")
        while True:
            result = input("result: ")
            if len(result) != 4:
                print("Error Captcha... plesase reenter later...")
            else:
                try:
                    int(result)
                    print("You enter the %s, and pass the examination program"%result)
                    break
                except ValueError:
                    print("Error Captcha... plesase reenter later...")
        return result
    
a = CrawerWirelessNetWork("2201503184", "858892")
b = a.login()