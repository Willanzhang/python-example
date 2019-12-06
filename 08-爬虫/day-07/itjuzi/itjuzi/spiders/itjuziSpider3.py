# -*- coding: utf-8 -*-

# https://www.cnblogs.com/bk9527/p/10504883.html  middle 使用 selenium

# 使用了 无头浏览器 已经 自动 selenium
import scrapy
import json
import time
import sys
from itjuzi.items import ItjuziItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time



reload(sys)

sys.setdefaultencoding("utf-8")


class Itjuzispider3Spider(scrapy.Spider):
    name = 'itjuziSpider3'
    allowed_domains = ['itjuzi.com']


    def start_requests(self):
        """
        先登录桔子网
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        url = "https://www.itjuzi.com/login"
        # ./chromedriver 文件地址   此文件需要下载和当前浏览器对应的版本
        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)


        driver.get(url)
        driver.save_screenshot("juzi.png")

        text = driver.find_element_by_xpath("//div[@class='el-input']/input[@type='text']").send_keys("18566209878")
        passwd = driver.find_element_by_xpath("//div[@class='el-input']/input[@type='password']").send_keys("Zbw631871612")
        # 这里是完成了登录
        button = driver.find_element_by_xpath("//button[@class='el-button el-button--primary']").click()
        time.sleep(3)
        print 'sleep1111-----------------'
        seleniumCookies = driver.get_cookies()
        cookies_dict = {}
        for cookie in seleniumCookies:
            # 在保存成dict时，我们其实只要cookies中的name和value，而domain等其他都可以不要
            cookies_dict[cookie['name']] = cookie['value']
        
        # 这里就可以输出cookie 了
        print cookies_dict
        print 'sleep2222-----------------'

        driver.save_screenshot("new_juzi.png")
        # 关闭浏览器
        driver.quit()
        pass

        JUZI_USER = "18711665181"
        JUZI_PWD = "Zbw631871612"
        url = "https://www.itjuzi.com/api/authorizations"
        payload = {"account": JUZI_USER, "password": JUZI_PWD}
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