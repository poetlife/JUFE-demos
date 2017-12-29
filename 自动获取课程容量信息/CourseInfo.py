# coding=utf-8
# __author__ = "Peng Jidong"
import rsa
import binascii
import requests
from bs4 import BeautifulSoup
import sys
import os

import pandas as pd  # use this as store way

import optparse  # command line tools
from random import randint  # random tools


# this code attemps to get the new info with course
class LoginToCampus:
    def __init__(self, student_num, password):
        self.student_num = student_num
        self.password = password
        self.jufe_session = requests.session()
        self.headers = {
                        'Host': 'ssl.jxufe.edu.cn',
                        'Origin': 'https://ssl.jxufe.edu.cn',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
                                       51.0.2704.84 Safari/537.36',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                        'Referer': ""
        }
        self.data = {
                    "username": self.student_num,  # refill later
                    "password": "",  # refill later
                    "errors": "0",
                    "imageCodeName": "",
                    "_rememberMe": "on",
                    "cryptoType": "1",
                    "lt": "_c01C8161C-458D-5ABA-AD27-55438D2520B1_kA3BE3356-EFCD-0846-620D-74F8AB074C99",
                    "_eventId": "submit"
        }
        self.login_url = "https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal" \
                         "%2Flogin%3Fredirect%3D%252Fc"

    def _crypto(self):
        # operate RSA encryption for the password
        n = '5598e3b75d21a2989274e222fa59ab07d829faa29b544e3a920c4dd287aed9302a657280c23220a35ae985ba157400e0502ce8e445' \
            '70a1513bf7146f372e9c842115fb1b86def80e2ecf9f8e7a586656d12b27529f487e55052e5c31d0836b2e8c01c011bca911d983b1' \
            '541f20b7466c325b4e30b4a79652470e88135113c9d9'  # 256-bit hex
        e = '10001'  # hex

        public_key = rsa.PublicKey(int(n, 16), int(e, 16))
        encrypted_password = rsa.encrypt(self.password.encode(), public_key)
        encoded_password = binascii.b2a_hex(encrypted_password)  # 将bytes转化为16进制

        return encoded_password

    def _valid_login(self):
        # 验证是否登录成功
        s = self.jufe_session
        login = s.get(self.login_url, headers=self.headers)
        bsObj_login = BeautifulSoup(login.text, 'lxml')
        self.data['lt'] = bsObj_login.find_all('input', {'name': 'lt'})[0].get('value')  # update the lt in the data
        form_url = bsObj_login.find_all("form", {"id": "fm1"})[0].get("action")
        form_url = 'https://ssl.jxufe.edu.cn' + form_url

        # post
        self.headers['Referer'] = 'https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn' \
                                  '%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fc'
        s.post(form_url, data=self.data, allow_redirects=True)

        # 通过访问一个需要权限的页面来判断是否登录成功
        result = s.get('http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1')
        if result.url.split(":")[0] == "http":
            return s
        else:
            return False

    def run(self):
        self.data['password'] = self._crypto()
        s = self._valid_login()
        if s:
            print('[+] login successfully!')
        else:
            print('[-] failed to login! And system will exit soon!')
            sys.exit()


class QueryCourseData:
    def __init__(self, search, term=172, search_by='CourseCode', do_search='查询'):
        # data为
        # searchContext:01032
        # term:172
        # searchBy:CourseCode
        # doSearch:查询
        self.searchContext = search
        self.term = term
        self.searchBy = search_by
        self.doSearch = do_search


class CourseInfo(LoginToCampus):
    def __init__(self, student_num, password):
        super(CourseInfo, self).__init__(student_num, password)
        self.teacher_url = "http://xfz.jxufe.edu.cn/portal/main.xsp/page/-2"
        self.course_url = "http://xfz.jxufe.edu.cn/portal/main.xsp/page/-2/?.a.p=aT0lMkZ4Znpwb3J0YWwlMkZpbmZvcjRBbGwm" \
                          "dD1yJnM9bm9ybWFsJmVzPWRldGFjaCZtPXZpZXc%3D&mlinkf=infor4All%2Findex.jsp"
        self.classmates_url = "http://xfz.jxufe.edu.cn/portal/main.xsp/page/-2/?.a.p=aT0lMkZ4Znpwb3J0YWwlMkZpbmZvcjRB" \
                              "bGwmdD1yJnM9bm9ybWFsJmVzPXBudWxsJm09dmlldw%3D%3D&mlinkf=infor4All%2FselectClassStudent.jsp"
        super(CourseInfo, self).run()  # 获取登录信息
        self._inner_process1()  # 防止系统判定非人为访问
        self.head_rows = []
        self.context = []

    def _inner_process1(self):
        # 按顺序访问网址，防止出错,访问完毕之后，可以开始post数据了
        link1 = self.jufe_session.get(self.teacher_url)
        if link1.status_code == 200:
            print('[+] teacher channel login successfully!')
        link2 = self.jufe_session.get(self.course_url)
        if link2.status_code == 200:
            print('[+] query course channel entry successfully!')

    def _parse_course_headers(self, requests_obj):  # competed
        # 抓取表格头部
        bsObj = BeautifulSoup(requests_obj.text, 'lxml')  # 基本的组件
        table = bsObj.find('table', {'class': 'Table'})  # 唯一的目标，2017年12月份系统
        thead_tr = table.find('thead').find_all('td')
        for item in thead_tr:
            # 遍历
            self.head_rows.append(item.get_text())

    def _parse_course_context(self, requests_obj):
        # 用来解析得到的网页
        bsObj = BeautifulSoup(requests_obj.text, 'lxml')  # 基本的组件
        tbody = bsObj.find('table', {'class': 'Table'}).find('tbody')
        # 遍历tr，再遍历td
        trs = tbody.find_all('tr')
        for tr in trs:
            single_row = []
            # 每一条记录
            for item in tr.find_all('td'):
                single_row.append(item.get_text())
            self.context.append(single_row)

    def _combine_data_2_pandas(self, path):
        self.final_data = pd.DataFrame(self.context, columns=self.head_rows)
        self.final_data.to_excel(path)

    def query_course_with_code_list(self, code_list, path):
        # 传递一个代码列表, 先处理headers
        temp = QueryCourseData(code_list[0]).__dict__
        query_result = self.jufe_session.post(self.course_url, data=temp)
        self._parse_course_headers(query_result)
        # 然后再处理context
        for i in code_list:
            result = self.jufe_session.post(self.course_url, data=QueryCourseData(i).__dict__)
            self._parse_course_context(result)
        self._combine_data_2_pandas(path)

    def query_course(self, code, path):
        # current only support query course by code, term default is '172'
        data = QueryCourseData(code).__dict__
        query_result = self.jufe_session.post(self.course_url, data=data)
        self._parse_course_headers(query_result)
        self._parse_course_context(query_result)
        self._combine_data_2_pandas(path)

    def test(self):
        pass


def read_text(path):
    # 读取文本文档
    result = []
    with open(path) as f:
        list = f.read()
        for i in list.split('\n'):
            if len(i) == 5:
                result.append(i)
    return result


# command line tools, attempt to neglect
def main():
    # 用来初始化命令行参数页面
    parser = optparse.OptionParser('Usage %prog ' + '-u <username> -p <password>')
    parser.add_option('-u', '--username', dest='username', type='string', help='enter your username/student number...')
    parser.add_option('-p', '--password', dest='password', type='string', help='enter your password, enter to compete...')
    parser.add_option('-p1', '--path1', dest='path1', type='string', help='enter your original info path...')
    parser.add_option('-p2', '--path2', dest='path2', type='string', help='enter your target path...')

    opts, args = parser.parse_args()
    print('your information entered as follows:\n  --username: %s\n  --password: %s\n  --path1: %s\n  --path2: %s' %
          (opts.username, opts.password, opts.path1, opts.path2))
    prompt = input('enter y to continue, n to cancel: ')
    if prompt == 'y':
        print('go on to execute the program, maybe need a long time to compete...')
        # check the valid of the path
        if os.path.exists(opts.path1) and os.path.exists(opts.path2):
            c = CourseInfo(opts.username, opts.password)  # instance
            c.query_course_with_code_list(read_text(opts.path1), opts.path2)
        else:
            print('path is invalid!System will exit soon!')
            sys.exit()
    elif prompt == 'n':
        print('exit...')
        sys.exit()
    else:
        print('invalid arguments...\n the system will exit soon...')
        sys.exit()


if __name__ == '__main__':
    main()