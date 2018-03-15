# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 11:58:30 2018
this file aims to modify the wireless network experience
@author: Administrator
"""
from io import BytesIO
from PIL import Image  # process the image lib
from functools import wraps
import requests
import lxml.etree  # faster

url_0 = "http://172.31.5.249"  # base
url_1 = "http://172.31.5.249/wlan_self/"  # 无线网登录平台
url_2 = "http://172.31.5.249/wlan_self/a.html"  # 登录
url_3 = "http://172.31.5.249/wlan_self/user_login.php"  # 无线网管理平台
url_4 = "http://172.31.5.249/wlan_self/index.php"  # 登录成功后的页面
url_5 = "http://172.31.5.249/wlan_self/user_logout.php?the_type=0"  # logout
url_6 = "http://w.jxufe.edu.cn/wlan_self/index.php"  # 申请来宾账户
url_7 = "http://w.jxufe.edu.cn/ifvalid/jxcd_captcha_code_file.php?rand=2030335763"  # 获取一个验证码

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
        self.status = False  # 登录状态
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
        print(self.s.cookies)
        captcha = url_0 + self.parseHtml(text_login.text).xpath(configXpath.get("login_captcha"))[0].get("src")
        result_captcha = self.parseCaptcha(captcha)
        login_data["ykt_user_id"] = self.username
        login_data["ykt_password"] = self.password
        login_data["6_letters_code"] = result_captcha
        result_login = self.s.post(url_3, data=login_data)
        if result_login.url == url_4:
            print("login successfully...")
        else:
            # 由于存在编码问题，显示不了中文，因此重新进行编码解码
            # fu*********k, 网页使用的是gb2312编码
            text = result_login.content.decode("gb2312")
            if "一卡通认证失败，请重新输入相关信息，请返回！" in text:
                print("用户名或者密码输入错误！")
            else:
                print("验证码输入错误！")
                
    def addGuestAccount(self, user_id_phone="13812345678",
                        guest_wlan_password="123456",
                        guest_email="example@example.com",
                        guest_fullname="exampleName",
                        guest_address="guestAddress"):
        # 2018-3-15 15:23:44 remain unsolved
        
        self.s.get(url_6)
        # 添加来宾账户
        global guest_data
        guest_data["user_id_phone"] = user_id_phone
        guest_data["guest_wlan_password"] = guest_wlan_password
        guest_data["guest_email"] = guest_email
        guest_data["guest_address"]= guest_address
        guest_data["guest_fullname"] = guest_fullname
        # 这里需要获取一个验证码
        guest_data["6_letters_code"] = self.parseCaptcha(url_7)
        # 使用session post
        result = self.s.post(url_6, data=guest_data)
        # 判断是否成功
        print(result.content.decode("gb2312"))
    
    def removeGuestAccount(self,):
        pass
        
    def parseHtml(self, html):
        obj = lxml.etree.HTML(html)
        return obj
    
    def parseCaptcha(self, captcha):
        # 识别验证码，并返回相关数据
        # 这种操作是错误的，因为这种情况下，不同次数访问的验证码仍然是不一样的，因此，这里需要使用session去下载这个验证码
        # 换用了session()操作获取验证码依然是错误的操作模式 2018-3-13 18:56:55
        # 进一步分析发现，带cookies的http请求会造成验证码刷新，实际上，爬取处理图片的URL没有意义，
        # 可以直接带cookies的请求会更高效
        # already solved
        im_captcha = self.s.get(captcha)
        file_captcha = BytesIO(im_captcha.content)
        '''
        可以去除这段IO操作，以减少性能的消耗
        if os.path.exists("./temp.jpg"):
            os.remove("./temp.jpg")
        with open("./temp.jpg", "wb") as f:
            f.write(im_captcha.content)
        '''
        image = Image.open(file_captcha)
        image.show()
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
    
    
a = CrawerWirelessNetWork("2201503184", "000000")
b = a.login()
c = a.addGuestAccount()