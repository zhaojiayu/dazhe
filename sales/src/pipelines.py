# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import database


class GetMarketPipeline(object):
    def __init__(self):
        self.db = database.DBOperation()

    def process_item(self, item, spider):
        self.db.insert_data(item)
        return item

    def close_spider(self, spider):
        self.db.dis_conn()
