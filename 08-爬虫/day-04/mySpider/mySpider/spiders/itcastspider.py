#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   itcastspider.py
@Time    :   2019/11/18 15:02:22
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib

import scrapy

# 創建一个爬虫类
class ItcastSpider(scrapy.Spider):
	# 爬虫名
	name = "itcast"
	# 允许爬虫作用的范围
	allowd_domains = ["http://www.itcast.cn/"]
	# 爬虫起始的url
	start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

	def parse(self, response):
		with open('teacher.html', 'w') as f:
			f.write(response.body)