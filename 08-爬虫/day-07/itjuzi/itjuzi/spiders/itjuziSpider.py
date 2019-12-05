# -*- coding: utf-8 -*-
import scrapy
import json
import time
import sys
from itjuzi.items import ItjuziItem
reload(sys)

sys.setdefaultencoding("utf-8")

class ItjuzispiderSpider(scrapy.Spider):
    name = 'itjuziSpider'
    allowed_domains = ['itjuzi.com']
    page = 1
    pagetotal = 152117
    url = "https://www.itjuzi.com/api/companys"
    postData = {
        "city": [],
        "com_fund_needs": "",
        "hot_city": "",
        "keyword": "",
        "location": "",
        "page": str(page),
        "pagetotal": str(pagetotal),
        "per_page": "20",
        "prov": "",
        "round": [],
        "scope": "",
        "selected": "",
        "sort": "",
        "status": "",
        "sub_scope": "",
        "total": "0",
        "year": []
    }
# CURLOPT_FOLLOWLOCATION: true


    def start_requests(self):
        # url = "https://www.itjuzi.com/api/companys"
        print self.postData
        print "******************************"

        yield scrapy.FormRequest(
            url = self.url,
            formdata = self.postData,
            callback = self.process_parse,
            dont_filter = True
        )

    def process_parse(self, response):
        item = ItjuziItem()
        res = json.loads(response.text)
        # file = open("teach.json", "a+")
        # context = json.dumps(res, ensure_ascii= False)
        # file.write(context)
        print "FormRequest-------------------+++++++++"
        print res
        if (res.get('code') == 200):
            data =  res.get('data')["data"]
            for each in data:
                item["name"] = each["name"]
                # 省
                item["prov"] = each["prov"]
                # 市
                item["city"] = each["city"]
                # 注册公司名称
                item["registerName"] = each["register_name"]
                # 描述
                item["des"] = each["des"]
                # 口号
                item["slogan"] = each["slogan"]
                yield item

        if self.page <= 10:
            self.page += 1
            self.pagetotal = 152117
            postData = {
                "city": [],
                "com_fund_needs": "",
                "hot_city": "",
                "keyword": "",
                "location": "",
                "page": str(self.page),
                "pagetotal": str(self.pagetotal),
                "per_page": "20",
                "prov": "",
                "round": [],
                "scope": "",
                "selected": "",
                "sort": "",
                "status": "",
                "sub_scope": "",
                "total": "0",
                "year": []
            }
            time.sleep(2)
            print 'sleep _________________'
            print postData
            yield scrapy.FormRequest(
                url = self.url,
                formdata = postData,
                callback = self.process_parse,
            )

    def deal_json(self, response):
        pass