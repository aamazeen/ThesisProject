# various imports - add whichever others are needed
from time import *
from stocks import *
from os import path
from stocksymbol import StockSymbol
from tqdm import tqdm
import yfinance as yf
import csv
import schedule
import datetime
import pytz
import holidays

# various declarations
market_open = False	    # beginning value of False to be tested daily
# stock_tickers = []    # list of ticker symbols updated daily
list_of_stocks = []	    # list of Stock objects containing information on every stock that will be tested
current_positions = {}
if not path.isfile('current_positions.csv'):
    current_positions = {'Cash': {'shares': 0.0, 'value': 100000.0}}  # adding tickers when purchased
else:
    with open('current_positions.csv', 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # toss headers
        for ticker, shares, value in reader:
            current_positions[ticker] = {'shares': float(shares), 'value': float(value)}
            # load dictionary with existing positions
tz = pytz.timezone('US/Eastern')    # timezone used for determining market open status
us_holidays = holidays.country_holidays('US')   # list of holidays used for determining market open status
# TODO: defining global variables


# define methods
def create_stock_objects(missing_stocks):
    global list_of_stocks
    if len(missing_stocks) > 0:
        for item in missing_stocks:
            temp_stock = Stock(item,
                               missing_stocks[item]['open_price'],
                               missing_stocks[item]['current_price'],
                               missing_stocks[item]['year_high'],
                               missing_stocks[item]['year_low'],
                               missing_stocks[item]['company_name'])
            list_of_stocks.append(temp_stock)


def daily_steps():  # we will cycle through this one every day
    global market_open
    market_open = is_market_open()  # changes value to True if the stock market is open that day
    # temp_sell_decisions = {}    # used to store temporary ticker:shares pairs to execute trades later
    # temp_buy_decisions = {}     # used to store temporary ticker:shares pairs to execute trades later

    if market_open:
        stock_tickers = update_ticker_list()
        with open('ticker_symbols.csv', 'w', newline='') as fp:
            write_csv = csv.writer(fp)
            for item in stock_tickers:
                write_csv.writerow(item)
        temp_stock_data = fetch_stock_data(stock_tickers)
        missing_stocks = find_missing_stocks(temp_stock_data)
        create_stock_objects(missing_stocks)
        update_stock_values(temp_stock_data)
        if len(current_positions) > 1:   # 'Cash' will always be there, so checking if there is anything else
            temp_sell_decisions = to_sell_or_not_to_sell(temp_stock_data)
            if len(temp_sell_decisions) > 0:
                execute_orders(temp_stock_data, temp_sell_decisions)
        if current_positions['Cash']['value'] > 0:
            temp_buy_decisions = to_buy_or_not_to_buy(temp_stock_data)
            if len(temp_buy_decisions) > 0:
                execute_orders(temp_stock_data, temp_buy_decisions)
        with open('current_positions.csv', 'w', newline='') as fp:
            write_csv = csv.writer(fp)
            write_csv.writerow(['Item', 'Shares', 'Value ($)'])
            for key in current_positions:
                write_csv.writerow([key, current_positions[key]['shares'], current_positions[key]['value']])

    print('DONE!!')
    market_open = False


# TODO: change this into actual code
def execute_orders(temp_stock_data, trade_decisions):
    global current_positions
    for item in tqdm(trade_decisions, desc='Execute Orders'):
        if item in current_positions:
            current_positions[item]['shares'] += trade_decisions[item]
        else:
            current_positions[item] = {'shares': 0.0, 'value': 0.0}
            current_positions[item]['shares'] = float(trade_decisions[item])
        if trade_decisions[item] == -current_positions[item]['shares']:
            current_positions['Cash']['value'] += current_positions[item]['value']
        else:
            current_positions['Cash']['value'] -= trade_decisions[item] * temp_stock_data[item]['current_price']
        # add or subtract the number of shares from current_positions
        # add or subtract the amount of cash from current_positions
        if current_positions[item]['shares'] == 0.0:
            del current_positions[item]
        if not path.isfile('transactions.csv'):
            with open('transactions.csv', 'w', newline='') as fp:
                write_csv = csv.writer(fp)
                write_csv.writerow(['DateTime', 'Ticker', 'Old Balance', 'Transaction Amount', 'New Balance'])
        with open('transactions.csv', 'a', newline='') as fp:
            write_csv = csv.writer(fp)
            write_csv.writerow([datetime.datetime.now(tz).strftime('%Y-%m-%d'),
                                item,
                                current_positions[item]['value'] -
                                trade_decisions[item] * temp_stock_data[item]['current_price'],
                                trade_decisions[item] * temp_stock_data[item]['current_price'],
                                current_positions[item]['value']])


# TODO: change this to pull the actual data needed for algorithms
def fetch_stock_data(stock_ticker_list):
    stock_data = {}
    for item in tqdm(stock_ticker_list, desc='Fetch Data'):
        try:
            temp_data = yf.Ticker(item).info
            stock_data[item] = {'open_price': temp_data['open'],
                                'current_price': temp_data['currentPrice'],
                                'year_high': temp_data['fiftyTwoWeekHigh'],
                                'year_low': temp_data['fiftyTwoWeekLow'],
                                'company_name': temp_data['shortName']}
        except:
            pass
    with open('stock_data.csv', 'w', newline='') as fp:
        write_csv = csv.writer(fp)
        write_csv.writerow(['ticker', 'open_price', 'current_price', 'year_high', 'year_low', 'company_name'])
        for key in stock_data:
            write_csv.writerow([key,
                                stock_data[key]['open_price'],
                                stock_data[key]['current_price'],
                                stock_data[key]['year_high'],
                                stock_data[key]['year_low'],
                                stock_data[key]['company_name']])
    return stock_data


def find_missing_stocks(temp_stock_data):
    temp_missing_stocks = {}
    for item in temp_stock_data:
        stock_found = False		# changes value to True if the match is found
        for stock in list_of_stocks:
            if item == stock.ticker:
                stock_found = True
                break
            else:
                continue
        if stock_found:
            continue
        else:
            temp_missing_stocks[item] = temp_stock_data[item]
    return temp_missing_stocks


def is_market_open():
    now = datetime.datetime.now(tz)
    open_time = datetime.time(hour=9, minute=30, second=0)
    close_time = datetime.time(hour=16, minute=0, second=0)
    # If a holiday
    if now.strftime('%Y-%m-%d') in us_holidays:
        # Override for testing
        override_request = input('Override market_open (t/f)? ')
        if override_request == 't':
            return True
        else:
            return False
    # If before 0930 or after 1600
    elif (now.time() < open_time) or (now.time() > close_time):
        # Override for testing
        override_request = input('Override market_open (t/f)? ')
        if override_request == 't':
            return True
        else:
            return False
    # If it's a weekend
    elif now.date().weekday() > 4:
        # Override for testing
        override_request = input('Override market_open (t/f)? ')
        if override_request == 't':
            return True
        else:
            return False
    else:
        return True


# TODO: change this into actual code
def to_buy_or_not_to_buy(temp_stock_data):
    temp_decisions = {}
    for item in temp_stock_data:
        # TODO: this is financial decision making for Buy
        if temp_stock_data[item]['current_price'] < 50.0:
            if current_positions['Cash']['value'] >= temp_stock_data[item]['current_price']:
                temp_decisions[item] = 1.0
        # perform tests to see if an amount should be bought/how much
        # if shares should be bought, and we have sufficient cash:
        #     add ticker:shares(+) pair to temp_decisions
    return temp_decisions


# TODO: change this into actual code
def to_sell_or_not_to_sell(temp_stock_data):
    temp_decisions = {}
    for item in current_positions:
        if item == 'Cash':
            continue
        elif item not in temp_stock_data:
            print(item + ' is not listed in temp_stock_data')
            temp_decisions[item] = -current_positions[item]['shares']
        # TODO: this is financial decision making for Sell
        elif temp_stock_data[item]['current_price'] < 50.0:
            if current_positions[item]['shares'] > 1.0:
                temp_decisions[item] = -1.0
            # perform tests to see if an amount should be sold/how much
            # if shares should be sold, and we have sufficient shares:
            #     add ticker:shares(-) pair to temp_decisions
    return temp_decisions


# TODO: change this when I figure out what information I actually need
def update_stock_values(stock_data):
    global list_of_stocks
    global current_positions
    for item in list_of_stocks:
        if item.ticker not in stock_data:
            print(item.ticker + ' is not listed in stock_data')
        else:
            item.open_price = stock_data[item.ticker]['open_price']
            item.current_price = stock_data[item.ticker]['current_price']
            item.year_high = stock_data[item.ticker]['year_high']
            item.year_low = stock_data[item.ticker]['year_low']
            if item.ticker in current_positions:
                current_positions[item.ticker]['value'] = (float(current_positions[item.ticker]['shares']) *
                                                           stock_data[item.ticker]['current_price'])


def update_ticker_list():
    api_key = 'c2267d8c-c557-4c9e-848b-c537a794a84c'
    ss = StockSymbol(api_key)
    set_of_symbols = set()

    # get symbol list based on market
    symbol_list_us = ss.get_symbol_list(market="US")  # "us" or "america" will also work
    for item in symbol_list_us:
        set_of_symbols.add(item['symbol'])

    # Some stocks are 5 characters. Those stocks are not of interest.
    del_set = set()
    sav_set = set()

    for symbol in set_of_symbols:
        if len(symbol) > 4:
            del_set.add(symbol)
        else:
            sav_set.add(symbol)

    list_of_symbols = sorted(list(sav_set))
    return list_of_symbols


for i in range(3):
    daily_steps()

# this is the part that runs every day
# schedule.every().day.at("12:00").do(daily_steps)

# while True:
#     # Checks whether a scheduled task is pending to run or not
#     schedule.run_pending()
#     sleep(1)
