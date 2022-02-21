import os
import scrapy
import pandas as pd
import unicodedata

class QuotesSpider(scrapy.Spider):
    name = "stock"
    url = 'https://www.investing.com'

    symbol = 'MMM'
    handle_httpstatus_all = True
    break_point = False

    def start_requests(self):
        os.chdir(r'C:\Users\Son Tran\PycharmProjects\pythonProject\stock_crawl\invest\invest\spiders')
        df = pd.read_csv('../../../web-scraping-investing/list_500.csv')

        # url_get = 'https://www.investing.com/equities/3m-co-news/1'
        #
        for i in ['/equities/becton-dickinsn','/equities/wellpoint-inc']:
        # i= '/equities/abbvie-inc'
            url_get = self.url + i + '-news'

            for count_page in range(1,1000000):
                url_get_page = url_get + '/%s' % count_page
                if self.break_point:
                    self.break_point = False
                    break
            # url_get_page = 'https://www.investing.com/equities/abbvie-inc-news/11'
                yield scrapy.Request(url_get_page, callback=self.parse, meta = {
                  'dont_redirect': True,
                  'handle_httpstatus_list': [302]})


    def parse(self, response):
        if response.status == 302:
            self.break_point = True
        else:

            # for i in response.xpath('//article/div/p'):
            #     print(i.get())
            data_final = {"title": [],
                          "time": [],
                          "para": [],
                          "link_stock_id":[]
                          }

            path_link = '/' +  response.url.split('/')[-3:][0] + '/' + response.url.split('/')[-3:][1][:-5]

            title_name = response.xpath('//div[@class="mediumTitle1"]/article/div/a/text()')

            title_name = [name for name in title_name if len(name.get()) > 4]

            for title in title_name:
                data_final['title'].append(title.get())
                data_final['link_stock_id'].append(path_link)
            count = 0
            for i in range(0,len(title_name)):
                count += 1
                time = response.xpath('//span[@class="date"]/text()')[i]
                data_final['time'].append(time.get().split('-')[1].strip())
                if i == (len(title_name) -1):break
            for para in response.xpath('//article/div/p'):
                # data_final['para'].append(unicodedata.normalize('NFC',para.extract().strip().replace('\n',' ')))
                data_final['para'].append(para.get().strip())
            # if len(str(len(data_final['time']))) == len(str(len(data_final['para']))) == len(str(len(data_final['time']))) == len(str(len(data_final['title']))):
            os.chdir(r'C:\Users\Son Tran\PycharmProjects\pythonProject\stock_crawl\invest\invest\data')

            pd.DataFrame(data_final).to_csv('data_1.csv', index=False, encoding='utf-8', mode='a',
                                            header=False)
            # else:
            #     print("time" + '   ' + str(len(data_final['time'])))
            #     print("para" + '   ' + str(len(data_final['para'])))
            #     print("title" + '   ' + str(len(data_final['title'])))








