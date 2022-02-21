import os
import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "gua"

    def start_requests(self):
        # for i in range(1,5000):
        # url = 'https://www.theguardian.com/us-news/us-politics?page=1'
        months = ['aug', 'jul','jun','may','apr','mar','feb','jan','dec','nov','oct','sep']
        for year in range(2015,2022):
            for month in months:
                for date in range(1,32):
                    if len(str(date)) ==1:
                        date = '0'+ str(date)
                    else:
                        date
                    url = 'https://www.theguardian.com/australia-news/australian-politics/%s/%s/%s/all' % (year, month,date)

                    yield scrapy.Request(url, callback=self.parse, meta = {
                  'dont_redirect': True,
                  'handle_httpstatus_list': [302]})

    def parse(self, response):
        if response.status == 200:
            time_spi = response.url.split('/')[-4:]
            time = time_spi[0] + ' ' + time_spi[1] + ' ' + time_spi[2]
            data = {"title": [], "time": []}
            if len (response.xpath(r'//div[@class="fc-item__container"]/a/text()')) >0:
                for title in response.xpath(r'//div[@class="fc-item__container"]/a/text()'):
                    data['title'].append(title.extract().strip())
                    data['time'].append(time)
            os.chdir(r'C:\Users\Son Tran\PycharmProjects\pythonProject\stock_crawl\guard\gua\gua\data_au')
            pd.DataFrame(data).to_csv('%s.csv'% time_spi[0].strip(),index=False, header=None,mode='a')










