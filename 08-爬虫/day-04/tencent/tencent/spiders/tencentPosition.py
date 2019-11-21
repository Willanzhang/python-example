#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tencentPosition.py
@Time    :   2019/11/21 18:05:54
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib
import scrapy
from tencent.items import TencentItem
import json
import time
class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']

    # url = "https://careers.tencent.com/search.html?index="
    # offset = 1
    # start_urls = [
    #     url + str(offset)
    # ]
    page = 1
    url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1574306491995&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageSize=10&language=zh-cn&area=cn&pageIndex="
    # start_urls = ["https://careers.tencent.com/tencentcareer/api/post/Query"]
    start_urls = [url + str(page)]

    # 重载requset 
    # formRequst 是scrapy 发送post请求的方法
	# def start_requests(self):
    #     # get 请求
    #     yield scrapy.Request(url + str("?timestamp=1574306491995&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"), callback=self.parse)

    def parse(self, response):
        print "----------"
        res = json.loads(response.text)
        if (res.get('Code') == 200):
            data =  res.get('Data')["Posts"]
            for each in data:
                item = TencentItem()
                # 职位名称
                item['postionName'] = each['RecruitPostName']
                # 详情连接
                item['positionLink'] = each['PostURL']
                # 职位类别
                item['positionType'] = each['CategoryName']
                # 招聘人數
                item['peopleNum'] = each['RecruitPostId']
                # 工作地點
                item['workLocation'] = each['LocationName']
                # 发布时间
                item['publishTime'] = each['LastUpdateTime']

                print item
                yield item
        if self.page <= 10:
            self.page += 1
        
        time.sleep(2)
        print self.url + '****************************************'
        yield scrapy.Request(self.url + str(self.page), callback = self.parse)

        # xpath("//a/h4[@class='recruit-title'] | //a/h4") xpath 还可以使用或
        # for each in response.xpath("//a[@class='recruit-list-link']"):
		# 	item = TencentItem()
        #     # 职位名称
        #     postionName = each.xpath("./div[@class='recruit-title']/text()").extract()[0]
        #     # 详情连接
        #     positionLink = each.xpath("./div[@class='recruit-title']/text()").extract()[0]
        #     # 职位类别
        #     positionType = scrapy.Field()
        #     # 招聘人數
        #     peopleNum = scrapy.Field()
        #     # 工作地點
        #     workLocation = scrapy.Field()
        #     # 发布时间
        #     publishTime = scrapy.Field()
    

