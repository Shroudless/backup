# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class QuarterlyIncomeStatementSpider(scrapy.Spider):
    name = "QuarterlyIncomeStatement"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?q=NASDAQ:SKUL&fstype=ii',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("Currency", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TimePeriod", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Revenue", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherRevenueTotal", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalRevenue", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CostOfRevenueTotal", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("GrossProfit", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("SellingGeneralAdminExpensesTotal", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ResearchAndDevelopment", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DepreciationAmortization", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("InterestExpenseIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("UnusualExpenseIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherOperatingExpenses", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalOperatingExpenses", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OperatingIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("InterestIncomeExpense", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("GainLossOnSaleOfAssets", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherNet", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IncomeBeforeTax", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IncomeAfterTax", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MinorityInterest", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("EquityInAffiliates", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetIncomeBeforeExtraItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AccountingChange", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DiscontinuedOperations", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ExtraordinaryItem", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("PreferredDividends", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IncomeAvailabletoCommonExclExtraItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IncomeAvailabletoCommonInclExtraItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("BasicWeightedAverageShares", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("BasicEPSExcludingExtraordinaryItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("BasicEPSIncludingExtraordinaryItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DilutionAdjustment", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DilutedWeightedAverageShares", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DilutedEPSExcludingExtraordinaryItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DilutedEPSIncludingExtraordinaryItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DividendsperShareCommonStockPrimaryIssue", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("GrossDividendsCommonStock", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetIncomeAfterStockBasedCompExpense", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("BasicEPSAfterStockBasedCompExpense", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DilutedEPSAfterStockBasedCompExpense", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DepreciationSupplemental", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalSpecialItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NormalizedIncomeBeforeTaxes", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[43]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("EffectOfSpecialItemsOnIncomeTaxes", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[44]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IncomeTaxesExcludingImpactOfSpecialItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[45]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NormalizedIncomeAfterTaxes", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[46]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NormalizedIncomeAvailToCommon", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[47]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("BasicNormalizedEPS", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[48]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DilutedNormalizedEPS", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))




        return l.load_item()