# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TencentSpider.items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    # https://careers.tencent.com/search.html?index=4
    # url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1574306491995&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageSize=10&language=zh-cn&area=cn&pageIndex="
    start_urls = ["https://careers.tencent.com/search.html?index=0"]

    # response 里连接的提取规则， 返回的是符合匹配规则的链接的匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))
    newlink = LinkExtractor(allow=("position.php\?"))
    rules = (
        # 获取列表里的链接， 一次发送请求， 并且继续跟进，调用指定的回调函数
        Rule(pagelink, callback="parse_item", follow=True),
        # Rule(newlink, callback='parse_item', follow=True),
    )

    # starts_url = [
    #     "https://careers.tencent.com/search.html?index=0"
    # ]

    # 第一次執行实际是会会执行这个回调， 但是针对link 是不能以这函数作为回调的
    def parse(self, response):
        print '----------------------------------'
        print response.text
        pass

    # 正則沒匹配上的話 一次都不會執行這個，
    def parse_item(self, response):
        print '----------------------------------'
        print response.text()
        item = TencentItem()
        even_list = response.xpath("//a[@class='recruit-list-link']")
        for each in even_list:
            # 职位名称
            postionName = each.xpath("./div[@class='recruit-title']/text()").extract()[0]
            #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
            #item['name'] = response.xpath('//div[@id="name"]').get()
            #item['description'] = response.xpath('//div[@id="description"]').get()
            yield item
