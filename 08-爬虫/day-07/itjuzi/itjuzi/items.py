# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # 公司名称
    name = scrapy.Field()
    # 省
    prov = scrapy.Field()
    # 市
    city = scrapy.Field()
    # 注册公司名称
    registerName = scrapy.Field()
    # 描述
    des = scrapy.Field()
    # 口号
    slogan = scrapy.Field()
    # 爬虫名字
    spiderName = scrapy.Field()
    # 爬取时间
    crawlTime = scrapy.Field()
    # pass
