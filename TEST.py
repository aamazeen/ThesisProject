"""test_dict = {'key1': 'value1', 'key2': 'value2'}
test_dict2 = {}
for item in test_dict:
    print(item)
    test_dict2[item] = test_dict[item]
print(test_dict2)


import requests
import json


def get_stock_price(symbol):
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=" + symbol
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    print(data)

    return data['quoteResponse']['result'][0]['regularMarketPrice']


print(get_stock_price('GOOG'))


import pandas as pd
from yahoo_fin import stock_info as si


# gather stock symbols from major US exchanges
df1 = pd.DataFrame( si.tickers_sp500() )
df2 = pd.DataFrame( si.tickers_nasdaq() )
df3 = pd.DataFrame( si.tickers_dow() )
df4 = pd.DataFrame( si.tickers_other() )

# convert DataFrame to list, then to sets
sym1 = set( symbol for symbol in df1[0].values.tolist() )
sym2 = set( symbol for symbol in df2[0].values.tolist() )
sym3 = set( symbol for symbol in df3[0].values.tolist() )
sym4 = set( symbol for symbol in df4[0].values.tolist() )

# join the 4 sets into one. Because it's a set, there will be no duplicate symbols
symbols = set.union( sym1, sym2, sym3, sym4 )

# Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
my_list = ['W', 'R', 'P', 'Q']
del_set = set()
sav_set = set()

for symbol in symbols:
    if len( symbol ) > 4 and symbol[-1] in my_list:
        del_set.add( symbol )
    else:
        sav_set.add( symbol )

print( f'Removed {len( del_set )} unqualified stock symbols...' )
print( f'There are {len( sav_set )} qualified stock symbols...' )



from stocksymbol import StockSymbol

api_key = 'c2267d8c-c557-4c9e-848b-c537a794a84c'
ss = StockSymbol(api_key)

setOfSymbols = set()

setOfExchanges = set()

# get symbol list based on market
symbol_list_us = ss.get_symbol_list(market="US") # "us" or "america" will also work
print(symbol_list_us)
for item in symbol_list_us:
    setOfExchanges.add(item['exchange'])
print(setOfExchanges)

for item in symbol_list_us:
    setOfSymbols.add(item['symbol'])
print(setOfSymbols)

# Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
del_set = set()
sav_set = set()

for symbol in setOfSymbols:
    if len(symbol) > 4:
        del_set.add(symbol)
    else:
        sav_set.add(symbol)

print(f'Removed {len(del_set)} unqualified stock symbols...')
print(f'There are {len(sav_set)} qualified stock symbols...')

listOfSymbols = sorted(list(sav_set))
print(listOfSymbols)"""

# get symbol list based on index
# symbol_list_spx = ss.get_symbol_list(index="SPX")

# show a list of available market
# market_list = ss.market_list

# show a list of available index
# index_list = ss.index_list

# import yfinance as yf
# stock_info = {}

# stock_info["MSFT"] = {"currentPrice": yf.Ticker("MSFT").info["currentPrice"]}
# print(stock_info)
# print(yf.Ticker("MSFT").info)
# print(stock_info["MSFT"]["currentPrice"])

# msft = yf.Ticker("MSFT")

# get all stock info
# msft.info

# get historical market data
# hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
# msft.history_metadata

# show actions (dividends, splits, capital gains)
# msft.actions
# msft.dividends
# msft.splits
# msft.capital_gains  # only for mutual funds & etfs

# show share count
# msft.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
# msft.income_stmt
# msft.quarterly_income_stmt
# - balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet
# - cash flow statement
# msft.cashflow
# msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
# msft.major_holders
# msft.institutional_holders
# msft.mutualfund_holders

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
# msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
# msft.isin

# show options expirations
# msft.options

# show news
# msft.news

# get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts

# import pandas_market_calendars as mcal
# nyse = mcal.get_calendar('NYSE')
# nyse.valid_days(start_date='2016-12-20', end_date='2017-01-10')

# import datetime, pytz, holidays
#
# tz = pytz.timezone('US/Eastern')
# us_holidays = holidays.US()
# now = None
#
# if not now:
#     now = datetime.datetime.now(tz)
# openTime = datetime.time(hour = 9, minute = 30, second = 0)
# closeTime = datetime.time(hour = 16, minute = 0, second = 0)
# # If a holiday
# if now.strftime('%Y-%m-%d') in us_holidays:
#     print('False')
# # If before 0930 or after 1600
# elif (now.time() < openTime) or (now.time() > closeTime):
#     print('False')
# # If it's a weekend
# elif now.date().weekday() > 4:
#     print('False')
# else:
#     print('True')
#
# print(datetime.datetime.now(tz).strftime('%Y-%m-%d'))