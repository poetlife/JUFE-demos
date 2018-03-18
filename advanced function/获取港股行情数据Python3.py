# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:10:03 2018

@author: Administrator
@description: get the trade data of the HK market...
@modified: 2018-3-18 22:10:39

"""

import requests
import pandas as pd
import re
import json

class Date:
    """
    allowed format:
        2018-03-18
    """
    def __init__(self, date):
#        print("init data is: ", date)
        date = date.split("-")
        if len(date) != 3:
            raise ValueError("you entered the wrong date type!")
        self.year = int(date[0])
        self.month = int(date[1])
        self.day = int(date[2])


def parseDate(bgdate, eddate):
    
    def construct_date(year, month, day):
        return "%s-%s-%s"%(year, month, day)
    
    # 起始日期， 结束日期
    bg = vars(Date(bgdate))  # start
    ed = vars(Date(eddate))  # end
    
    spread = ed.get("year") - bg.get("year")
    if spread > 1:
        # parse to a list contained the date annually
        bgs = []
        eds = []
        for i in range(1, spread):
            bgs.append(construct_date(bg.get("year") + i -1,
                                      bg.get("month"),
                                      bg.get("day")))
            eds.append(construct_date(bg.get("year") + i,
                                      bg.get("month"),
                                      bg.get("day")))
        bgs.append(construct_date(bg.get("year") + spread - 1,
                                      bg.get("month"),
                                      bg.get("day")))
        eds.append(construct_date(ed.get("year"),
                                      ed.get("month"),
                                      ed.get("day")))
        # zip
        data = list(zip(bgs, eds))
        return data
    else:
        return [(bgdate, eddate)]


# main func
class HKStock():
    """
    get data and export it to csv format
    """
    
    def __init__(self, code, bgdate, eddate):
        a = self.get_dq(code=code, bgdate=bgdate, eddate=eddate)
        a.to_csv("./sample%s.csv"%(code))
    
    def get_dq(self, code, mkt="AUTO", bgdate="2000-01-01", eddate="2018-12-31", fq=None):
        if mkt == "AUTO":
            if re.search('^\d{5}',code):
                mkt='hk'
            elif re.search('^6\d{5}',code):
                mkt='sh'
            elif re.search('^0|3\d{5}',code):
                mkt='sz'
            code_par= mkt +code
            print ('get dq of %s.%s[from:%s, to:%s]' % (code, mkt, bgdate,eddate))
            
        def to_url(date_list):
            if fq==None:
                urls = []
                for i in date_list:
                    url= 'http://web.ifzq.gtimg.cn/appstock/app/kline/kline?_var=kline_day&param=%s,day,%s,%s,640,' % (code_par, i[0],i[1])
                    urls.append(url)
                dataname='day'
                return (urls, dataname)
            else:
                """
                暂时未碰到这种情况，所以不处理
                """
                assert fq in ['qfq','hfq']
                url= 'http://web.ifzq.gtimg.cn/appstock/app/hkfqkline/get?_var=kline_day&param=%s,day,%s,%s,640,%s' % (code_par, bgdate,eddate, fq)
                dataname= fq+ 'day'
                pass
        
        date = to_url(parseDate(bgdate, eddate))
        dataname = date[1]
        # 使用循环获取数据
        pandas_data = []
        for url in date[0]:
            
            cn=requests.get(url)  # 可以在这里得到港股的数据，然后需要解析至Json
            print(url)
            js= re.search('(?<=kline_day=).*', cn.text).group()
            jsparsed=json.loads(js)
            dq=pd.DataFrame(jsparsed['data'][code_par][dataname])
            if dq.shape[1]==6:
                dq.columns= ['date','open','close','high','low','volume']
            elif dq.shape[1]==7:
                dq.columns= ['date','open','close','high','low','volume','qy']
            pandas_data.append(dq)
            
        # concat the data
        df = pd.concat(pandas_data)
        return df
    
a = HKStock("00992", "2001-09-01", "2011-09-30")
        




