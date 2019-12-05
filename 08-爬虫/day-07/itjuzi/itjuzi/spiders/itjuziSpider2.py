# -*- coding: utf-8 -*-
import scrapy
import json
import time
import sys
from itjuzi.items import ItjuziItem
reload(sys)

sys.setdefaultencoding("utf-8")


class Itjuzispider2Spider(scrapy.Spider):
    name = 'itjuziSpider2'
    allowed_domains = ['itjuzi.com']


    def start_requests(self):
        """
        先登录桔子网
        """
        JUZI_USER = "18711665181"
        JUZI_PWD = "Zbw631871612"
        url = "https://www.itjuzi.com/api/authorizations"
        payload = {"account": JUZI_USER, "password": JUZI_PWD, "type": "pswd"}
        # 提交json数据不能用scrapy.FormRequest，需要使用scrapy.Request，然后需要method、headers参数
        yield scrapy.Request(url=url,
                             method="POST",
                             body=json.dumps(payload),
                             headers={'Content-Type': 'application/json'},
                             callback=self.parse
                             )

    def parse(self, response):
        # 获取Authorization参数的值
        token = json.loads(response.text)
        url = "https://www.itjuzi.com/api/investevents"
        payload = {
                "pagetotal": 0, "total": 0, "per_page": 20, "page": 1, "type": 1, "scope": "", "sub_scope": "",
                "round": [], "valuation": [], "valuations": "", "ipo_platform": "", "equity_ratio": [""],
                "status": "", "prov": "", "city": [], "time": [], "selected": "", "location": "", "currency": [],
                "keyword": ""
            }
        yield scrapy.Request(url=url,
                             method="POST",
                             body=json.dumps(payload),
                             meta={'token': token},
                             # 把Authorization参数放到headers中
                             headers={'Content-Type': 'application/json', 'Authorization': token['data']['token']},
                             callback=self.parse_info
                             )

    def parse_info(self, response):
        # 获取传递的Authorization参数的值
        token = response.meta["token"]
        # 获取总记录数
        total = json.loads(response.text)["data"]["page"]["total"]
        # 因为每页20条数据，所以可以算出一共有多少页
        if type(int(total)/20) is not int:
            page = int(int(total)/20)+1
        else:
            page = int(total)/20

        url = "https://www.itjuzi.com/api/investevents"
        for i in range(1,page+1):
            payload = {
                "pagetotal": total, "total": 0, "per_page": 20, "page":i  , "type": 1, "scope": "", "sub_scope": "",
                "round": [], "valuation": [], "valuations": "", "ipo_platform": "", "equity_ratio": [""],
                "status": "", "prov": "", "city": [], "time": [], "selected": "", "location": "", "currency": [],
                "keyword": ""
            }
            yield scrapy.Request(url=url,
                                 method="POST",
                                 body=json.dumps(payload),
                                 headers={'Content-Type': 'application/json', 'Authorization': token['data']['token']},
                                 callback=self.parse_detail
                                 )
       
    def parse_detail(self, response):
        infos = json.loads(response.text)["data"]["data"]      
        for each in infos:
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