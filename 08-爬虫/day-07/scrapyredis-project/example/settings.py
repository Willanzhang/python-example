#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2019/11/29 16:17:34
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib

# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'

# 使用 scrapy-redis的去重类  不使用 scrapy 默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了 scrapy-redis 里的调度器组件  不使用 scrapy 默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停 redis 请求记录不丢失
SCHEDULER_PERSIST = True

# 默认的 scraoy-redis 请求（按优先级顺序）队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列形式的规则 先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈形式  请求先进后厨
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# scrapy_redis.pipelines.RedisPipeline 支持将数据存储到 Redis数据库里， 必须启动
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

REDIS_HOST = "192.168.50.66"
REDIS_PORT = 6379
# LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1
