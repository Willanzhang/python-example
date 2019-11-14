#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   seleniumtext.py
@Time    :   2019/11/14 16:06:53
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib
# selenium 已经放弃 PhantomJS了，建议使用火狐或者谷歌无界面浏览器
# https://blog.csdn.net/u010358168/article/details/79749149   
# chromedriver 版本需要和本机装的浏览器版本向对应   https://sites.google.com/a/chromium.org/chromedriver/home
# selenium版本降级
# 通过pip show selenium显示，默认安装版本为3.8.1。 
# 将其卸载pip uninstall selenium，重新安装并指定版本号pip install selenium==2.48.0。

# 除了使用 selenimu 还可以是用   Puppeteer: pypeteer(Puppeteer 的python 版本) https://blog.csdn.net/freeking101/article/details/93331204

# 导入 webdriver
from selenium import webdriver

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# ./chromedriver 文件地址
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
driver.set_window_size(1400, 900)


# 如果没有在环境变量指定PhantomJS位置
# driver = webdriver.PhantomJS(executable_path="./phantomjs"))

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("https://www.baidu.com/")
# print driver.page_source
driver.find_element_by_id("kw").send_keys(u"长城")
driver.save_screenshot("baidu.png")
# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("head").text
# element = driver.find_element(by=By.ID, value="head")
# 打印数据内容
print data
