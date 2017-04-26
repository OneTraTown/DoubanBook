# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class DoubanItem(Item):
    book_name = Field()
    book_author = Field()
    book_publish = Field()
    book_publish_date = Field()
    book_price = Field()
    book_star = Field()
    book_rating = Field()
