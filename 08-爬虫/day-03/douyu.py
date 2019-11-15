#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   douyu.py
@Time    :   2019/11/14 19:32:43
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib
# 测试模块
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup as bs

# 测试模块
class douyu(unittest.TestCase):
	# 初始化方法
	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')
		self.driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
		self.number = 0
		# self.driver = webdriver.PhantomJS()
	# 测试方法必须有test字样开头
	def testDouyu(self):

		self.driver.get("https://www.douyu.com/directory/all")
		try:
			while True:
				print '---------'
				soup = bs(self.driver.page_source, 'lxml')
				# 房间名 返回都是列表
				names = soup.find_all("h3", {"class": "DyListCover-intro"})
				# 观众人数 热度 返回列表
				numbers = soup.find_all("span", {"class": "DyListCover-hot"})
				# zip(names, numbers) 将name 和 numbers 这两个列表合并为一个元组： [(1,2),(3,4)...]
				for name, number in zip(names, numbers):
					print u"房间热度" + number.get_text() + u"\t房间名：" + name.get_text()
					self.number += 1

				# 如果在页面源码找到 disabledd 的类名 就跳出
				if (self.driver.page_source.find("dy-Pagination-disabled dy-Pagination-next") != -1):
					break
				self.driver.find_element_by_class_name(" dy-Pagination-next").click()
		except:
			pass

	#测试结束后执行的方法
	def tearDown(self):
		print "主播数量%d"%self.number
		# 跳出浏览器
		self.driver.quit()
if __name__ == "__main__":
	# 启动测试模块
	unittest.main()


# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')


# url = "https://www.douyu.com/directory/all"
# # 使用 bs4
# # title: h3 class=DyListCover-intro  find_all("h3", {"calss": "DyListCover-intro"})
# # tag: span calss=DyListCover-zone  find_all("span", {"calss": "DyListCover-zone"})
# # user: h2 class=DyListCover-user find_all("span", {"calss": "DyListCover-user"})
# # hot: span class=DyListCover-hot

# # nextpage 下一页不可点： li class=dy-Pagination-disabled dy-Pagination-next
# # nextpage 下一页可以点击： li class= dy-Pagination-next
# # ./chromedriver 文件地址
# driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
# # driver = webdriver.PhantomJS()
# # driver.set_window_size(1400, 900)
# driver.get(url)

# # 输入账号密码
# # driver.find_element_by_name("form_email").send_keys("xxxxx@xxxx.com")
# # driver.find_element_by_name("form_password").send_keys("xxxxxxxx")

# # title = driver.find_elements_by_class_name("DyListCover-intro")
# # print title

# driver.save_screenshot("douyu.png")
# print driver.find_elements_by_class_name("DyListCover-intro")
# # if (driver.page_source.find("dy-Pagination-disabled") != -1):
# #     break

# # 模拟点击登录
# # driver.find_element_by_xpath("//input[@class='bn-submit']").click()

# # # 等待3秒
# # time.sleep(3)

# # with open("douban.html", "w") as file:
# #     file.write(driver.page_source)