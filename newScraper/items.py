# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrawlerItem(scrapy.Item):
    link = scrapy.Field()
    date = scrapy.Field()
    header = scrapy.Field()
    message = scrapy.Field()

class SwedbankItem(scrapy.Item):
    link = scrapy.Field()
    date = scrapy.Field()
    header = scrapy.Field()
    message = scrapy.Field()
