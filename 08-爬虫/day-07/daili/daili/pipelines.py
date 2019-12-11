# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis

REDIS_URL = 'redis://root:123456@127.0.0.1:6379'
class DailiPipeline(object):

    def __init__(self):
        reds = redis.Redis.from_url(REDIS_URL, db=1, decode_responses=True)
    def process_item(self, item, spider):
        ip_port = item['ip_port']

        return item
