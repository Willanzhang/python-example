#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用了线程库
import threading
from Queue import Queue
from lxml import etree
import requests
import json
import time
import re

class ThreadCrawl(threading.Thread):
	def __init__(self, threadName, pageQueue, dataQueue):
		# 下面两行都是父类初始化
		# threading.Thread.__init__(self)
		# 这里多重继承不需要修改 优先用super
		super(ThreadCrawl, self).__init__() 
		self.threadName = threadName
		self.pageQueue = pageQueue
		self.dataQueue = dataQueue
		self.headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
	   

	def run(self):
		print "启动" + self.threadName
		while not CRWAL_EXIT:
			try:
				# 取出一个数字， 先进先出
				# 可选参数block 默认值是True
				# 1 如果队列为空, block为True的话，不会结束，就会进入阻塞状态，直到队列有新的数据
				# 2 如果队列为空，block为flase的话， 就会掏出一个 Queue.emoty()的异常
				page = self.pageQueue.get(False)
				url = "http://www.lovehhy.net/Joke/Detail/QSBK/" + str(page) + "/"
				# .text 别忘记了
				content = requests.get(url, headers = self.headers).text
				time.sleep(1)
				self.dataQueue.put(content)
			except Exception as e:
				print e
				pass

		print "结束" + self.threadName
	
class ThreadParse(threading.Thread):
	def __init__(self, threadName, dataQueue, filename, lock):
		super(ThreadParse, self).__init__()
		self.threadName = threadName
		self.dataQueue = dataQueue
		self.filename = filename
		# 锁
		self.lock = lock

	def run(self):
		print "启动" + self.threadName
		while not PARSE_EXIT:
			try:
				# print self.dataQueue.get()

				# html = self.dataQueue.get()
				html = self.dataQueue.get(False)
				self.parse(html)
			except Exception as result:
				pass
		print "退出" + self.threadName

	
	def parse(self, html):

		# text = etree.HTML(html.decode('gbk', 'ignore').encode('utf-8'))
		text = etree.HTML(html)

		# text = etree.HTML(html)

		# 返回所有段子的结点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
		# node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

		arr = []

		# title 列表
		node_list = text.xpath('//div[@class="cat_llb"]/h3[@class="red"]/a')

		# 描述 列表
		desc_list = text.xpath('//div[@class="cat_llb"]/text()')

		# 文章内容列表
		content_list = text.xpath('//div[contains(@id, "endtext")]')
		for index in range(len(node_list)):
			try:
				title = node_list[index].text
				# content = content_list[index].text
				# 使用xpath(‘string(.)’)这种方式获取所有文本 
				content = content_list[index].xpath('string(.)')
				desc = desc_list[index]
				items = {
					"title": title,
					"content": content.lstrip(),
					"desc": desc,
					"time": desc.split(u"　　")[0],
					"click_num": re.compile("\d").search(desc.split(u"　　")[1]).group(0)
				}
				arr.insert(0,items)
				
				# with 后面有两个必须执行的操作：__enter__ 和 _exit__
				# 不管里面的操作结果如何，都会执行打开、关闭
				# 打开锁、处理内容、释放锁
				with self.lock:
					self.filename.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")
			except Exception as error:
				print error


CRWAL_EXIT = False
PARSE_EXIT = False
def man():
	# 页码的队列， 表示10个页面
	pageQueue = Queue(10)
	# 放入1~10个数字，先进先出
	for i in range(1, 11):
		pageQueue.put(i)
	
	# 采集结果（每页的HTML源码）的数据对列表，参数为空表示不限制
	dataQueue = Queue()

	filename = open("duanzi.json", 'a')

	# 创建锁
	lock = threading.Lock()

	# 三个采集线程的名字
	crawlList = ["采集线程1号", "采集线程2号", "采集线程3号"]


	# 存储三个采集线程的列表集合
	threadCrawl = []
	for threadName in crawlList:
		thread = ThreadCrawl(threadName,  pageQueue, dataQueue)
		# start 对应这个 ThreadCrawl类中的run
		thread.start()
		threadCrawl.append(thread)


	# 三个解析线程的名字
	parseList = ["解析线程1号", "解析线程2号", "解析线程3号"]
	# 存储三个解析线程
	threadparse = []
	for threadName in parseList:
		thread = ThreadParse(threadName, dataQueue, filename, lock)
		thread.start()
		threadparse.append(thread)

	# 等待pageQueue队列为空， 也就是等待之前的操作执行完毕
	while not pageQueue.empty():
		pass

	# 如果pageQueue为空，采集线程退出循环
	global CRWAL_EXIT
	CRWAL_EXIT = True

	print "pageQueue为空"

	# 前面创建的是非守护线程， 守护线程是主线程结束，字线程结束，所以这里要加一个阻塞状态
	for thread in threadCrawl:
		thread.join()
		print "1"

	while not dataQueue.empty():
		pass


	global PARSE_EXIT
	PARSE_EXIT = True

	for thread in threadparse:
		thread.join()
		print "2"

	with lock:
		# 关闭文件
		filename.close()
	print "谢谢使用！"


if __name__ == "__main__":
	man()