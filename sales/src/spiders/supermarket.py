# -*- coding:utf-8 -*-
# __author__ = 'Administrator'
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from src.items import GetMarketInfoItem
import re
import time
import datetime
import src.database
from scrapy.http import FormRequest


class GeturlSpider(BaseSpider):
    name = "market"
    allowed_domains = ["http://www.dazhe5.com"]
    start_urls = ['http://www.dazhe5.com/news/chaoshi/']
    del_obj = src.database.DBOperation()
    del_obj.delete_all()

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        market_item = hxs.select('//*[@id="shangchang"]/li/a/@href').extract()
        for link in market_item:
            yield Request(link, callback=self.parse_item, dont_filter=True)
       #link = 'http://www.dazhe5.com/news/chaoshi/watsons/'
       # yield Request(link, callback=self.parse_item, dont_filter=True)

#    自定义函数，用来处理新链接的request后获得的response
#    用于与Parse方法一起实现递归爬虫
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print today
        item = GetMarketInfoItem()
        market_names = hxs.select('//*[@class="note_1"]/a/text()').extract()
        market_titles = hxs.select('//*[@class="box1"]/a/text()').extract()
        market_times = hxs.select('//*[@class="box2"]/text()').extract()
        market_end_times = hxs.select('//*[@class="middle_box_times"]/input/@value').extract()
        market_urls = hxs.select('//*[@class="box1"]/a/@href').extract()
       # print (today < market_end_times[2])
        for i in range(len(market_times)):
            if today < market_end_times[i]:
                print 'Is on sale'
                item['market_name'] = market_names[i]
                item['market_title'] = market_titles[i]
                item['market_time'] = market_times[i]
                item['market_url'] = market_urls[i]
                yield item
            else:
                print 'Is not on sale'


