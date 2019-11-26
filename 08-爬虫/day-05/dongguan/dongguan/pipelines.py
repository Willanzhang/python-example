# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import time
import json
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

class DongguanPipeline(object):
    # __init__是可选的
    def __init__(self):
        self.filename = open( str(time.strftime("%Y-%m-%d")) + "-tencent.json", "wa")

    # 只有此方法是必须写的 处理 item 数据
    def process_item(self, item, spider):
        # spider 是爬虫的名字
        jsontext = json.dumps(dict(item), ensure_ascii= False) + "\n"
        self.filename.write(jsontext)
        return item
    
    # close_spider 是可选的， 结束时调用
    def close_spider(self, spider):
        self.filename.close()