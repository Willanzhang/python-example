# -*- coding: utf-8 -*-
import scrapy
import json
import time

class ItjuzispiderSpider(scrapy.Spider):
    name = 'itjuziSpider'
    allowed_domains = ['itjuzi.com']
    page = 1
    url = "https://www.itjuzi.com/api/companys"
    postData = {
        "city": [],
        "com_fund_needs": "",
        "hot_city": "",
        "keyword": "",
        "location": "",
        "page": str(page),
        "pagetotal": "152117",
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
        print "******************************"

        yield scrapy.FormRequest(
            url = self.url,
            formdata = self.postData,
            callback = self.parse,
            dont_filter = True
        )

    def parse(self, response):
        print '------------------------------'
        res = json.loads(response.text)
        print res
        pass
        # if (res.get('Code') == 200):
        #     data =  res.get('Data')["Posts"]
        #     for each in data:

        #         print item
        #         yield item
        if self.page <= 10:
            self.page += 1
        
        time.sleep(2)
        yield scrapy.FormRequest(
            url = self.url,
            formdata = self.postData,
            callback = self.parse
        )
    