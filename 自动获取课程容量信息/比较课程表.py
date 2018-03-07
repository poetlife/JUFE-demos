# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:29:46 2018

@author: This file was aimed to generate a schedule with deginated number of students

"""
import requests
from bs4 import BeautifulSoup
import bs4

data = {"username":"2201503184",
        "password":"2090035994e1e9010134100000ca6d2153c375539a6144c985d72e4712fc3fbee5eb16026ceab8889d34d9c6c7f1c314fee48a949e301bead01009627382a5a023ed9c57937d1b544e721e6451ff98672bf8f22c44f222fdaa08f391d28cd8e8e1164d4f788f2a4b27768324b414d7e419c7ff0218e2aab3705c4672ea59e4c4",
        "errors":"0",
        "imageCodeName":"" , 
        "_rememberMe":"on",
        "cryptoType":"1",
        "lt":"_cC041A6D0-0FFF-6D45-0D91-BA3537852C93_k2DF1A51E-D7A1-FE7F-607E-A27D0CE6E970",
        "_eventId":"submit"}

login_url = "https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fc"
bkjw_url = "http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1"
cxsyxqkb_url = "http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1/?.a.p=aT0lMkZ4Znpwb3J0YWwlMkZzZWxlY3RTdWJqZWN0UmVzdWx0NFN0dWRlbnQmdD1yJnM9bm9ybWFs%0AJmVzPWRldGFjaCZtPXZpZXc%3D&mlinkf=showSchedule.jsp"


test_url = "http://www.jxufe.edu.cn"

s = requests.session()

r0 = s.get(login_url)
bsObj_login = BeautifulSoup(r0.text, 'lxml')
data['lt'] = bsObj_login.find_all('input', {'name': 'lt'})[0].get('value')

# 将get 的cookies继承

s.post(login_url, data=data, allow_redirects=True)

# 这里开始查询课表，这里提交的数据为post_data
def parse_table(table_bsObj):
    if isinstance(table_bsObj, bs4.element.Tag):
        # 这里的话如多是的话，基本类型应该没有问题
        thead = table_bsObj.find("thead")
        tbody = table_bsObj.find("tbody")
        result1 = parse_table_head(thead)
        result2 = parse_table_body(tbody)
        print(result1)
        print(result2)
        b = zip(result1, result2)
        return b
    else:
        print("传入类型有问题")
        return {}

def parse_table_head(table_head_bsObj):
    result = []
    if isinstance(table_head_bsObj, bs4.element.Tag):
        # 这里为True，基本类型应该没有问题
        table_head = table_head_bsObj.find_all("tr")
        if len(table_head) > 1:
            print("tableHead's length is over 1, can't parse, pass")
        elif len(table_head) == 0:
            print("cannot find table head, please fill right para")
        else:
            tr = table_head[0]
            tds = tr.find_all("td")
            for td in tds:
                result.append(td.get_text())
        return result
    else:
        print("传入类型有问题")
        return result

def parse_table_body(table_body_bsObj):
    result = []
    if isinstance(table_body_bsObj, bs4.element.Tag):
        # 这里为True，基本类型应该没有问题
        table_bodys = table_body_bsObj.find_all("tr")
        if len(table_bodys) == 0:
            print("cannot find table body, please fill right para")
        else:
            # 这里会涉及到多个tr/td标签的解析
            for tr in table_bodys:
                result2 = []
                tds = tr.find_all("td")
                for td in tds:
                    result2.append(td.get_text())
                result.append(result2)
        return result
    else:
        print("传入类型有问题")
        return result

data_schdule = {
        "studentCode": "0153184",
        "term": "172"
        }

s.get(bkjw_url)
s.get(cxsyxqkb_url)
result1 = s.post(cxsyxqkb_url, data=data_schdule)


class Schedule:
    # 个人的课表集
    def __init__(self, studentName):
        print("hello")
        self.name = studentName

class Class:
    # 这个类用来定义课程数据集
    def __init__(self):
        pass

style = "border:1px solid #CCCCCC;padding:5px;background:#F3F3F3 ;line-height : normal ;border-collapse:collapse;"

schdule_html = BeautifulSoup(result1.text, "lxml")
table = schdule_html.find("table",{"style": style})
a = parse_table(table)
