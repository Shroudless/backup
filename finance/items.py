# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FinanceItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CompanyName = Field()
    StockExchangeAndCode = Field()
    Currency = Field()
    StockPrice = Field()
    MarketCap = Field()
    PE = Field()
    EPS = Field()
    Shares = Field()
    InstOwn = Field()
    Date = Field()
    NetProfitMargin = Field()
    OperatingMargin = Field()
    EBITDMargin = Field()
    ReturnOnAssets = Field()
    ReturnOnEquity = Field()
    Employees = Field()
    CDPScore = Field()
    TimePeriod = Field()
    Revenue = Field()
    OtherRevenueTotal = Field()
    TotalRevenue = Field()
    CostOfRevenueTotal = Field()
    GrossProfit = Field()
    SellingGeneralAdminExpensesTotal = Field()
    ResearchAndDevelopment = Field()
    DepreciationAmortization = Field()
    InterestExpenseIncome = Field()
    UnusualExpenseIncome = Field()
    OtherOperatingExpenses = Field()
    TotalOperatingExpenses = Field()
    OperatingIncome = Field()
    InterestIncomeExpense = Field()
    GainLossOnSaleOfAssets = Field()
    OtherNet = Field()
    IncomeBeforeTax = Field()
    IncomeAfterTax = Field()
    MinorityInterest = Field()
    EquityInAffiliates = Field()
    NetIncomeBeforeExtraItems = Field()
    AccountingChange = Field()
    DiscontinuedOperations = Field()
    ExtraordinaryItem = Field()
    NetIncome = Field()
    PreferredDividends = Field()
    IncomeAvailabletoCommonExclExtraItems = Field()
    IncomeAvailabletoCommonInclExtraItems = Field()
    BasicWeightedAverageShares = Field()
    BasicEPSExcludingExtraordinaryItems = Field()
    BasicEPSIncludingExtraordinaryItems = Field()
    DilutionAdjustment = Field()
    DilutedWeightedAverageShares = Field()
    DilutedEPSExcludingExtraordinaryItems = Field()
    DilutedEPSIncludingExtraordinaryItems = Field()
    DividendsperShareCommonStockPrimaryIssue = Field()
    GrossDividendsCommonStock = Field()
    NetIncomeAfterStockBasedCompExpense = Field()
    BasicEPSAfterStockBasedCompExpense = Field()
    DilutedEPSAfterStockBasedCompExpense = Field()
    DepreciationSupplemental = Field()
    TotalSpecialItems = Field()
    NormalizedIncomeBeforeTaxes = Field()
    EffectOfSpecialItemsOnIncomeTaxes = Field()
    IncomeTaxesExcludingImpactOfSpecialItems = Field()
    NormalizedIncomeAfterTaxes = Field()
    NormalizedIncomeAvailToCommon = Field()
    BasicNormalizedEPS = Field()
    DilutedNormalizedEPS = Field()
    CashAndEquivalents = Field()
    ShortTermInvestments = Field()
    CashAndShortTermInvestments = Field()
    AccountsReceivableTradeNet = Field()
    ReceivablesOther = Field()
    TotalReceivablesNet = Field()
    TotalInventory = Field()
    PrepaidExpenses = Field()
    OtherCurrentAssetsTotal = Field()
    TotalCurrentAssets = Field()
    PropertyPlantEquipmentTotalGross = Field()
    AccumulatedDepreciationTotal = Field()
    GoodwillNet = Field()
    IntangiblesNet = Field()
    LongTermInvestments = Field()
    OtherLongTermAssetsTotal = Field()
    TotalAssets = Field()
    AccountsPayable = Field()
    AccruedExpenses = Field()
    NotesPayableShortTermDebt = Field()
    CurrentPortofLTDebtCapitalLeases = Field()
    OtherCurrentliabilitiesTotal = Field()
    TotalCurrentLiabilities = Field()
    LongTermDebt = Field()
    CapitalLeaseObligations = Field()
    TotalLongTermDebt = Field()
    TotalDebt = Field()
    DeferredIncomeTax = Field()
    #MinorityInterest = Field() #already done above for income statement
    OtherLiabilitiesTotal = Field()
    TotalLiabilities = Field()
    RedeemablePreferredStockTotal = Field()
    PreferredStockNonRedeemableNet = Field()
    CommonStockTotal = Field()
    AdditionalPaidInCapital = Field()
    RetainedEarningsAccumulatedDeficit = Field()
    TreasuryStockCommon = Field()
    OtherEquityTotal = Field()
    TotalEquity = Field()
    TotalLiabilitiesShareholdersEquity = Field()
    SharesOutsCommonStockPrimaryIssue = Field()
    TotalCommonSharesOutstanding = Field()
    NetIncomeStartingLine = Field()
    DepreciationDepreciation = Field()
    Amortization = Field()
    DeferredTaxes = Field()
    NonCashItems = Field()
    ChangesInWorkingCapital = Field()
    CashFromOperatingActivities = Field()
    CapitalExpenditures = Field()
    OtherInvestingCashFlowItemsTotal = Field()
    CashFromInvestingActivities = Field()
    FinancingCashFlowItems = Field()
    TotalCashDividendsPaid = Field()
    IssuanceRetirementofStockNet = Field()
    IssuanceRetitementOfDebtNet = Field()
    CashFromFinancingActivities = Field()
    ForeignExchangeEffects = Field()
    NetChangeInCash = Field()
    CashInterestPaidSupplemental = Field()
    CashTaxesPaidSupplemental = Field()









