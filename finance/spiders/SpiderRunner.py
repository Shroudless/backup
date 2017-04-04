import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class DailyFinancialDataSpider(scrapy.Spider):
    name = "DailyFinancialData"
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


class QuarterlyKeyRatiosSpider(scrapy.Spider):
    name = "QuaterlyKeyRatios"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?cid=6826782',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("CompanyName", '//*[@id="companyheader"]/div[1]/h3/text()', MapCompose(unicode.strip, unicode.title))  # needs return value to output
        l.add_xpath("StockExchangeAndCode", '//*[@id="companyheader"]/div[1]/text()[1]', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetProfitMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[1]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OperatingMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[2]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("EBITDMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[3]/td[2]', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ReturnOnAssets", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[4]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ReturnOnEquity", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[5]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Employees", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[5]/td[2]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[2]', MapCompose(unicode.strip, unicode.title))



        return l.load_item()



class QuarterlyIncomeStatementSpider(scrapy.Spider):
    name = "QuarterlyCashFlow"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?q=NASDAQ:SKUL&fstype=ii',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("Currency", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TimePeriod", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetIncomeStartingLine", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DepreciationDepreciation", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Amortization", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DeferredTaxes", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NonCashItems", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ChangesInWorkingCapital", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromOperatingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CapitalExpenditures", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherInvestingCashFlowItemsTotal", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromInvestingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("FinancingCashFlowItems", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalCashDividendsPaid", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IssuanceRetirementofStockNet", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IssuanceRetitementOfDebtNet", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromFinancingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ForeignExchangeEffects", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetChangeInCash", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashInterestPaidSupplemental", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashTaxesPaidSupplemental", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))




        return l.load_item()


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



class QuarterlyCashFlowSpider(scrapy.Spider):
    name = "QuarterlyCashFlow"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.google.com/finance?q=NASDAQ:SKUL&fstype=ii',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("Currency", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TimePeriod", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetIncomeStartingLine", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DepreciationDepreciation", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Amortization", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("DeferredTaxes", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NonCashItems", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ChangesInWorkingCapital", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromOperatingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CapitalExpenditures", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("OtherInvestingCashFlowItemsTotal", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromInvestingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("FinancingCashFlowItems", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("TotalCashDividendsPaid", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IssuanceRetirementofStockNet", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("IssuanceRetitementOfDebtNet", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashFromFinancingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("ForeignExchangeEffects", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("NetChangeInCash", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashInterestPaidSupplemental", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("CashTaxesPaidSupplemental", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))




        return l.load_item()







configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(DailyFinancialDataSpider)
    yield runner.crawl(QuarterlyKeyRatiosSpider)
    yield runner.crawl(QuarterlyIncomeStatementSpider)
    yield runner.crawl(QuarterlyBalanceSheetSpider)
    yield runner.crawl(QuarterlyCashFlowSpider)
    reactor.stop()

crawl()
reactor.run()