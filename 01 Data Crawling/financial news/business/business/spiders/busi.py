import os
import scrapy
import pandas as pd
import unicodedata

class QuotesSpider(scrapy.Spider):
    name = "busi"
    url = 'https://www.investing.com/news/economic-indicators'

    def start_requests(self):
        # for i in range(1,1881):
            url_get_page = self.url + '/%s' % 2
            yield scrapy.Request(url_get_page, callback=self.parse)


    def parse(self, response):
        print(len(response.xpath('//div[@class="textDiv"]/a/text()')))
        print(len(response.xpath('//span[@class="date"]/text()')))
        for i in response.xpath('//div[@class="textDiv"]/a/text()'):
            print(i.get().strip())








