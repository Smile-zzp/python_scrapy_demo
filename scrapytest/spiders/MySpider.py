import scrapy
import re
from scrapytest.items import Item

class MySpider(scrapy.Spider):
    name = "MySpider"
    start_urls = ["http://www.imooc.com/course/list"]
    def parse(self, response):
        item = Item()
        html = response.text
        cont = re.findall(r'data-original="(.*?)"', html)
        for i in range(len(cont)):
            # scrapy.Request发请求时，必须要完整的URL信息,所以补齐 http:
            item['img_url'] = 'http:'+cont[i]
            yield item
