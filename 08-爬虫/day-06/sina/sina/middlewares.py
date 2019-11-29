# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
import logging
from .utils import fetch_one_proxy

from settings import USER_AGENTS
from settings import PROXIES

# https://www.kuaidaili.com/pricing/#dps
# 非开放代理且未添加白名单，需用户名密码认证
username = "willian_zhangb"
password = "v17ezvhl"
proxy = fetch_one_proxy() # 获取一个代理

THRESHOLD = 3  # 换ip阈值
fail_time = 0  # 此ip异常次数
logger = logging.getLogger(__name__)
# 随机的User-Agent
class RandomUserAgent(object):
	def process_request(self, request, spider):
		useragent = random.choice(USER_AGENTS)
		#print useragent
		request.headers.setdefault("User-Agent", useragent)

class RandomProxy(object):
	def process_request(self, request, spider):
		
		# 这是使用了私密代理
		proxy_url = 'http://%s:%s@%s' % (username, password, proxy)
		request.meta['proxy'] = proxy_url  # 设置代理
		logger.debug("using proxy: {}".format(request.meta['proxy']))
		# 设置代理身份认证
		# Python3 写法
		# auth = "Basic %s" % (base64.b64encode(('%s:%s' % (username, password)).encode('utf-8'))).decode('utf-8')
		# Python2 写法
		auth = "Basic " + base64.b64encode('%s:%s' % (username, password))
		request.headers['Proxy-Authorization'] = auth

		# 这是使用独享代理
		"""
		proxy = random.choice(PROXIES)
		print '----------------'
		print proxy
		if proxy['user_passwd'] is None:
			# 没有代理账户验证的代理使用方式

			request.meta['proxy'] = "http://" + proxy['ip_port']

		else:
			# 对账户密码进行base64编码转换
			base64_userpasswd = base64.b64encode(proxy['user_passwd'])
			# 对应到代理服务器的信令格式里
			request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd

			request.meta['proxy'] = "http://" + proxy['ip_port']
		"""
	def process_response(self, request, response, spider):
		"""
			如果状态码异常，则增加ip异常次数
			当异常次数达到阈值, 则更换ip,
			此换ip策略比较简略, 仅供参考
		"""
		global fail_time, proxy, THRESHOLD
		if not(200 <= response.status < 300):
			fail_time += 1
			if fail_time >= THRESHOLD:
				proxy = fetch_one_proxy()
				fail_time = 0
		return response




"""
from scrapy import signals


class DoubanSpiderMiddleware(object):
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the spider middleware does not modify the
	# passed objects.

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_spider_input(self, response, spider):
		# Called for each response that goes through the spider
		# middleware and into the spider.

		# Should return None or raise an exception.
		return None

	def process_spider_output(self, response, result, spider):
		# Called with the results returned from the Spider, after
		# it has processed the response.

		# Must return an iterable of Request, dict or Item objects.
		for i in result:
			yield i

	def process_spider_exception(self, response, exception, spider):
		# Called when a spider or process_spider_input() method
		# (from other spider middleware) raises an exception.

		# Should return either None or an iterable of Request, dict
		# or Item objects.
		pass

	def process_start_requests(self, start_requests, spider):
		# Called with the start requests of the spider, and works
		# similarly to the process_spider_output() method, except
		# that it doesn’t have a response associated.

		# Must return only requests (not items).
		for r in start_requests:
			yield r

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)


class DoubanDownloaderMiddleware(object):
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the downloader middleware does not modify the
	# passed objects.

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_request(self, request, spider):
		# Called for each request that goes through the downloader
		# middleware.

		# Must either:
		# - return None: continue processing this request
		# - or return a Response object
		# - or return a Request object
		# - or raise IgnoreRequest: process_exception() methods of
		#   installed downloader middleware will be called
		return None

	def process_response(self, request, response, spider):
		# Called with the response returned from the downloader.

		# Must either;
		# - return a Response object
		# - return a Request object
		# - or raise IgnoreRequest
		return response

	def process_exception(self, request, exception, spider):
		# Called when a download handler or a process_request()
		# (from other downloader middleware) raises an exception.

		# Must either:
		# - return None: continue processing this exception
		# - return a Response object: stops process_exception() chain
		# - return a Request object: stops process_exception() chain
		pass

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)
"""