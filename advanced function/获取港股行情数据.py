
import requests
import json
import pandas as pd
import re

def get_dq(code='00005',mkt='AUTO', bgdate='2001-09-01',eddate='2018-03-15',fq=None):

	if mkt=='AUTO':
		if re.search('^\d{5}',code):
			mkt='hk'
		elif re.search('^6\d{5}',code):
			mkt='sh'
		elif re.search('^0|3\d{5}',code):
			mkt='sz'
		code_par= mkt +code
		print ('get dq of %s.%s[from:%s, to:%s]' % (code, mkt, bgdate,eddate))

	if fq==None:
		url= 'http://web.ifzq.gtimg.cn/appstock/app/kline/kline?_var=kline_day&param=%s,day,%s,%s,640,' % (code_par, bgdate,eddate)
		dataname='day'
	else:
		assert fq in ['qfq','hfq']
		url= 'http://web.ifzq.gtimg.cn/appstock/app/hkfqkline/get?_var=kline_day&param=%s,day,%s,%s,640,%s' % (code_par, bgdate,eddate, fq)
		dataname= fq+ 'day'


	cn=requests.get(url)  # 可以在这里得到港股的数据，然后需要解析至Json
	print(cn.text)
	js= re.search('(?<=kline_day=).*', cn.text).group()
	jsparsed=json.loads(js)
	dq=pd.DataFrame(jsparsed['data'][code_par][dataname])
	if dq.shape[1]==6:
		dq.columns= ['date','open','close','high','low','volume']
	elif dq.shape[1]==7:
		dq.columns= ['date','open','close','high','low','volume','qy']
	return dq

class HKStock():
	def __init__(self, code):
		temp = get_dq(code)
		# 自动保存在这个文件夹
		temp.to_csv("./%s.csv"%code)


a = HKStock("00992")