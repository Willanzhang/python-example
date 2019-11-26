# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']

    start_urls = ["http://wz.sun0769.com/index.php/question/questionType?type=4&page=0"]

    pagelink = LinkExtractor(allow=r"type=4&page=\d+")
    detaillink = LinkExtractor(allow=r"/html/question/\d+/\d+.shtml")

    rules = (
        Rule(pagelink, follow=True),
        Rule(detaillink, follow=False, callback='parse_item'),
    )


    def parse_item(self, response):
        item = DongguanItem()
        # 链接
        item['url'] = response.url
        # 標題
        item['title']  = response.xpath('//div[@class="wzy1"]//td/span[@class="niae2_top"]/text()').extract()[0]
        # 編號
        item['number'] = response.xpath('//div[@class="wzy1"]//td/span[2]/text()').extract()[0]
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]//tr[1]/td[@class="txt16_3"]/text()').extract()[0]
        print '------------------'
        print item
        yield item