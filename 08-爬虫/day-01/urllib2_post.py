#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2

# 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# 完整的headers
headers = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"X-Requested-With": "XMLHttpRequest",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

# 用户接口输入
key = raw_input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
# i=hello&
# from=AUTO&
# to=AUTO&
# smartresult=dict&
# client=fanyideskweb&
# salt=15549537269048&
# sign=3eaaf352aa535eb5bf4fbfe15d3d7b7d&
# ts=1554953726904&
# bv=94d71a52069585850d26a662e1bcef22&
# doctype=json&
# version=2.1&
# keyfrom=fanyi.web&
# action=FY_BY_REALTlME

formdata = {
	"i": key,
	"from": "AUTO",
	"to": "AUTO",
	"smartresult": "dict",
	"client": "fanyideskweb",
	"salt": "15549537269048",
	"sign": "3eaaf352aa535eb5bf4fbfe15d3d7b7d",
	"ts": "1554953726904",
	"bv": "94d71a52069585850d26a662e1bcef22",
	"doctype": "json",
	"version": "2.1",
	"keyfrom": "fanyi.web",
	"action": "FY_BY_REALTlME"
}

# 经过urlencode转码
data = urllib.urlencode(formdata)

# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib2.Request(url, data=data, headers=headers)

print urllib2.urlopen(request).read()
