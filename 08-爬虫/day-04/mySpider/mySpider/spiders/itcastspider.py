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
# 导入 item文件 mySpider 是项目名
from mySpider.items import ItcastItem

# 創建一个爬虫类
class ItcastSpider(scrapy.Spider):
	# 爬虫名
	name = "itcast"
	# 允许爬虫作用的范围
	allowd_domains = ["http://www.itcast.cn/"]
	# 爬虫起始的url
	start_urls = ["http://www.itcast.cn/channel/teacher.shtml#aios"]
	    	
	def parse(self, response):
		# with open('teacher.html', 'w') as f:
		# 	f.write(response.body)
		teacher_list = response.xpath("//div[@class='li_txt']")

		# treacherItem = []
		for each in teacher_list:
			# 将我们得到的数据封装到一个 `ItcastItem` 对象
			item = ItcastItem()
    		# name.extract() 將匹配的结果转化为Unicode 字符串
			# 不加 extract() 结果为xpath 匹配对象
 			name = each.xpath("./h3/text()").extract()
			# title
			title = each.xpath("./h4/text()").extract()
			# info
			info = each.xpath("./p/text()").extract()

			item['name'] = name[0].encode('utf-8')
			item['title'] = title[0].encode('utf-8')
			item['info'] = info[0].encode('utf-8')

			# treacherItem.append(item)

			#将获取的数据交给pipelines 管道文件
			yield item

		# return treacherItem
