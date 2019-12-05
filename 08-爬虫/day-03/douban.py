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
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
url = "https://www.douban.com/"
# ./chromedriver 文件地址   此文件需要下载和当前浏览器对应的版本
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
# driver.set_window_size(1400, 900)
driver.get(url)

# # 输入账号密码
# driver.find_element_by_name("form_email").send_keys("xxxxx@xxxx.com")
# driver.find_element_by_name("form_password").send_keys("xxxxxxxx")

# # 模拟点击登录
# driver.find_element_by_xpath("//input[@class='bn-submit']").click()

driver.save_screenshot("douban.png")


# 等待3秒
time.sleep(3)

# driver 滚动 到 10000
js = "window.scrollTo(0, 10000)"

driver.execute_script(js)

driver.save_screenshot("newdouban.png")

# 关闭浏览器
driver.quit()
# with open("douban.html", "w") as file:
#     file.write(driver.page_source)