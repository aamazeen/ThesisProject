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
# stock_info["AAQC"] = yf.Ticker("AAQC").info
# stock_info["AAQC"] = {"open_price": yf.Ticker("AAQC").info['open']}
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

# from tqdm import tqdm
# from time import sleep
#
# for i in tqdm(range(100)):
#     sleep(0.02)

# example_dict = {'A': 1, 'B': 2}
# additions = {'A': 1, 'B': 2, 'C': 3}
#
# for item in additions:
#     if item in example_dict:
#         example_dict[item] += additions[item]
#     else:
#         example_dict[item] = additions[item]
#
# print(example_dict)

# import csv
#
# d = {}
# with open('current_positions.csv', 'r', newline='') as f:
#     reader = csv.reader(f, delimiter=',')
#     next(reader)  # toss headers
#     for ticker, shares, value in reader:
#         if ticker == 'Cash':
#             d[ticker] = float(value)
#         else:
#             d[ticker] = float(shares)
#
# print(d)

# import os
# import datetime
#
# def generate_csv_filename(prefix):
#     now = datetime.datetime.now()
#     formatted_date = now.strftime("%Y%m%d%H%M")
#     filename = f"{prefix}_{formatted_date}.csv"
#     return filename
#
# def get_most_recent_csv_file(directory, prefix):
#     prefix_files = [file for file in os.listdir(directory) if file.startswith(prefix)]
#
#     if prefix_files:
#         prefix_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
#         most_recent_csv = prefix_files[0]
#         return most_recent_csv
#     else:
#         return None  # No files found with the specified prefix
#
# # Function to get the most recent file for each prefix
# def get_most_recent_files_for_prefixes(directory, prefixes):
#     most_recent_files = {}
#     for prefix in prefixes:
#         most_recent_files[prefix] = get_most_recent_csv_file(directory, prefix)
#     return most_recent_files
#
# # Provide the path to your directory where CSV files are stored
# directory_path = "."
#
# # List of prefixes for your files
# file_prefixes = ["current_positions", "stock_data", "ticker_symbols", "transactions"]
#
# # Get the most recent file for each prefix
# recent_files_for_prefixes = get_most_recent_files_for_prefixes(directory_path, file_prefixes)
#
# # Display the most recent file for each prefix
# for prefix, recent_file in recent_files_for_prefixes.items():
#     if recent_file:
#         print(f"The most recent '{prefix}' CSV file is: {recent_file}")
#     else:
#         print(f"No '{prefix}' CSV files found in the directory.")
#
# for key in recent_files_for_prefixes:
#     print(key + recent_files_for_prefixes[key])


# import pandas as pd
# import numpy as np
# from pypfopt.efficient_frontier import EfficientFrontier
# from pypfopt import risk_models
# from pypfopt import expected_returns
#
# # Generating random stock names for demonstration purposes
# np.random.seed(123)
# num_stocks = 5
# stocks = ['Stock_' + str(i) for i in range(1, num_stocks+1)]
#
# # Creating random returns data for stocks
# num_obs = 1000
# np.random.seed(456)
# stock_returns = np.random.rand(num_obs, num_stocks)  # Random returns data
# dates = pd.date_range(start='1/1/2020', periods=num_obs, freq='D')
# returns_df = pd.DataFrame(stock_returns, columns=stocks, index=dates)
#
# # Displaying the randomly generated returns data
# print("\nRandomly generated returns data for demonstration purposes:")
# print(returns_df.head())
#
# # Calculate expected returns and sample covariance matrix
# mu = expected_returns.mean_historical_return(returns_df)
# Sigma = risk_models.sample_cov(returns_df)
#
# # Optimize for maximum Sharpe ratio
# ef = EfficientFrontier(mu, Sigma)
# weights = ef.max_sharpe()
# cleaned_weights = ef.clean_weights()
#
# # Display the optimal weights for assets and portfolio performance
# print("\nOptimal weights:\n")
# print(cleaned_weights)
# print("\nExpected return, Volatility, Sharpe ratio:")
# print(ef.portfolio_performance(verbose=True))

# ticker_symbols = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'NVDA', 'META', 'BRK.B', 'TSLA', 'LLY', 'V', 'AVGO', 'JPM',
#                   'UNH', 'WMT', 'XOM', 'MA', 'JNJ', 'PG', 'HD', 'COST', 'MRK', 'ORCL', 'ABBV', 'CVX', 'ADBE', 'CRM',
#                   'KO', 'BAC', 'AMD', 'PEP', 'ACN', 'NFLX', 'MCD', 'TMO', 'CSCO', 'INTC', 'LIN', 'ABT', 'TMUS',
#                   'CMCSA', 'WFC', 'INTU', 'DHR', 'DIS', 'AMGN', 'VZ', 'PFE', 'NKE', 'QCOM', 'IBM', 'TXN', 'NOW', 'PM',
#                   'CAT', 'MS', 'UNP', 'BX', 'GE', 'SPGI', 'UPS', 'AXP', 'COP', 'HON', 'BA', 'UBER', 'ISRG', 'PLD',
#                   'LOW', 'AMAT', 'NEE', 'RTX', 'GS', 'BKNG', 'BLK', 'SYK', 'T', 'MDT', 'SCHW', 'LMT', 'VRTX', 'ELV',
#                   'DE', 'TJX', 'GILD', 'SBUX', 'PANW', 'BMY', 'C', 'LRCX', 'REGN', 'MDLZ', 'PGR', 'CVS', 'AMT', 'ADP',
#                   'ETN', 'MMC', 'ADI', 'CB', 'ZTS', 'MU', 'CI', 'ABNB', 'BSX', 'FI', 'ANET', 'SO', 'SHW', 'EQIX',
#                   'ITW', 'KLAC', 'DUK', 'HCA', 'SNPS', 'MO', 'WM', 'CDNS', 'NOC', 'SLB', 'ICE', 'CME', 'GD', 'MCO',
#                   'CSX', 'BDX', 'EOG', 'CL', 'MAR', 'PYPL', 'USB', 'TGT', 'MCK', 'LULU', 'CMG', 'FDX', 'MNST', 'CTAS',
#                   'AON', 'MPC', 'MMM', 'PNC', 'PH', 'FCX', 'APD', 'PSX', 'APH', 'TDG', 'ROP', 'ECL', 'ORLY', 'TT',
#                   'EMR', 'HUM', 'CHTR', 'NXPI', 'MSI', 'RSG', 'PXD', 'NSC', 'PSA', 'ADSK', 'DHI', 'OXY', 'MET',
#                   'WELL', 'AJG', 'PCAR', 'TFC', 'CCI', 'COF', 'AFL', 'DXCM', 'GM', 'EL', 'FTNT', 'SPG', 'SRE', 'AIG',
#                   'STZ', 'CARR', 'HLT', 'KHC', 'MCHP', 'ROST', 'CPRT', 'F', 'EW', 'VLO', 'TRV', 'KDP', 'IDXX', 'AZO',
#                   'COR', 'HES', 'NEM', 'MSCI', 'PAYX', 'AEP', 'LEN', 'O', 'WMB', 'ODFL', 'BK', 'CNC', 'KMB', 'GWW',
#                   'NUE', 'DLR', 'KVUE', 'OKE', 'TEL', 'MRNA', 'KMI', 'D', 'ALL', 'LHX', 'CTSH', 'IQV', 'HSY', 'AMP',
#                   'JCI', 'A', 'SYY', 'URI', 'AME', 'DOW', 'LVS', 'PCG', 'PRU', 'ADM', 'EA', 'FIS', 'FAST', 'YUM',
#                   'CEG', 'GIS', 'BIIB', 'EXC', 'IT', 'OTIS', 'ROK', 'GEHC', 'VRSK', 'PPG', 'CSGP', 'GPN', 'XEL',
#                   'CMI', 'KR', 'NDAQ', 'CTVA', 'DD', 'EXR', 'VICI', 'BKR', 'ON', 'ED', 'IR', 'RCL', 'HAL', 'MLM',
#                   'LYB', 'FICO', 'ANSS', 'PEG', 'EFX', 'VMC', 'DLTR', 'DG', 'HPQ', 'PWR', 'CDW', 'ACGL', 'MPWR',
#                   'FANG', 'TTWO', 'DVN', 'DFS', 'EIX', 'XYL', 'BF.B', 'KEYS', 'WEC', 'GLW', 'CAH', 'CBRE', 'WBD',
#                   'AVB', 'SBAC', 'AWK', 'ZBH', 'WST', 'WTW', 'MTD', 'RMD', 'FTV', 'DAL', 'HIG', 'TROW', 'WY', 'TSCO',
#                   'CHD', 'BR', 'GRMN', 'STT', 'EQR', 'ULTA', 'FITB', 'WAB', 'NVR', 'RJF', 'APTV', 'HWM', 'PHM', 'DTE',
#                   'MOH', 'MTB', 'STE', 'FE', 'ARE', 'ILMN', 'ETR', 'EBAY', 'BRO', 'ROL', 'CCL', 'LYV', 'VRSN', 'ALGN',
#                   'TDY', 'INVH', 'HPE', 'BLDR', 'VTR', 'EXPE', 'DOV', 'PTC', 'FLT', 'IFF', 'BAX', 'WBA', 'PPL', 'ES',
#                   'JBHT', 'IRM', 'GPC', 'CTRA', 'COO', 'K', 'LH', 'AEE', 'AXON', 'WRB', 'PFG', 'DRI', 'TRGP', 'VLTO',
#                   'EXPD', 'STLD', 'WAT', 'HBAN', 'TYL', 'CNP', 'NTAP', 'MKC', 'EPAM', 'AKAM', 'CLX', 'BALL', 'FDS',
#                   'OMC', 'HUBB', 'ATO', 'HOLX', 'HRL', 'NTRS', 'STX', 'FSLR', 'LUV', 'RF', 'CMS', 'J', 'CINF', 'SWKS',
#                   'JBL', 'WDC', 'EG', 'CE', 'TER', 'ESS', 'BBY', 'AVY', 'L', 'TSN', 'IEX', 'MAA', 'TXT', 'EQT', 'LW',
#                   'DGX', 'SYF', 'LDOS', 'MAS', 'ENPH', 'SNA', 'PKG', 'GEN', 'ALB', 'POOL', 'CFG', 'CF', 'SWK', 'FOX',
#                   'FOXA', 'MGM', 'DPZ', 'NDSN', 'AMCR', 'NWS', 'BEN', 'INCY', 'NWSA', 'VTRS', 'PODD', 'HST', 'KIM',
#                   'CAG', 'BG', 'SJM', 'MRO', 'RVTY', 'TAP', 'CBOE', 'KEY', 'UAL', 'IP', 'CPB', 'LNT', 'ZBRA', 'TRMB',
#                   'UDR', 'LKQ', 'EVRG', 'AES', 'IPG', 'JKHY', 'AOS', 'NI', 'JNPR', 'REG', 'TFX', 'PNR', 'NRG', 'TECH',
#                   'PEAK', 'PAYC', 'GL', 'KMX', 'BXP', 'CRL', 'UHS', 'MOS', 'WRK', 'WYNN', 'CPT', 'FFIV', 'ALLE',
#                   'EMN', 'CDAY', 'CHRW', 'MKTX', 'HII', 'MTCH', 'APA', 'DVA', 'QRVO', 'HSIC', 'CZR', 'BBWI', 'BIO',
#                   'RL', 'CTLT', 'PARA', 'AIZ', 'AAL', 'RHI', 'ETSY', 'FRT', 'TPR', 'PNW', 'IVZ', 'XRAY', 'BWA',
#                   'GNRC', 'FMC', 'CMA', 'NCLH', 'HAS', 'MHK', 'VFC', 'WHR', 'ZION']
#
# ticker_symbols = [
#     'MMM', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AAP', 'AES',
#     'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALXN', 'ALGN', 'ALLE',
#     'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP',
#     'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS',
#     'ANTM', 'AON', 'AOS', 'APA', 'AAPL', 'AMAT', 'APTV', 'ADM', 'ANET', 'AJG',
#     'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BKR', 'BLL', 'BAC',
#     'BK', 'BAX', 'BDX', 'BRK.B', 'BBY', 'BIO', 'BIIB', 'BLK', 'BA', 'BKNG',
#     'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BF.B', 'CHRW', 'COG', 'CDNS',
#     'CZR', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE',
#     'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CERN', 'CF', 'SCHW', 'CHTR', 'CVX',
#     'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX',
#     'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'CXO', 'COP',
#     'ED', 'STZ', 'COO', 'CPRT', 'GLW', 'CTVA', 'COST', 'CCI', 'CSX', 'CMI',
#     'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM',
#     'FANG', 'DLR', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DPZ',
#     'DOV', 'DOW', 'DTE', 'DUK', 'DRE', 'DD', 'DXC', 'EMN', 'ETN', 'EBAY',
#     'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ETR', 'EOG', 'EFX', 'EQIX', 'EQR', 'ESS',
#     'EL', 'ETSY', 'EVRG', 'ES', 'RE', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM',
#     'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FRC', 'FISV',
#     'FLT', 'FLIR', 'FLS', 'FMC', 'F', 'FTNT', 'FTV', 'FBHS', 'FOXA', 'FOX',
#     'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD',
#     'GL', 'GPN', 'GS', 'GWW', 'HAL', 'HBI', 'HIG', 'HAS', 'HCA', 'PEAK', 'HSIC',
#     'HSY', 'HES', 'HPE', 'HLT', 'HFC', 'HOLX', 'HD', 'HON', 'HRL', 'HST',
#     'HWM', 'HPQ', 'HUM', 'HBAN', 'HII', 'IEX', 'IDXX', 'INFO', 'ITW', 'ILMN',
#     'INCY', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG',
#     'IVZ', 'IPGP', 'IQV', 'IRM', 'JKHY', 'J', 'JBHT', 'SJM', 'JNJ', 'JCI',
#     'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC',
#     'KHC', 'KR', 'LB', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LEG', 'LDOS', 'LEN',
#     'LLY', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LUMN', 'LYB', 'MTB',
#     'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MKC', 'MXIM',
#     'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT',
#     'MAA', 'MHK', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI',
#     'MSCI', 'MYL', 'NDAQ', 'NOV', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS',
#     'NEE', 'NLSN', 'NKE', 'NI', 'NSC', 'NTRS', 'NOC', 'NLOK', 'NCLH', 'NRG',
#     'NUE', 'NVDA', 'NVR', 'ORLY', 'OXY', 'ODFL', 'OMC', 'OKE', 'ORCL', 'OTIS',
#     'PCAR', 'PKG', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PENN', 'PNR', 'PBCT', 'PEP',
#     'PKI', 'PRGO', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG',
#     'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PTC', 'PEG', 'PSA', 'PHM',
# ]
#
#
# ticker_set = set(ticker_symbols)
# ticker_list = sorted(list(ticker_set))
# print(ticker_list)
# print(len(ticker_list))


# # various imports - add whichever others are needed
# from time import *
# from stocks import *
# from os import path
# from stocksymbol import StockSymbol
# from tqdm import tqdm
# import yfinance as yf
# import csv
# import schedule
# import datetime
# import pytz
# import holidays
# import os
#
# # various declarations
# market_open = False	    # beginning value of False to be tested daily
# directory_path = '.'    # path to the directory where CSV files are stored
# file_prefixes = ['current_positions', 'stock_data', 'transactions']   # v1 list of file prefixes
# # file_prefixes = ['current_positions', 'stock_data', 'ticker_symbols', 'transactions']   # v2 list of file prefixes
stock_tickers = [
    'A', 'AAL', 'AAPL', 'ABBV', 'ABNB', 'ABT', 'ACGL', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES',
    'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALL', 'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP',
    'AMT', 'AMZN', 'ANET', 'ANSS', 'AON', 'AOS', 'APA', 'APD', 'APH', 'APTV', 'ARE', 'ATO', 'AVB', 'AVGO', 'AVY', 'AWK',
    'AXON', 'AXP', 'AZO', 'BA', 'BAC', 'BALL', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BG', 'BIIB', 'BIO', 'BK',
    'BKNG', 'BKR', 'BLDR', 'BLK', 'BMY', 'BR', 'BRO', 'BSX', 'BWA', 'BX', 'BXP', 'C', 'CAG', 'CAH', 'CARR',
    'CAT', 'CB', 'CBOE', 'CBRE', 'CCI', 'CCL', 'CDAY', 'CDNS', 'CDW', 'CE', 'CEG', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR',
    'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO', 'COP', 'COR',
    'COST', 'CPB', 'CPRT', 'CPT', 'CRL', 'CRM', 'CSCO', 'CSGP', 'CSX', 'CTAS', 'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CVS',
    'CVX', 'CZR', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ',
    'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EG', 'EIX', 'EL', 'ELV', 'EMN', 'EMR',
    'ENPH', 'EOG', 'EPAM', 'EQIX', 'EQR', 'EQT', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE',
    'EXR', 'F', 'FANG', 'FAST', 'FCX', 'FDS', 'FDX', 'FE', 'FFIV', 'FI', 'FICO', 'FIS', 'FITB', 'FLT', 'FMC', 'FOX',
    'FOXA', 'FRT', 'FSLR', 'FTNT', 'FTV', 'GD', 'GE', 'GEHC', 'GEN', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GNRC', 'GOOG',
    'GOOGL', 'GPC', 'GPN', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HCA', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOLX',
    'HON', 'HPE', 'HPQ', 'HRL', 'HSIC', 'HST', 'HSY', 'HUBB', 'HUM', 'HWM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN',
    'INCY', 'INTC', 'INTU', 'INVH', 'IP', 'IPG', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JBL',
    'JCI', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'K', 'KDP', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO',
    'KR', 'KVUE', 'L', 'LDOS', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNT', 'LOW', 'LRCX', 'LULU', 'LUV',
    'LVS', 'LW', 'LYB', 'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'META',
    'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOH', 'MOS', 'MPC', 'MPWR', 'MRK', 'MRNA', 'MRO',
    'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTCH', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NDSN', 'NEE', 'NEM', 'NFLX', 'NI', 'NKE',
    'NOC', 'NOW', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWS', 'NWSA', 'NXPI', 'O', 'ODFL', 'OKE', 'OMC',
    'ON', 'ORCL', 'ORLY', 'OTIS', 'OXY', 'PANW', 'PARA', 'PAYC', 'PAYX', 'PCAR', 'PCG', 'PEAK', 'PEG', 'PEP', 'PFE',
    'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PODD', 'POOL', 'PPG', 'PPL', 'PRU',
    'PSA', 'PSX', 'PTC', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD',
    'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'RVTY', 'SBAC', 'SBUX', 'SCHW', 'SHW', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO',
    'SPG', 'SPGI', 'SRE', 'STE', 'STLD', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG',
    'TDY', 'TECH', 'TEL', 'TER', 'TFC', 'TFX', 'TGT', 'TJX', 'TMO', 'TMUS', 'TPR', 'TRGP', 'TRMB', 'TROW', 'TRV',
    'TSCO', 'TSLA', 'TSN', 'TT', 'TTWO', 'TXN', 'TXT', 'TYL', 'UAL', 'UBER', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS',
    'URI', 'USB', 'V', 'VFC', 'VICI', 'VLO', 'VLTO', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VTRS', 'VZ', 'WAB', 'WAT',
    'WBA', 'WBD', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WTW', 'WY', 'WYNN',
    'XEL', 'XOM', 'XRAY', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS'
]   # list of Fortune 500 ticker symbols took out BF.B and BRK.B
# list_of_stocks = []	    # list of Stock objects containing information on every stock that will be tested
# current_positions = {}
# tz = pytz.timezone('US/Eastern')    # timezone used for determining market open status
# us_holidays = holidays.country_holidays('US')   # list of holidays used for determining market open status
#
#
# # define methods
# def create_directory(directory, prefix):
#     prefix_directory = os.path.join(directory, prefix)
#     os.makedirs(prefix_directory, exist_ok=True)
#
#
# def create_stock_objects(missing_stocks):
#     global list_of_stocks
#     if len(missing_stocks) > 0:
#         for item in missing_stocks:
#             temp_stock = Stock(item,
#                                missing_stocks[item]['open_price'],
#                                missing_stocks[item]['current_price'],
#                                missing_stocks[item]['year_high'],
#                                missing_stocks[item]['year_low'],
#                                missing_stocks[item]['company_name'])
#             list_of_stocks.append(temp_stock)
#
#
# def daily_steps():  # we will cycle through this one every day
#     global market_open
#     market_open = is_market_open()  # changes value to True if the stock market is open that day
#     # temp_sell_decisions = {}    # used to store temporary ticker:shares pairs to execute trades later
#     # temp_buy_decisions = {}     # used to store temporary ticker:shares pairs to execute trades later
#
#     if market_open:
#         # stock_tickers = update_ticker_list()
#         # with open('ticker_symbols.csv', 'w', newline='') as fp:
#         #     write_csv = csv.writer(fp)
#         #     for item in stock_tickers:
#         #         write_csv.writerow(item)
#         temp_stock_data = fetch_stock_data(stock_tickers)
#         missing_stocks = find_missing_stocks(temp_stock_data)
#         create_stock_objects(missing_stocks)
#         update_stock_values(temp_stock_data)
#         if len(current_positions) > 1:   # 'Cash' will always be there, so checking if there is anything else
#             temp_sell_decisions = to_sell_or_not_to_sell(temp_stock_data)
#             if len(temp_sell_decisions) > 0:
#                 execute_orders(temp_stock_data, temp_sell_decisions)
#         if current_positions['Cash']['value'] > 0:
#             temp_buy_decisions = to_buy_or_not_to_buy(temp_stock_data)
#             if len(temp_buy_decisions) > 0:
#                 execute_orders(temp_stock_data, temp_buy_decisions)
#         with open(write_csv_file(directory_path, 'current_positions'), 'w', newline='') as fp:
#             write_csv = csv.writer(fp)
#             write_csv.writerow(['Item', 'Shares', 'Value ($)'])
#             for key in current_positions:
#                 write_csv.writerow([key, current_positions[key]['shares'], current_positions[key]['value']])
#
#     print('DONE!!')
#     market_open = False
#
#
# def execute_orders(temp_stock_data, trade_decisions):
#     global current_positions
#     global recent_files_for_prefixes
#     existing_content = []
#     for item in tqdm(trade_decisions, desc='Execute Orders'):
#         if item in current_positions:
#             current_positions[item]['shares'] += trade_decisions[item]
#         else:
#             current_positions[item] = {'shares': 0.0, 'value': 0.0}
#             current_positions[item]['shares'] = float(trade_decisions[item])
#         if trade_decisions[item] == -current_positions[item]['shares']:
#             current_positions['Cash']['value'] += current_positions[item]['value']
#         else:
#             current_positions['Cash']['value'] -= trade_decisions[item] * temp_stock_data[item]['current_price']
#         # add or subtract the number of shares from current_positions
#         # add or subtract the amount of cash from current_positions
#         if current_positions[item]['shares'] == 0.0:
#             del current_positions[item]
#         # if not path.isfile('transactions.csv'):
#         if recent_files_for_prefixes['transactions']:
#             with open(recent_files_for_prefixes['transactions'], 'r') as fp:
#                 reader = csv.reader(fp)
#                 next(reader)
#                 existing_content = list(reader)
#         with open(write_csv_file(directory_path, 'transactions'), 'w', newline='') as fp:
#             write_csv = csv.writer(fp)
#             write_csv.writerow(['DateTime', 'Ticker', 'Old Balance', 'Transaction Amount', 'New Balance'])
#             # write existing content to the new file
#             write_csv.writerows(existing_content)
#             write_csv.writerow([datetime.datetime.now(tz).strftime('%Y-%m-%d'),
#                                 item,
#                                 current_positions[item]['value'] -
#                                 trade_decisions[item] * temp_stock_data[item]['current_price'],
#                                 trade_decisions[item] * temp_stock_data[item]['current_price'],
#                                 current_positions[item]['value']])
#         # with open('transactions.csv', 'a', newline='') as fp:
#         #     write_csv = csv.writer(fp)
#         #     write_csv.writerow([datetime.datetime.now(tz).strftime('%Y-%m-%d'),
#         #                         item,
#         #                         current_positions[item]['value'] -
#         #                         trade_decisions[item] * temp_stock_data[item]['current_price'],
#         #                         trade_decisions[item] * temp_stock_data[item]['current_price'],
#         #                         current_positions[item]['value']])
#
#
# def fetch_stock_data(stock_ticker_list):
#     stock_data = {}
#     for item in tqdm(stock_ticker_list, desc='Fetch Data'):
#         try:
#             temp_data = yf.Ticker(item).info
#             stock_data[item] = {'open_price': temp_data['open'],
#                                 'current_price': temp_data['currentPrice'],
#                                 'year_high': temp_data['fiftyTwoWeekHigh'],
#                                 'year_low': temp_data['fiftyTwoWeekLow'],
#                                 'company_name': temp_data['shortName']}
#         except:
#             pass
#     with open(write_csv_file(directory_path, 'stock_data'), 'w', newline='') as fp:
#         write_csv = csv.writer(fp)
#         write_csv.writerow(['ticker', 'open_price', 'current_price', 'year_high', 'year_low', 'company_name'])
#         for key in stock_data:
#             write_csv.writerow([key,
#                                 stock_data[key]['open_price'],
#                                 stock_data[key]['current_price'],
#                                 stock_data[key]['year_high'],
#                                 stock_data[key]['year_low'],
#                                 stock_data[key]['company_name']])
#     return stock_data
#
#
# def find_missing_stocks(temp_stock_data):
#     temp_missing_stocks = {}
#     for item in temp_stock_data:
#         stock_found = False		# changes value to True if the match is found
#         for stock in list_of_stocks:
#             if item == stock.ticker:
#                 stock_found = True
#                 break
#             else:
#                 continue
#         if stock_found:
#             continue
#         else:
#             temp_missing_stocks[item] = temp_stock_data[item]
#     return temp_missing_stocks
#
#
# def generate_csv_filename(prefix):
#     now = datetime.datetime.now()
#     formatted_date = now.strftime('%Y%m%d%H%M')
#     filename = f'{prefix}_{formatted_date}.csv'
#     return filename
#
#
# def get_most_recent_csv_file(directory, prefix):
#     prefix_files = [file for file in os.listdir(directory) if file.startswith(prefix)]
#
#     if prefix_files:
#         prefix_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
#         most_recent_csv = prefix_files[0]
#         return most_recent_csv
#     else:
#         return None  # No files found with the specified prefix
#
#
# # Function to get the most recent file for each prefix
# def get_most_recent_files_for_prefixes(directory, prefixes):
#     most_recent_files = {}
#     for prefix in prefixes:
#         most_recent_files[prefix] = get_most_recent_csv_file(directory, prefix)
#     return most_recent_files
#
#
# def is_market_open():
#     now = datetime.datetime.now(tz)
#     open_time = datetime.time(hour=9, minute=30, second=0)
#     close_time = datetime.time(hour=16, minute=0, second=0)
#     # If a holiday
#     if now.strftime('%Y-%m-%d') in us_holidays:
#         # Override for testing
#         override_request = input('Override market_open (t/f)? ')
#         if override_request == 't':
#             return True
#         else:
#             return False
#     # If before 0930 or after 1600
#     elif (now.time() < open_time) or (now.time() > close_time):
#         # Override for testing
#         override_request = input('Override market_open (t/f)? ')
#         if override_request == 't':
#             return True
#         else:
#             return False
#     # If it's a weekend
#     elif now.date().weekday() > 4:
#         # Override for testing
#         override_request = input('Override market_open (t/f)? ')
#         if override_request == 't':
#             return True
#         else:
#             return False
#     else:
#         return True
#
#
# def to_buy_or_not_to_buy(temp_stock_data):
#     temp_decisions = {}
#     for item in temp_stock_data:
#         if temp_stock_data[item]['current_price'] < 50.0:
#             if current_positions['Cash']['value'] >= temp_stock_data[item]['current_price']:
#                 temp_decisions[item] = 1.0
#         # perform tests to see if an amount should be bought/how much
#         # if shares should be bought, and we have sufficient cash:
#         #     add ticker:shares(+) pair to temp_decisions
#     return temp_decisions
#
#
# def to_sell_or_not_to_sell(temp_stock_data):
#     temp_decisions = {}
#     for item in current_positions:
#         if item == 'Cash':
#             continue
#         elif item not in temp_stock_data:
#             print(item + ' is not listed in temp_stock_data')
#             temp_decisions[item] = -current_positions[item]['shares']
#         elif temp_stock_data[item]['current_price'] < 50.0:
#             if current_positions[item]['shares'] > 1.0:
#                 temp_decisions[item] = -1.0
#             # perform tests to see if an amount should be sold/how much
#             # if shares should be sold, and we have sufficient shares:
#             #     add ticker:shares(-) pair to temp_decisions
#     return temp_decisions
#
#
# def update_stock_values(stock_data):
#     global list_of_stocks
#     global current_positions
#     for item in list_of_stocks:
#         if item.ticker not in stock_data:
#             print(item.ticker + ' is not listed in stock_data')
#         else:
#             item.open_price = stock_data[item.ticker]['open_price']
#             item.current_price = stock_data[item.ticker]['current_price']
#             item.year_high = stock_data[item.ticker]['year_high']
#             item.year_low = stock_data[item.ticker]['year_low']
#             if item.ticker in current_positions:
#                 current_positions[item.ticker]['value'] = (float(current_positions[item.ticker]['shares']) *
#                                                            stock_data[item.ticker]['current_price'])
#
#
# # def update_ticker_list():
# #     api_key = 'c2267d8c-c557-4c9e-848b-c537a794a84c'
# #     ss = StockSymbol(api_key)
# #     set_of_symbols = set()
# #
# #     # get symbol list based on market
# #     symbol_list_us = ss.get_symbol_list(market='US')  # 'us' or 'america' will also work
# #     for item in symbol_list_us:
# #         set_of_symbols.add(item['symbol'])
# #
# #     # Some stocks are 5 characters. Those stocks are not of interest.
# #     del_set = set()
# #     sav_set = set()
# #
# #     for symbol in set_of_symbols:
# #         if len(symbol) > 4:
# #             del_set.add(symbol)
# #         else:
# #             sav_set.add(symbol)
# #
# #     list_of_symbols = sorted(list(sav_set))
# #     return list_of_symbols
#
#
# def write_csv_file(directory, prefix):
#     create_directory(directory, prefix)
#     filename = generate_csv_filename(prefix)
#     file_path = os.path.join(directory, prefix, filename)
#     return file_path
#
#
# recent_files_for_prefixes = get_most_recent_files_for_prefixes(directory_path, file_prefixes)
# if recent_files_for_prefixes['current_positions']:
#     with open(get_most_recent_csv_file(directory_path, 'current_positions')) as f:
#         reader = csv.reader(f, delimiter=',')
#         next(reader)    # toss headers
#         for ticker, shares, value in reader:
#             current_positions[ticker] = {'shares': float(shares), 'value': float(value)}
#             # load dictionary with existing positions
# else:
#     current_positions = {'Cash': {'shares': 0.0, 'value': 100000.0}}  # adding tickers when purchased
# # if not path.isfile('current_positions.csv'):
# #     current_positions = {'Cash': {'shares': 0.0, 'value': 100000.0}}  # adding tickers when purchased
# # else:
# #     with open('current_positions.csv', 'r', newline='') as f:
# #         reader = csv.reader(f, delimiter=',')
# #         next(reader)  # toss headers
# #         for ticker, shares, value in reader:
# #             current_positions[ticker] = {'shares': float(shares), 'value': float(value)}
# #             # load dictionary with existing positions
#
#
# for i in range(3):
#     daily_steps()

# # this is the part that runs every day
# # schedule.every().day.at('12:00').do(daily_steps)
#
# # while True:
# #     # Checks whether a scheduled task is pending to run or not
# #     schedule.run_pending()
# #     sleep(1)
#
#
# def round_up(number, decimal_places):
#     temp_number = number * (10 ** decimal_places)
#     adjusted_number = temp_number + 0.5
#     rounded_number = round(adjusted_number) / (10 ** decimal_places)
#     return rounded_number
#
#
# print(round_up(-3.14159265358979, 0))

# noinspection PyStatementEffect
# {'address1': 'One Microsoft Way', 'city': 'Redmond', 'state': 'WA', 'zip': '98052-6399', 'country': 'United States',
#  'phone': '425 882 8080', 'website': 'https://www.microsoft.com', 'industry': 'Software - Infrastructure',
#  'industryKey': 'software-infrastructure', 'industryDisp': 'Software - Infrastructure', 'sector': 'Technology',
#  'sectorKey': 'technology', 'sectorDisp': 'Technology',
#  'longBusinessSummary': 'Microsoft Corporation develops and supports software, services, devices and solutions'
#                         'worldwide. The Productivity and Business Processes segment offers office, exchange,'
#                         'SharePoint, Microsoft Teams, office 365 Security and Compliance, Microsoft viva, and Microsoft'
#                         '365 copilot; and office consumer services, such as Microsoft 365 consumer subscriptions,'
#                         'Office licensed on-premises, and other office services. This segment also provides LinkedIn;'
#                         'and dynamics business solutions, including Dynamics 365, a set of intelligent, cloud-based'
#                         'applications across ERP, CRM, power apps, and power automate; and on-premises ERP and CRM'
#                         'applications. The Intelligent Cloud segment offers server products and cloud services, such as'
#                         'azure and other cloud services; SQL and windows server, visual studio, system center, and'
#                         'related client access licenses, as well as nuance and GitHub; and enterprise services'
#                         'including enterprise support services, industry solutions, and nuance professional services.'
#                         'The More Personal Computing segment offers Windows, including windows OEM licensing and other'
#                         'non-volume licensing of the Windows operating system; Windows commercial comprising volume'
#                         'licensing of the Windows operating system, windows cloud services, and other Windows'
#                         'commercial offerings; patent licensing; and windows Internet of Things; and devices, such as'
#                         'surface, HoloLens, and PC accessories. Additionally, this segment provides gaming, which'
#                         'includes Xbox hardware and content, and first- and third-party content; Xbox game pass and'
#                         'other subscriptions, cloud gaming, advertising, third-party disc royalties, and other cloud'
#                         'services; and search and news advertising, which includes Bing, Microsoft News and Edge, and'
#                         'third-party affiliates. The company sells its products through OEMs, distributors, and'
#                         'resellers; and directly through digital marketplaces, online, and retail stores. The company'
#                         'was founded in 1975 and is headquartered in Redmond, Washington.',
#  'fullTimeEmployees': 221000,
#  'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Satya  Nadella', 'age': 56, 'title': 'Chairman & CEO', 'yearBorn': 1967,
#                       'fiscalYear': 2023, 'totalPay': 9276400, 'exercisedValue': 0, 'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Mr. Bradford L. Smith LCA', 'age': 64, 'title': 'President & Vice Chairman',
#                       'yearBorn': 1959, 'fiscalYear': 2023, 'totalPay': 3591277, 'exercisedValue': 0,
#                       'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Ms. Amy E. Hood', 'age': 51, 'title': 'Executive VP & CFO',
#                       'yearBorn': 1972, 'fiscalYear': 2023, 'totalPay': 3452196, 'exercisedValue': 0,
#                       'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Mr. Judson B. Althoff', 'age': 49,
#                       'title': 'Executive VP & Chief Commercial Officer', 'yearBorn': 1974, 'fiscalYear': 2023,
#                       'totalPay': 3355797, 'exercisedValue': 0, 'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Mr. Christopher David Young', 'age': 51,
#                       'title': 'Executive Vice President of Business Development, Strategy & Ventures',
#                       'yearBorn': 1972, 'fiscalYear': 2023, 'totalPay': 2460507, 'exercisedValue': 0,
#                       'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Ms. Alice L. Jolla', 'age': 56,
#                       'title': 'Corporate VP & Chief Accounting Officer', 'yearBorn': 1967, 'fiscalYear': 2023,
#                       'exercisedValue': 0, 'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Mr. James Kevin Scott', 'age': 51, 'title': 'Executive VP of AI & CTO',
#                       'yearBorn': 1972, 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Brett  Iversen', 'title': 'Vice President of Investor Relations',
#                       'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Mr. Hossein  Nowbar', 'title': 'Chief Legal Officer', 'fiscalYear': 2023,
#                       'exercisedValue': 0, 'unexercisedValue': 0},
#                      {'maxAge': 1, 'name': 'Mr. Frank X. Shaw', 'title': 'Chief Communications Officer',
#                       'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0}],
#  'auditRisk': 6, 'boardRisk': 3, 'compensationRisk': 3, 'shareHolderRightsRisk': 2, 'overallRisk': 2,
#  'governanceEpochDate': 1711670400, 'compensationAsOfEpochDate': 1703980800, 'maxAge': 86400, 'priceHint': 2,
#  'previousClose': 421.43, 'open': 421.05, 'dayLow': 419.14, 'dayHigh': 421.87, 'regularMarketPreviousClose': 421.43,
#  'regularMarketOpen': 421.05, 'regularMarketDayLow': 419.14, 'regularMarketDayHigh': 421.87, 'dividendRate': 3.0,
#  'dividendYield': 0.0070999996, 'exDividendDate': 1715731200, 'payoutRatio': 0.2523, 'fiveYearAvgDividendYield': 0.95,
#  'beta': 0.89, 'trailingPE': 38.039783, 'forwardPE': 34.01132, 'volume': 21871161, 'regularMarketVolume': 21871161,
#  'averageVolume': 22936715, 'averageVolume10days': 18901212, 'averageDailyVolume10Day': 18901212,
#  'marketCap': 3126134571008, 'fiftyTwoWeekLow': 275.37, 'fiftyTwoWeekHigh': 430.82,
#  'priceToSalesTrailing12Months': 13.736239, 'fiftyDayAverage': 411.2622, 'twoHundredDayAverage': 363.093,
#  'trailingAnnualDividendRate': 2.86, 'trailingAnnualDividendYield': 0.0067864177, 'currency': 'USD',
#  'enterpriseValue': 3156509196288, 'profitMargins': 0.36269, 'floatShares': 7418919053, 'sharesOutstanding': 7430439936,
#  'sharesShort': 54210656, 'sharesShortPriorMonth': 42451775, 'sharesShortPreviousMonthDate': 1707955200,
#  'dateShortInterest': 1710460800, 'sharesPercentSharesOut': 0.0073, 'heldPercentInsiders': 0.00054000004,
#  'heldPercentInstitutions': 0.73861, 'shortRatio': 2.46, 'shortPercentOfFloat': 0.0073,
#  'impliedSharesOutstanding': 7430439936, 'bookValue': 32.06, 'priceToBook': 13.122894, 'lastFiscalYearEnd': 1688083200,
#  'nextFiscalYearEnd': 1719705600, 'mostRecentQuarter': 1703980800, 'earningsQuarterlyGrowth': 0.332,
#  'netIncomeToCommon': 82541002752, 'trailingEps': 11.06, 'forwardEps': 12.37, 'pegRatio': 2.59,
#  'lastSplitFactor': '2:1', 'lastSplitDate': 1045526400, 'enterpriseToRevenue': 13.87, 'enterpriseToEbitda': 26.654,
#  '52WeekChange': 0.46474946, 'SandP52WeekChange': 0.27393317, 'lastDividendValue': 0.75, 'lastDividendDate': 1707868800,
#  'exchange': 'NMS', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 'underlyingSymbol': 'MSFT',
#  'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 'firstTradeDateEpochUtc': 511108200,
#  'timeZoneFullName': 'America/New_York', 'timeZoneShortName': 'EDT', 'uuid': 'b004b3ec-de24-385e-b2c1-923f10d3fb62',
#  'messageBoardId': 'finmb_21835', 'gmtOffSetMilliseconds': -14400000, 'currentPrice': 420.72, 'targetHighPrice': 505.89,
#  'targetLowPrice': 275.98, 'targetMeanPrice': 425.08, 'targetMedianPrice': 427.72, 'recommendationMean': 1.7,
#  'recommendationKey': 'buy', 'numberOfAnalystOpinions': 48, 'totalCash': 80981999616, 'totalCashPerShare': 10.899,
#  'ebitda': 118427000832, 'totalDebt': 111358001152, 'quickRatio': 1.096, 'currentRatio': 1.218,
#  'totalRevenue': 227583000576, 'debtToEquity': 46.736, 'revenuePerShare': 30.612, 'returnOnAssets': 0.1519,
#  'returnOnEquity': 0.39174, 'freeCashflow': 58680999936, 'operatingCashflow': 102646996992, 'earningsGrowth': 0.332,
#  'revenueGrowth': 0.176, 'grossMargins': 0.69815004, 'ebitdaMargins': 0.52037, 'operatingMargins': 0.43585998,
#  'financialCurrency': 'USD', 'trailingPegRatio': 2.1338}

['MSFT', 'AAPL', 'NVDA', 'AMZN', 'GOOG', 'GOOGL', 'META', 'BRK.B', 'LLY', 'AVGO', 'JPM', 'V', 'TSLA', 'WMT', 'XOM', 'MA', 'UNH', 'PG', 'JNJ', 'HD', 'ORCL', 'MRK', 'COST', 'ABBV', 'CVX', 'CRM', 'BAC', 'AMD', 'NFLX', 'KO', 'PEP', 'LIN', 'TMO', 'ADBE', 'DIS', 'ACN', 'WFC', 'CSCO', 'ABT', 'TMUS', 'QCOM', 'CAT', 'DHR', 'VZ', 'INTU', 'IBM', 'AMAT', 'GE', 'INTC', 'CMCSA', 'UBER', 'AXP', 'NOW', 'COP', 'BX', 'TXN', 'MS', 'PFE', 'UNP', 'AMGN', 'PM', 'ISRG', 'SPGI', 'MU', 'NKE', 'RTX', 'SYK', 'GS', 'ETN', 'NEE', 'HON', 'UPS', 'SCHW', 'LRCX', 'T', 'PGR', 'BKNG', 'BLK', 'C', 'ELV', 'PLD', 'DE', 'BA', 'MDT', 'TJX', 'LMT', 'CI', 'VRTX', 'ABNB', 'BMY', 'CB', 'REGN', 'MMC', 'BSX', 'ADP', 'SBUX', 'ADI', 'CVS', 'FI', 'ANET', 'KLAC', 'MDLZ', 'AMT', 'SNPS', 'GILD', 'HCA', 'PANW', 'CDNS', 'SHW', 'WM', 'GD', 'TGT', 'CMG', 'MPC', 'EOG', 'SLB', 'ITW', 'ICE', 'CME', 'ZTS', 'SO', 'EQIX', 'DUK', 'MAR', 'PSX', 'MO', 'PH', 'CL', 'CSX', 'MCK', 'BDX', 'FCX', 'APH', 'PYPL', 'TT', 'TDG', 'CTAS', 'FDX', 'NOC', 'USB', 'EMR', 'ECL', 'PCAR', 'PXD', 'AON', 'PNC', 'NXPI', 'VLO', 'OXY', 'CEG', 'RSG', 'MNST', 'ROP', 'MSI', 'NSC', 'EW', 'SMCI', 'FTNT', 'CPRT', 'COF', 'AZO', 'DXCM', 'HLT', 'APD', 'MET', 'AJG', 'TRV', 'ADSK', 'AIG', 'DHI', 'WELL', 'EL', 'F', 'GM', 'CARR', 'TFC', 'MMM', 'GWW', 'PSA', 'AFL', 'SPG', 'COR', 'ODFL', 'STZ', 'NUE', 'HES', 'WMB', 'URI', 'MCHP', 'ROST', 'OKE', 'NEM', 'LEN', 'O', 'ALL', 'KHC', 'SRE', 'AMP', 'TEL', 'DLR', 'JCI', 'AEP', 'PAYX', 'CCI', 'FAST', 'IQV', 'LULU', 'IDXX', 'MSCI', 'BK', 'CMI', 'KDP', 'KMB', 'A', 'AME', 'DOW', 'FIS', 'PRU', 'KR', 'KMI', 'D', 'GEHC', 'LVS', 'LHX', 'MRNA', 'OTIS', 'HSY', 'GIS', 'CTVA', 'CNC', 'CSGP', 'KVUE', 'CHTR', 'PWR', 'YUM', 'MLM', 'IR', 'HUM', 'SYY', 'EXC', 'HAL', 'IT', 'FANG', 'PCG', 'VMC', 'NDAQ', 'CTSH', 'ACGL', 'DG', 'EA', 'RCL', 'BKR', 'CDW', 'LYB', 'DVN', 'PEG', 'VRSK', 'PPG', 'GPN', 'ADM', 'ROK', 'EFX', 'MPWR', 'DFS', 'DD', 'XYL', 'ED', 'EXR', 'FICO', 'HIG', 'VICI', 'ANSS', 'DAL', 'FTV', 'BIIB', 'ON', 'XEL', 'CBRE', 'WST', 'DLTR', 'HPQ', 'GRMN', 'MTD', 'RMD', 'GLW', 'WTW', 'HWM', 'KEYS', 'EIX', 'TSCO', 'RJF', 'EBAY', 'CAH', 'WAB', 'ZBH', 'TROW', 'TRGP', 'AVB', 'TTWO', 'WEC', 'NVR', 'WY', 'CHD', 'BLDR', 'PHM', 'BRO', 'BF.B', 'DOV', 'FITB', 'LYV', 'ALGN', 'BR', 'WDC', 'HPE', 'AXON', 'EQR', 'STLD', 'SBAC', 'MTB', 'AWK', 'IRM', 'STT', 'DECK', 'DTE', 'HUBB', 'WRB', 'ETR', 'PTC', 'MOH', 'CPAY', 'ROL', 'FE', 'ARE', 'NTAP', 'BAX', 'VLTO', 'ULTA', 'IFF', 'INVH', 'STE', 'CTRA', 'BALL', 'GPC', 'TSN', 'WBD', 'ES', 'ILMN', 'APTV', 'JBHT', 'MKC', 'PPL', 'WAT', 'PFG', 'HBAN', 'TDY', 'K', 'COO', 'AEE', 'CBOE', 'CINF', 'HRL', 'VRSN', 'STX', 'CCL', 'DRI', 'FSLR', 'J', 'TXT', 'RF', 'OMC', 'HOLX', 'IEX', 'CLX', 'CE', 'LH', 'JBL', 'CNP', 'NTRS', 'TYL', 'AVY', 'LDOS', 'CMS', 'ATO', 'VTR', 'EXPE', 'BBY', 'MRO', 'L', 'LUV', 'EXPD', 'MAS', 'SWKS', 'PKG', 'SYF', 'FDS', 'EG', 'WBA', 'TER', 'AKAM', 'EQT', 'CF', 'CFG', 'ENPH', 'SNA', 'NDSN', 'EPAM', 'ESS', 'BG', 'NRG', 'POOL', 'TRMB', 'ZBRA', 'MAA', 'CAG', 'MGM', 'NWSA', 'NWS', 'SWK', 'DGX', 'ALB', 'BEN', 'TAP', 'HST', 'UAL', 'FOX', 'FOXA', 'GEN', 'KEY', 'VTRS', 'PNR', 'LKQ', 'IP', 'AMCR', 'APA', 'DOC', 'CRL', 'CPB', 'AOS', 'KMX', 'AES', 'RVTY', 'WRK', 'LNT', 'KIM', 'SJM', 'INCY', 'JKHY', 'NI', 'WYNN', 'JNPR', 'UDR', 'SOLV', 'EVRG', 'IPG', 'DVA', 'EMN', 'LW', 'ALLE', 'PODD', 'PAYC', 'HII', 'FFIV', 'RL', 'QRVO', 'REG', 'TECH', 'MOS', 'GL', 'UHS', 'CPT', 'CTLT', 'BBWI', 'TFX', 'TPR', 'BXP', 'DAY', 'BIO', 'AIZ', 'HSIC', 'CZR', 'MTCH', 'AAL', 'PNW', 'MKTX', 'CHRW', 'FRT', 'GNRC', 'NCLH', 'RHI', 'BWA', 'HAS', 'MHK', 'ETSY', 'IVZ', 'PARA', 'FMC', 'CMA']