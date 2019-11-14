#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import json
from lxml import etree
import requests
import re

url = "http://www.lovehhy.net/Joke/Detail/QSBK/"
headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request = urllib2.Request(url, headers = headers)

html = urllib2.urlopen(request).read()
# 响应返回的是字符串，解析为HTML DOM模式 text = etree.HTML(html)

# text = etree.HTML(html.decode('utf-8', 'replace'))
# text = etree.HTML(html.decode("utf8","ignore"))
# 处理那乱码必须这么做！！！！
text = etree.HTML(html.decode('gbk', 'ignore').encode('utf-8'))
# text = etree.HTML(html)

# 返回所有段子的结点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
# node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

arr = []

# title 列表
node_list = text.xpath('//div[@class="cat_llb"]/h3[@class="red"]/a')

# 描述 列表
desc_list = text.xpath('//div[@class="cat_llb"]/text()')

# 文章内容列表
content_list = text.xpath('//div[contains(@id, "endtext")]')
for index in range(len(node_list)):
	title = node_list[index].text
	# content = content_list[index].text
	# 使用xpath(‘string(.)’)这种方式获取所有文本 
	content = content_list[index].xpath('string(.)')
	desc = desc_list[index]
	items = {
		"title": title,
		"content": content.lstrip(),
		"desc": desc,
		"time": desc.split(u"　　")[0],
		"click_num": re.compile("\d").search(desc.split(u"　　")[1]).group(0)
	}
	arr.insert(0,items)
	# print re.compile("\d").search(desc.split(u"　　")[1]).group(0)
  
with open("qiushi.json", "w") as f:
	f.write(json.dumps(arr, ensure_ascii = False).encode("utf-8") + "\n")


# items ={}
# for node in node_list:
#     # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
#     username = node.xpath('./div/a/@title')[0]
#     # 图片连接
#     image = node.xpath('.//div[@class="thumb"]//@src')#[0]
#     # 取出标签下的内容,段子内容
#     content = node.xpath('.//div[@class="content"]/span')[0].text
#     # 取出标签里包含的内容，点赞
#     zan = node.xpath('.//i')[0].text
#     # 评论
#     comments = node.xpath('.//i')[1].text

#     items = {
#         "username" : username,
#         "image" : image,
#         "content" : content,
#         "zan" : zan,
#         "comments" : comments
#     }

#     with open("qiushi.json", "a") as f:
#         f.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")



