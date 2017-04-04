# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class QuarterlyBalanceSheetSpider(scrapy.Spider):
    name = "QuarterlyBalanceSheet"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?q=NASDAQ:SKUL&fstype=ii',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("Currency", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TimePeriod", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashAndEquivalents", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ShortTermInvestments", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashAndShortTermInvestments", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AccountsReceivableTradeNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ReceivablesOther", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalReceivablesNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalInventory", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("PrepaidExpenses", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherCurrentAssetsTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalCurrentAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("PropertyPlantEquipmentTotalGross", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AccumulatedDepreciationTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("GoodwillNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IntangiblesNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("LongTermInvestments", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherLongTermAssetsTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AccountsPayable", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AccruedExpenses", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NotesPayableShortTermDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CurrentPortofLTDebtCapitalLeases", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherCurrentliabilitiesTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalCurrentLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("LongTermDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CapitalLeaseObligations", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalLongTermDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DeferredIncomeTax", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MinorityInterest", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherLiabilitiesTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("RedeemablePreferredStockTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("PreferredStockNonRedeemableNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CommonStockTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AdditionalPaidInCapital", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("RetainedEarningsAccumulatedDeficit", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TreasuryStockCommon", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherEquityTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalEquity", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalLiabilitiesShareholdersEquity", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("SharesOutsCommonStockPrimaryIssue", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalCommonSharesOutstanding", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))




        return l.load_item()