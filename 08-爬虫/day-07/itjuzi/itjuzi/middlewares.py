# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random
import base64
import logging
import time
from .utils import fetch_one_proxy
from scrapy.downloadermiddlewares.retry import RetryMiddleware

from settings import USER_AGENTS
from settings import PROXIES

# https://www.kuaidaili.com/pricing/#dps
# 非开放代理且未添加白名单，需用户名密码认证
username = "willian_zhangb"
password = "v17ezvhl"
# proxy = fetch_one_proxy() # 获取一个代理

THRESHOLD = 3  # 换ip阈值
fail_time = 0  # 此ip异常次数
logger = logging.getLogger(__name__)
# curl 'https://www.itjuzi.com/api/companys' 

# -H 'Connection: keep-alive' 
# -H 'Accept: application/json, text/plain, */*' 
# -H 'Origin: https://www.itjuzi.com' 
# -H 'Authorization: "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NzU1OTk4MDAsImV4cCI6MTU3NTYwMzQwMCwibmJmIjoxNTc1NTk5ODAwLCJqdGkiOiJHUHVOWHJQckhJMU1IWDllIiwic3ViIjo3OTA4ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiZldvQVhkIn0.H-PgP7igZ38nEN0jkq0sABdCr86-7DcyNJhbnoCQqng"' 
# -H 'CURLOPT_FOLLOWLOCATION: true' 
# -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36' 
# -H 'Content-Type: application/json;charset=UTF-8' 
# -H 'Sec-Fetch-Site: same-origin' 
# -H 'Sec-Fetch-Mode: cors' 
# -H 'Referer: https://www.itjuzi.com/company' 
# -H 'Accept-Encoding: gzip, deflate, br' 
# -H 'Accept-Language: zh-CN,zh;q=0.9' 
# -H 'Cookie: _ga=GA1.2.1314880111.1575270132; _gid=GA1.2.275180730.1575450802; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1575270133,1575278608; juzi_user=790885; juzi_token=bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NzU1OTk4MDAsImV4cCI6MTU3NTYwMzQwMCwibmJmIjoxNTc1NTk5ODAwLCJqdGkiOiJHUHVOWHJQckhJMU1IWDllIiwic3ViIjo3OTA4ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiZldvQVhkIn0.H-PgP7igZ38nEN0jkq0sABdCr86-7DcyNJhbnoCQqng; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1575599813; _gat_gtag_UA_59006131_1=1' --data-binary '{"pagetotal":152299,"total":0,"per_page":20,"page":3,"scope":"","sub_scope":"","round":[],"location":"","prov":"","city":[],"status":"","sort":"","selected":"","year":[],"hot_city":"","com_fund_needs":"","keyword":""}' --compressed
# 随机的User-Agent
class RandomUserAgent(object):

    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        #print useragent
        request.headers.setdefault("User-Agent", useragent)

class CookieMiddleware(RetryMiddleware):

    def process_request(self, request, spider):
        cookies= [
            {
                "_ga": "GA1.2.1314880111.1575270132",
                "Hm_lvt_1c587ad486cdb6b962e94fc2002edf89": "1575270133,1575278608,1575599663,1575604289",
                "juzi_user": "790885",
                "_gid": "GA1.2.275180730.1575450802",
                "Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89": "1575452638",
                "juzi_token": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NzU1OTk4MDAsImV4cCI6MTU3NTYwMzQwMCwibmJmIjoxNTc1NTk5ODAwLCJqdGkiOiJHUHVOWHJQckhJMU1IWDllIiwic3ViIjo3OTA4ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiZldvQVhkIn0.H-PgP7igZ38nEN0jkq0sABdCr86-7DcyNJhbnoCQqng",
                "_gat_gtag_UA_59006131_1": "1",
            },
            # {
            #     "Hm_lvt_1c587ad486cdb6b962e94fc2002edf89":"1575515539",
            #     "_ga":"GA1.2.372845372.1575515539",
            #     "_gid":"GA1.2.1068694372.1575515539",
            #     "juzi_user":"791716",
            #     "juzi_token":"bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NzU1MTU4NzksImV4cCI6MTU3NTUxOTQ3OSwibmJmIjoxNTc1NTE1ODc5LCJqdGkiOiJYd2swWjhRWDVwQkpCdEJ6Iiwic3ViIjo3OTE3MTYsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiblRvTlBaIn0.TapnaNHW_BLc_5aLlRNGS88FRujyjHRP0fxjkA_5V6o",
            #     "Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89": str(int(time.time()/1000))
            # }
        ]
        # request.headers.setdefault("Cookies", cookies)
        currentCookie = random.choice(cookies)
        authorization = currentCookie['juzi_token']
        # request.headers['Cookie'] = currentCookie
        request.cookies = currentCookie
        # request.headers['Authorization'] = authorization
        # request.headers['CURLOPT_FOLLOWLOCATION'] = "true"
        # request.headers['Referer'] = "https://www.itjuzi.com/company"
        # request.headers['Origin'] = "https://www.itjuzi.com"
        request.headers.setdefault("Authorization", authorization)
        request.headers.setdefault("CURLOPT_FOLLOWLOCATION", "true")
        request.headers.setdefault("CURLOPT_FOLLOWLOCATION", "true")
        request.headers.setdefault("Referer", "https://www.itjuzi.com/company")
        request.headers.setdefault("Origin", "https://www.itjuzi.com")

class RandomProxy(object):
    	def process_request(self, request, spider):
		
		# 这是使用了私密代理
		"""
		proxy_url = 'http://%s:%s@%s' % (username, password, proxy)
		request.meta['proxy'] = proxy_url  # 设置代理
		logger.debug("using proxy: {}".format(request.meta['proxy']))
		# 设置代理身份认证
		# Python3 写法
		# auth = "Basic %s" % (base64.b64encode(('%s:%s' % (username, password)).encode('utf-8'))).decode('utf-8')
		# Python2 写法
		auth = "Basic " + base64.b64encode('%s:%s' % (username, password))
		request.headers['Proxy-Authorization'] = auth
		"""

		# 这是使用独享代理
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
