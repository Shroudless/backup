# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class RatiosSpider(scrapy.Spider):
    name = "ratios"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?cid=6826782',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("CompanyName", '//*[@id="companyheader"]/div[1]/h3/text()', MapCompose(unicode.strip, unicode.title))  # needs return value to output
        l.add_xpath("StockExchangeAndCode", '//*[@id="companyheader"]/div[1]/text()[1]', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetProfitMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[1]/td[3]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OperatingMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[2]/td[3]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("EBITDMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[3]/td[3]', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ReturnOnAssets", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[4]/td[3]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ReturnOnEquity", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[5]/td[3]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Employees", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[5]/td[3]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[3]', MapCompose(unicode.strip, unicode.title))



        return l.load_item()
