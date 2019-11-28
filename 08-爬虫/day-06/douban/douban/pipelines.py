# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
# from scrapy.conf import settings
from scrapy.utils.project import get_project_settings

# 27017
# 查看当前数据库
# db

# 查看所有数据库
# show dbs

# 连接到xxx数据库

# 查看当前数据库下所有的表
# show collections

# 查看yyy表里的数据
# db.yyy.find

# 删除当前数据库
# db.dropDatabase()

# 创建集合
# db.createCollection('food')

# 删除集合
# db.food.drop()

class DoubanPipeline(object):
    def __init__(self):
        host = get_project_settings().get("MONGODB_HOST")
        port = get_project_settings().get("MONGODB_PORT")
        dbname = get_project_settings().get("MONGODB_DBNAME")
        sheetname = get_project_settings().get("MONGODB_SHEETNAME")

        # 创建MONGODB的数据库连接
        client = pymongo.MongoClient(host = host, port = port)

        # 指定数据库
        mydb = client[dbname]
        
        # 厨房数据的数据库表名
        self.mysheet = mydb[sheetname]


    def process_item(self, item, spider):
        data = dict(item)
        self.mysheet.insert(data)

        return item
