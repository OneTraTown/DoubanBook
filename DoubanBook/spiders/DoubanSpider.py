# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
from  scrapy.http import Request
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from douban.items import DoubanItem

class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = [
    'https://www.douban.com/tag/%E6%82%AC%E7%96%91/book?start=0'
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'start=\d{1,3}$')),
        callback='parse_item',follow = True),
    )


    def parse_item(self, response):
        items = []
        book_list = response.css('div.mod.book-list dl')
        for book in book_list:
            item = DoubanItem()
            try:
                item['book_name'] = book.xpath('dd/a/text()').extract()[0]
                temp = book.xpath('dd/div[1]/text()').extract()[0].strip().split('/')
                item['book_price'] = temp.pop()
                item['book_publish_date'] = temp.pop()
                item['book_publish'] = temp.pop()
                item['book_author'] = '/'.join(temp)
                item['book_star'] = book.xpath('//*[@id="content"]/div/div[1]/div[1]/dl[5]/dd/div[2]/span[1]/@class').extract()[0]
                item['book_rating'] = book.xpath('//*[@id="content"]/div/div[1]/div[1]/dl[5]/dd/div[2]/span[2]/text()').extract()
            except:
                pass
            items.append(item)
        return items
