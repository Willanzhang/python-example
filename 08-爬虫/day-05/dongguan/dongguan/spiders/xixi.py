# -*- coding: utf-8 -*-
import scrapy
from dongguan.items import DongguanItem

# 这里是直接使用 spider 类
class XixiSpider(scrapy.Spider):
    name = 'xixi'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]



    def parse(self, response):
        # 每一页里的所有帖子的链接集合
        links = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        # 迭代取出集合里的链接
        for link in links:
            # 提取列表里每个帖子的链接，发送请求放到请求队列里,并调用self.parse_item来处理
            yield scrapy.Request(link, callback = self.parse_item)

        # 页面终止条件成立前，会一直自增offset的值，并发送新的页面请求，调用parse方法处理
        if self.offset <= 71160:
            self.offset += 30
            # 发送请求放到请求队列里，调用self.parse处理response
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)

    # 处理每个帖子的response内容
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
        
        # 交给管道
        yield item