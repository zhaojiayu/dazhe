# -*- coding:utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class GetMarketInfoItem(Item):
    # define the fields for your item here like:
    market_name = Field()
    market_title = Field()
    market_time = Field()
    market_url = Field()
    pass
