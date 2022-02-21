import os
import scrapy
import pandas as pd
import unicodedata

class QuotesSpider(scrapy.Spider):
    name = "news"



    def start_requests(self):
        for i in range(1,2148):
        # for i in range(64, 65):

            url = 'https://vietnamnews.vn/politics-laws?p=%s' % i

            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        try:
            sub = []
            title = []
            for i in response.xpath('//span[@class="vnnews-tt-list-news"]/text()'):
                title.append(unicodedata.normalize('NFC',i.extract().strip().replace('\n',' ')))
                # title.append(i.extract().strip())
            title = title[1:]
            for i in response.xpath('//div[@class="vnnews-sapo-list-news"]/text()'):
                if len(i.extract().strip()) > 0:
                    sub.append(i.extract().strip())

            for i in response.xpath('//div[@class="vnnews-sapo-list-news"]/p/text()'):
                text = unicodedata.normalize('NFC',i.extract().strip().replace('\n',' '))
                sub.append(text)


            link_href = []
            for i in response.xpath('//li/a/@href'):
                if '/politics-laws/' in i.extract():
                    link_href.append(i.extract())
            index = len(title)
            link_href = link_href[:index]
            # print('para ' + str(len(sub)))
            # print('title ' + str(len(title)))
            # print('link_href ' + str(len(link_href)))
            if (len(sub) != len(title)) and (len(sub) != len(link_href)):
                test = [len(sub), len(title), len(link_href)]
                plus = max(test) - len(sub)

                for i in range(0,plus):
                    sub.append('')

            data ={'title':title,
                   'para': sub,
                   'link_href':link_href}


            os.chdir(r'C:\Users\Son Tran\PycharmProjects\pythonProject\stock_crawl\vnnews\vnnews\data_header')
            df = pd.DataFrame(data)
            df.to_csv('data_header.csv', index=False, mode='a', header=None)
        except:
            error = {'url':[response.url], 'check':['1'] }
            pd.DataFrame(error).to_csv('data_error.csv',index=False, mode='a', header=None)
