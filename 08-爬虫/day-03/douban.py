#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   douban.py
@Time    :   2019/11/14 19:32:43
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
url = "https://www.douban.com/"
# ./chromedriver 文件地址
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
# driver.set_window_size(1400, 900)

driver.get(url)
driver.save_screenshot("douban.png")