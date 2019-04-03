# -*- coding: utf-8 -*-
import scrapy
from newsCrawler.items import NewscrawlerItem
from bs4 import BeautifulSoup


class DnSpider(scrapy.Spider):
    name = 'dn'
    allowed_domains = ['dn.se']
    start_urls = ['https://www.dn.se']

    def parse(self, response):
        for item in self.scrape(response):
            yield item

    def scrape(self, response):
        for news in response.xpath('//a[starts-with(@class,"news-list")]'):
            item = NewscrawlerItem()
            item['link'] = news.re_first(r'href="(.*?)"')
            item['date'] = news.xpath('./time[@datetime]')\
                .re_first(r'\d{4}-\d{2}-\d{2}\w\d{2}:\d{2}:\d{2}')
            item['header'] = news.xpath('./h2/text()').get()
            if item['header'] is not None:
                item['header'] = item['header'].strip()
            item['link'] = response.urljoin(item['link'])
            request = scrapy.Request(item['link'], self.parse_message)
            request.meta['item'] = item
            yield request

    def parse_message(self, response):
        item = response.meta['item']
        item['message'] = response.\
            xpath('//div[contains(@class,"article__body")]').get()
        soup = BeautifulSoup(item['message'], 'html.parser')
        item['message'] = soup.get_text()
        yield item
