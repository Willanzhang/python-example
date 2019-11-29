#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   myspider_redis.py
@Time    :   2019/11/29 16:28:35
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib

from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'

    # 指定爬取域范围 和下面可二选一
    # allowed_domains = ["dmoz.org"]

    def __init__(self, *args, **kwargs):
        # 动态获取 域的范围  避免爬取超出当前域
        # Dynamically define the allowed domains list.
        print '**************************'

        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        print '--------------------------------'
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
