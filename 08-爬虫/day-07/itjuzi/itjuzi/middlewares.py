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
# from .utils import fetch_one_proxy

from settings import USER_AGENTS
from settings import PROXIES

# https://www.kuaidaili.com/pricing/#dps
# 非开放代理且未添加白名单，需用户名密码认证
# username = "willian_zhangb"
# password = "v17ezvhl"
# proxy = fetch_one_proxy() # 获取一个代理

# THRESHOLD = 3  # 换ip阈值
# fail_time = 0  # 此ip异常次数
logger = logging.getLogger(__name__)

# 随机的User-Agent
class RandomUserAgent(object):

    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        #print useragent
        request.headers.setdefault("User-Agent", useragent)

class CookieMiddleware(object):

    def process_request(self, request, spider):
        cookies={
            "_ga": "GA1.2.1314880111.1575270132",
            "Hm_lvt_1c587ad486cdb6b962e94fc2002edf89": "1575270133,1575278608",
            "juzi_user": "790885",
            "_gid": "GA1.2.275180730.1575450802",
            "Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89": "1575452638",
            "juzi_token": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1NzU0NTI3MzAsImV4cCI6MTU3NTQ1NjMzMCwibmJmIjoxNTc1NDUyNzMwLCJqdGkiOiIwOEliZm9wUENlTld6MXBRIiwic3ViIjo3OTA4ODUsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiaXB3WlY1In0.aj9YlADIUAxRrESLHu42lT-KbiWY6-BZii7KiRn6-Xk",
            "_gat_gtag_UA_59006131_1": "1",
            "Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89": str(int(time.time()/1000))
        }
        # request.headers.setdefault("Cookies", cookies)
        request.cookies = cookies
