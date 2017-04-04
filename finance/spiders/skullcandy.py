# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class SkullcandySpider(scrapy.Spider):
    name = "skullcandy"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?cid=6826782',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("CompanyName", '//*[@id="companyheader"]/div[1]/h3/text()', MapCompose(unicode.strip, unicode.title))#needs return value to output
        l.add_xpath("StockExchangeAndCode", '//*[@id="companyheader"]/div[1]/text()[1]',  MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Currency", '//*[@id="ref_6826782_elt"]/div/div/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("StockPrice", '//*[@id="ref_6826782_l"]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MarketCap", '//*[@id="market-data-div"]/div[2]/div[1]/table[1]/tr[5]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("PE", '//*[@id="market-data-div"]/div[2]/div[1]/table[1]/tr[6]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("EPS", '//*[@id="market-data-div"]/div[2]/div[1]/table[2]/tr[2]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Shares", '//*[@id="market-data-div"]/div[2]/div[1]/table[2]/tr[3]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("InstOwn", '//*[@id="market-data-div"]/div[2]/div[1]/table[2]/tr[5]/td[2]/text()', MapCompose(unicode.strip, unicode.title))


        return l.load_item()



