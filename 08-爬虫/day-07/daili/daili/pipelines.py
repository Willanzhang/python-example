# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import time

REDIS_URL = 'redis://root:123456@47.106.156.14:6379'
class DailiPipeline(object):

    def __init__(self):
        reds = redis.Redis.from_url(REDIS_URL, db=0, decode_responses=True)
        print '=============================================='
        print '=============================================='
        print '=============================================='
        print '=============================================='
        print '=============================================='

    def process_item(self, item, spider):
        ip_port = item['ip_port']
        reds.set('ip' + time.time(), ip_port)
        print "************************************************"
        print "************************************************"
        print "************************************************"
        print "************************************************"
        print "************************************************"
        return item
