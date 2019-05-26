# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class ScrapytestPipeline(object):
    def __init__(self):#创建并打开文件 data.json
        self.file = open('data.json','w',encoding='utf-8')
    def process_item(self, item, spider):#对数据进行操作
        #读取item的数据，ensure_ascii = False （防止写入的是ASCII字符码）
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        #写入文件
        self.file.write(line)
        return item
    # def open_spider(self,spider):
    #     pass
    # def close_spider(self,spider):
    #     pass






















