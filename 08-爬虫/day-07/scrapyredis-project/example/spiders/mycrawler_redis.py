#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mycrawler_redis.py
@Time    :   2019/11/29 16:29:05
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    # 启动所有端爬虫的指令 下面格式是参考格式，建议采用这种格式
    redis_key = 'mycrawler:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
