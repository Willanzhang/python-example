# -*- coding: utf-8 -*-
import scrapy
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from daili.items import DailiItem

class DailispiderSpider(scrapy.Spider):
    name = 'dailiSpider'
    allowed_domains = ['goubanjia.com/']
    # start_urls = ['http://www.goubanjia.com/']
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    url = "http://www.goubanjia.com/"
    # ./chromedriver 文件地址   此文件需要下载和当前浏览器对应的版本
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    print '*****************'

    def start_requests(self):

        item = DailiItem()
        self.driver.get(self.url)
        self.driver.save_screenshot("daili.png")
        time.sleep(1)

        # print driver.find_element_by_xpath
        cc = self.driver.find_elements_by_xpath("//tr[@class='success']/td[@class='ip'][1] | //tr[@class='warning']/td[@class='ip'][1]")
        print '================================================='
        print cc
        for each in cc:
            print '*****************'
            # ip = "".join(each.xpath('.//span/text() | .//div/text()').extract())
            # ip = each.find_elements_by_xpath('.//span/text() | .//div/text() | ./text()').extract()
            # https://www.cnblogs.com/devtester/p/8550119.html
            # https://blog.csdn.net/wzyaiwl/article/details/89001219
            ip = each.text
            # ip = each.extract()
            item['ip_port'] = ip
            print ip
            # ip = each.text
            with open('ip.json', 'a+') as f:
                f.write(ip+ '\n')
        # yield item

    def close_spider(self, spider):
        self.driver.quit()
        # self.file.close()
    # def parse(self, response):
    #     print '----------------------------'
    #     cc = response.xpath("//tr[@class='success']/td[@class='ip'][1] | //tr[@class='warning']/td[@class='ip'][1]")
    #     for each in cc:
    #         print '*****************'
              # 网站做了 防爬 端口 好通过 js 修改过
    #         # ip = "".join(each.xpath('.//span/text() | .//div/text()').extract())
    #         # ip = each.xpath('.//span/text() | .//div/text() | ./text()').extract()
    #         ip = each.extract()
    #         print ip
    #         # ip = each.text
    #         with open('ip.json', 'a+') as f:
    #             f.write(ip)
