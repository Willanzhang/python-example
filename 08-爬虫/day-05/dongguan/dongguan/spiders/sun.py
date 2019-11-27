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
        Rule(pagelink, process_links = "deal_links", follow = True),
        Rule(detaillink, follow=False, callback='parse_item'),
    )

    # 有些反爬虫措施会修改link 的地址
    # 需要重新处理每个 response 里提出的链接， Type&page=xx?type 修改为 Type?page=xx&type
    # links 就是 LinkExtractor 提出出来的当前页面链接列表
    def deal_links(self, links):
        for link in links:
            link.url = link.url.replace("?", "&").replace("Type&", "Type?")
        # 返回修改完的links 列表
        return links

    def parse_item(self, response):
        item = DongguanItem()
        # 链接
        item['url'] = response.url
        # 標題
        title = response.xpath('//div[@class="wzy1"]//td/span[@class="niae2_top"]/text()').extract()[0]
        item['title'] = title
        # 編號
        number = response.xpath('//div[@class="wzy1"]//td/span[2]/text()').extract()[0].split(':')[-1]
        item['number'] = number
        # 内容
        content = response.xpath('//div[@class="wzy1"]//tr[1]/td[@class="txt16_3"]/text()').extract()

        if (len(content)) == 0 or (len(content) == 1 and content[0].replace(u'\xa0', u'') == ''):
            content = response.xpath('//div[@class="wzy1"]//tr[1]/td[@class="txt16_3"]/div[@class="contentext"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        
        yield item