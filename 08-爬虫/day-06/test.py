title = response.xpath('//div[@class="info"]//a/span[@class="title"][1]/text()')  

info = response.xpath('//div[@class="info"]/div[@class="bd"]/p/text()')

start = response.xpath('//div[@class="info"]//div[@class="star"]/span[@class="rating_num"]/text()')

qute = response.xpath('//div[@class="info"]//p[@class="quote"]/span/text()')
