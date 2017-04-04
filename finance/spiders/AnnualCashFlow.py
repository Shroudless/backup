# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class AnnualCashFlowSpider(scrapy.Spider):
    name = "AnnualCashFlow"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?q=NASDAQ:SKUL&fstype=ii',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("Currency", '//div[@id="casannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TimePeriod", '//div[@id="casannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetIncomeStartingLine",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DepreciationDepreciation",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Amortization", '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DeferredTaxes", '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NonCashItems", '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ChangesInWorkingCapital", '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromOperatingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CapitalExpenditures",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherInvestingCashFlowItemsTotal",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromInvestingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("FinancingCashFlowItems",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalCashDividendsPaid", '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IssuanceRetirementofStockNet",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IssuanceRetitementOfDebtNet",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromFinancingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ForeignExchangeEffects", '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetChangeInCash", '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashInterestPaidSupplemental",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashTaxesPaidSupplemental",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))




        return l.load_item()