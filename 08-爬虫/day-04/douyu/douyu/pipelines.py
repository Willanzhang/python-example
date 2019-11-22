#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pipelines.py
@Time    :   2019/11/22 15:41:14
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 导入包 可以直接使用我们设置的settings
from scrapy.utils.project import get_project_settings

# 可以在 python/site/scrapy/pipelines 找 处理图片的方法   就是同级的 images.py 文件
from scrapy.pipelines.images import ImagesPipeline

import os
import scrapy
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

# class DouyuPipeline(object):
#     def process_item(self, item, spider):
#         return item

class ImagesPipeline(ImagesPipeline):
    # 获取setting 文件里的设置变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imageLink"]
        yield scrapy.Request(image_url)
    
    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]
        os.rename(self.IMAGES_STORE + '/' + image_path[0], \
            self.IMAGES_STORE + '/' + item['nickname'] + '.jpg')
        item['imagePath'] = self.IMAGES_STORE + '/' + item['nickname']

        return item