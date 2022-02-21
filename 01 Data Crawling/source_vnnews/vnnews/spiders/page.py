import os
import scrapy
import pandas as pd
import unicodedata

class QuotesSpider(scrapy.Spider):
    name = "page"
    domain = 'https://vietnamnews.vn'


    def start_requests(self):
        os.chdir(r'C:\Users\Son Tran\PycharmProjects\pythonProject\stock_crawl\vnnews\vnnews\data_header')
        df_info = pd.read_csv('data_header.csv')
        for i in list(df_info['page']):
            url = self.domain + i
            yield scrapy.Request(url, callback=self.parse)



    def parse(self, response):
        data = {"url":[], 'time':[]}
        time = response.xpath('//div[@class="vnnews-time-post"]/span/text()').extract()[0].strip()
        data['time'].append(time)
        url_final = '/'+ response.url.split('/')[3:][0]+'/' +response.url.split('/')[3:][1] +'/'+response.url.split('/')[3:][2]
        data['url'].append(url_final)
        df_save = pd.DataFrame(data)
        os.chdir(r'C:\Users\Son Tran\PycharmProjects\pythonProject\stock_crawl\vnnews\vnnews\data_header')
        df_save.to_csv('time.csv', mode='a',index=False, header=None)
