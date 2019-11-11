#!/usr/bin/env python

import urllib2
import json

import jsonpath
import chardet


url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request = urllib2.Request(url, headers = headers)

response = urllib2.urlopen(request)

#  取出json文件里的内容，返回的格式是字符串
html =  response.read()
print html