#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import scrapy
from douyu.items import DouyuItem
import json

class DouyuspiderSpider(scrapy.Spider):
    name = 'douyuSpider'
    allowed_domains = ['capi.douyucdn.cn']

    offset = 20
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='

    start_urls = [url + str(offset)]

    def parse(self, response):
        # 把json格式的数据转换为python格式， data段是列表
        # data = json.loads(response.text).get('data')
        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuItem()
            item['nickname'] = each['nickname']
            item['imageLink'] = each['vertical_src']

            yield item
        
        self.offset += 20
        # yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
