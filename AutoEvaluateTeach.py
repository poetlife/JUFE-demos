# coding: utf-8
# @ Author: xNathan
# @ GitHub: https://github.com/xNathan
# @ Date: 2015-12-11 23:24

# @modified by Peng Jidong on 2017-12-16 15:58:53
# - 适应了新版门户网的加密
# - 使用了命令行解析功能
# - [expectation] add multi thread to work quicker
"""Description
对本学期已选课程进行自动评教，简化复杂的填表过程。
适用对象：江西财经大学的学生
可以自由设定分值下限和上限，所有分数均为随机生成，作者不对评价客观真实性做保证。
本软件只供学习和参考，如果因为使用此软件而造成任何法律后果，作者不承担任何责任。
"""

import rsa
import binascii
import optparse
import requests
from bs4 import BeautifulSoup
import sys
from random import randint


class Original:
    """
    原作者写的程序，整合在了一个class里面，名称稍微有些变化
    """
    def __init__(self, session):
        self.min_grade = 86
        self.max_grade = 95
        self.login_url = 'http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1'
        self.base_url = 'http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1/?.a.p=aT0lMkZ4Znpwb3J0YWwlMkZwZ25ldyZ0PXImcz1ub3JtYWwmZXM9ZGV0YWNoJm09dmlldw==&mlinkf='
        self.post_url = self.base_url + 'pg/pg1.jsp'
        self.index_url = self.base_url + 'pg/index.jsp'

        self.post_data = {
            'courseName': '',  # 课程名称
            'teacherName': '',  # 老师姓名
            'courseCode': '',  # 课程代码
            'classNO': '',  # 班级代号
            'teachattitude': '',  # 教学态度
            'teachmethod': '',  # 教学水平
            'teacheffect': '',  # 教学效果
            'stmemo': '',  # 早退、表扬、建议
            'teachcontent': '',  # 课件评价
            'coursepleased': '',  # 课程价值
            'teachjc': '',  # 教材评价
            'jcmemo': '',  # 课程教材留言评价
            'coursememo': '',  # 课程设置留言评价
        }
        self.session = session  # 所有爬虫的基础

    def login(self):
        """登录百合信息平台"""
        try:
            # res = self.session.get(self.login_url)
            # return res.url == 'http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1'
            # examine before use this class, so cancel this examine
            return True
        except:
            return False

    def get_list(self):
        """获取课程列表"""
        page = self.session.get(self.index_url).text
        print('-------评教首页--------')
        print("首页长度为：", len(page))
        soup = BeautifulSoup(page, 'lxml')
        out_put = []
        for item in soup.find('table', class_='Table').findAll('tr'):
            out_put.append([i.get_text().encode('utf-8')
                            for i in item.findAll('td')])
        course_list = out_put[1:]  # 去除第一行表头
        return course_list

    def get_evaluate_list(self):
        """获取等待评教的课程列表"""

        # 先获取所有课程列表
        course_list = self.get_list()
        result = []
        for item in course_list:
            # item[-2] 有数据即已评教， 无数据则待评教
            if not item[-2]:
                result.append(item)
        return result

    def evaluate(self, courseCode, classNO,
                 courseName, teacherName):
        """进行评教
        Args:
            courseCode: 课程代码
            classNO: 班级代号
            courseName: 课程名称
            teacherName: 老师姓名
        Returns:
            Bool 值，True or False
            是否提交成功
        """

        self.post_data['courseCode'] = courseCode
        self.post_data['classNO'] = classNO
        self.post_data['courseName'] = courseName
        self.post_data['teacherName'] = teacherName

        self.post_data['teachattitude'] = randint(self.min_grade, self.max_grade + 1)
        self.post_data['teachmethod'] = randint(self.min_grade, self.max_grade + 1)
        self.post_data['teacheffect'] = randint(self.min_grade, self.max_grade + 1)
        self.post_data['stmemo'] = u'都有'.encode('utf-8')
        self.post_data['teachcontent'] = randint(self.min_grade, self.max_grade + 1)
        self.post_data['coursepleased'] = randint(self.min_grade, self.max_grade + 1)
        self.post_data['teachjc'] = randint(self.min_grade, self.max_grade + 1)
        self.post_data['jcmemo'] = u'教材适用'.encode('utf-8')
        self.post_data['coursememo'] = u'课程设置合理，易于接受'.encode('utf-8')
        res = self.session.post(self.post_url, data=self.post_data)
        return u'操作成功' in res.text

    def main(self):
        # 先登录
        if self.login():
            evaluate_list = self.get_evaluate_list()  # 获取待评教课程
            if evaluate_list:
                for item in self.get_evaluate_list():
                    courseCode = item[0]
                    classNO = item[1]
                    courseName = item[3]
                    teacherName = item[4]
                    print(courseCode, classNO, courseName, teacherName)
                    flag = self.evaluate(courseCode, classNO,
                                    courseName, teacherName)
                    if flag:
                        print('-----Success------\n')
                    else:
                        print('------Error-----\n')
            else:
                print('No course to evaluate')
        else:
            print('Login error')


class EvaluateTeach:
    def __init__(self, student_num, password):
        self.student_num = student_num
        self.password = password
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
        s = requests.session()
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

    def _auto_evaluate(self):
        # 自动评教，完全使用原作者的代码
        pass

    def run(self):
        self.data['password'] = self._crypto()
        s = self._valid_login()
        if s:
            print('[+] login successfully!')
        else:
            print('[-] failed to login! And system will exit soon!')
            sys.exit()

        # 进行自动评教
        original = Original(s)
        original.main()



def main():
    # 用来初始化命令行参数页面
    parser = optparse.OptionParser('Usage %prog ' + '-u <username> -p <password>')
    parser.add_option('-u', '--username', dest='username', type='string', help='enter your username/student number...')
    parser.add_option('-p', '--password', dest='password', type='string', help='enter your password, enter to compete...')
    opts, args = parser.parse_args()
    print('your information entered as follows:\n  --username: %s\n  --password: %s' %
          (opts.username, opts.password))
    prompt = input('enter y to continue, n to cancel: ')
    if prompt == 'y':
        print('go on to execute the program...')
        e = EvaluateTeach(opts.username, opts.password)
        e.run()
    elif prompt == 'n':
        print('exit...')
        sys.exit()
    else:
        print('invalid arguments...\n the system will exit soon...')
        sys.exit()



if __name__ == '__main__':
    main()
