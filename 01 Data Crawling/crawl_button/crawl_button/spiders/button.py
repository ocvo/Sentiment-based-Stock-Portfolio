import os
import scrapy
import pandas as pd
from selenium import webdriver
import time
class QuotesSpider(scrapy.Spider):
    name = "button"


    def __init__(self):

        self.driver = webdriver.Chrome(r'C:\Users\trans\PycharmProjects\pythonProject\stock_crawl\crawl_button\chromedriver.exe')

    def start_requests(self):
        df = pd.read_excel(r'C:\Users\trans\PycharmProjects\pythonProject\stock_crawl\web-scraping-investing\list_au_final.xlsx')
        os.chdir(r'C:\Users\trans\Downloads')
        files = os.listdir()
        files = [x.split('.')[0] for x in files ]
        print(len(list(df['Symbol'])))
        for i in list(df['Symbol']):
            if i.strip() not in files:
                url = 'https://finance.yahoo.com/quote/%s/history?period1=1104537600&period2=1629158400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true' % (i.strip() + '.AX')
                self.driver.get(url)
                while True:
                    try:
                        download = self.driver.find_element_by_xpath('//span[text()="Download"]')
                        time.sleep(1)
                        download.click()
                        time.sleep(1)
                        break
                        # get the data and write it to scrapy items
                    except:
                        break

    # def parse(self, response):









