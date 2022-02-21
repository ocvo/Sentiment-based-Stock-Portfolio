import os
import scrapy
import pandas as pd
from selenium import webdriver
import time

class QuotesSpider(scrapy.Spider):
    name = "start"

    def __init__(self):

        self.driver = webdriver.Chrome(r'C:\Users\trans\PycharmProjects\pythonProject\stock_crawl\crawl_button\chromedriver.exe')

    def start_requests(self):

            url = 'https://www.morningstar.com/stocks/xstc/vnm/valuation'
            self.driver.maximize_window()
            driver = self.driver.get(url)
            html = driver.page_source
            print(html)
            # data = self.driver.find_element_by_xpath('//td[@class="mds-data-table__cell__sal mds-data-table__cell--right__sal"]')
            # print(data)









