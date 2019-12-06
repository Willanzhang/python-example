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
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NzU2MTI3MzUsImV4cCI6MTU3NTYxNjMzNSwibmJmIjoxNTc1NjEyNzM1LCJqdGkiOiJUVmZIcURITlk0V3RvMkpXIiwic3ViIjo3OTA4ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiRUtRbVNsIn0.Kw8LE8FMYe5m1QR7Ksi86BrtErzajO-WyaFR3flhGPI",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "_ga=GA1.2.1314880111.1575270132; _gid=GA1.2.275180730.1575450802; juzi_user=790885; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1575270133,1575278608,1575599663,1575604289; OUTFOX_SEARCH_USER_ID_NCOO=1755928536.6689773; _gat_gtag_UA_59006131_1=1; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1575612714; juzi_token=bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NzU2MTI3MzUsImV4cCI6MTU3NTYxNjMzNSwibmJmIjoxNTc1NjEyNzM1LCJqdGkiOiJUVmZIcURITlk0V3RvMkpXIiwic3ViIjo3OTA4ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiRUtRbVNsIn0.Kw8LE8FMYe5m1QR7Ksi86BrtErzajO-WyaFR3flhGPI",
        "CURLOPT_FOLLOWLOCATION": "true",
        "Host": "www.itjuzi.com",
        "Origin": "https://www.itjuzi.com",
        "Referer": "https://www.itjuzi.com/company",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    postData = {
        "city": [],
        "com_fund_needs": "",
        "hot_city": "",
        "keyword": "",
        "location": "",
        # "page": str(page),
        "page": page,
        # "pagetotal": str(pagetotal),
        "pagetotal": pagetotal,
        "per_page": 200,
        "prov": "",
        "round": [],
        "scope": "",
        "selected": "",
        "sort": "",
        "status": "",
        "sub_scope": "",
        "total": 0,
        "year": []
    }
# CURLOPT_FOLLOWLOCATION: true


    def start_requests(self):
        # url = "https://www.itjuzi.com/api/companys"
        print self.postData
        print "******************************"

        # 使用 scrapy.FormRequest formdata 不能包含 int 类型
        yield scrapy.Request(url=self.url,
                             method="POST",
                             body=json.dumps(self.postData),
                            #  meta={'token': token},
                             # 把Authorization参数放到headers中,
                             headers = self.headers,
                             callback=self.process_parse
                             )
        # yield scrapy.FormRequest(
        #     url = self.url,
        #     formdata = self.postData,
        #     callback = self.process_parse,
        #     dont_filter = True
        # )

    def process_parse(self, response):
        item = ItjuziItem()
        res = json.loads(response.text)
        # file = open("teach.json", "a+")
        # context = json.dumps(res, ensure_ascii= False)
        # file.write(context)
        print "FormRequest-------------------+++++++++"
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

        if self.page < 3:
            self.page += 1
            self.pagetotal = 152117
            postData = {
                "city": [],
                "com_fund_needs": "",
                "hot_city": "",
                "keyword": "",
                "location": "",
                # "page": str(self.page),
                "page": self.page,
                # "pagetotal": str(self.pagetotal),
                "pagetotal": self.pagetotal,
                "per_page": 200,
                "prov": "",
                "round": [],
                "scope": "",
                "selected": "",
                "sort": "",
                "status": "",
                "sub_scope": "",
                "total": 0,
                "year": []
            }
            time.sleep(2)
            print 'sleep _________________---------------------------------------------------------------'
            print postData
            yield scrapy.Request(url=self.url,
                        method="POST",
                        body=json.dumps(postData),
                    #  meta={'token': token},
                        # 把Authorization参数放到headers中,
                        headers = self.headers,
                        callback=self.process_parse
                        )
            # yield scrapy.FormRequest(
            #     url = self.url,
            #     formdata = postData,
            #     callback = self.process_parse,
            # )

    def deal_json(self, response):
        pass