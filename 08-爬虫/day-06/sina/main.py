#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/11/29 10:48:17
@Author  :   William 
@Version :   1.0
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib

from scrapy import cmdline
cmdline.execute('scrapy crawl sinaSpider'.split())