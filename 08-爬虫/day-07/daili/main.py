#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/11/29 10:48:17
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib

# from scrapy import cmdline
# cmdline.execute('scrapy crawl dailiSpider'.split())

import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import redis
import time

REDIS_URL = 'redis://root:123456@47.106.156.14:6379'


def crawlDaili():
    reds = redis.Redis.from_url(REDIS_URL, db=0, decode_responses=True)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    url = "http://www.goubanjia.com/"
    # ./chromedriver 文件地址   此文件需要下载和当前浏览器对应的版本
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver.get(url)
    driver.save_screenshot("daili.png")
    time.sleep(1)
    # print driver.find_element_by_xpath
    cc = driver.find_elements_by_xpath("//tr[@class='success']/td[@class='ip'][1] | //tr[@class='warning']/td[@class='ip'][1]")
    print '================================================='
    print cc

    score = 1 / int(time.time())
    for index in range(0, len(cc)):
        print '*****************'
        each = cc[index]
        ip = each.text
        score += index
        print ip
        # reds.set('ip' + str(time.time()), ip)
        # 不使用列表
        # reds.lpush('ip', ip)
        # 使用集合方便去重 sudo pip install redis==2.10.6    redis版本过高会出问题
        reds.zadd('ips', ip, score)
        #  zrange ips 0 0  取第一个
        # ip = each.text
        # with open('ip.json', 'a+') as f:
        #     f.write(ip+ '\n')
    driver.quit()

if __name__ == '__main__':
    print '-----------crawl start-----------'
    crawlDaili()