# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

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
#         # print '----------------------------------------------------------------------' + '\n' + '---------------------------------------------------'
#         return item

class ImagesPipeline(ImagesPipeline):
    # 获取setting 文件里的设置变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imageLink"]
        yield scrapy.Request(image_url)
    
    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]
        print image_path

        if len(image_path) > 0:
            os.rename(self.IMAGES_STORE + '/' + image_path[0], self.IMAGES_STORE + '/' + item['nickname'] + '.jpg')
            item['imagePath'] = self.IMAGES_STORE + '/' + item['nickname']

        return item
