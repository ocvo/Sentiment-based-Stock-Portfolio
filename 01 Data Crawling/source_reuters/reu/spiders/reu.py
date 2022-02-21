import os
import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "reu"



    def start_requests(self):
        for i in range(1,3300):
            url = 'https://www.reuters.com/news/archive/politicsNews?view=page&page=%s&pageSize=10' %i

            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        if response.status == 200:
            data ={"title":[], "para":[],"time":[]}
            for title in response.xpath('//h3[@class="story-title"]/text()'):
                data['title'].append(title.extract().strip())

            for para in response.xpath('//div[@class="story-content"]/p/text()'):
                data['para'].append(para.extract().strip())

            for time in response.xpath('//span[@class="timestamp"]/text()'):
                data['time'].append(time.extract().strip())

            df = pd.DataFrame(data)
            os.chdir(r'C:\Users\Son Tran\PycharmProjects\pythonProject\stock_crawl\reu\reu\data')
            df.to_csv('data_usa.csv', index=False, header=None, mode='a')







