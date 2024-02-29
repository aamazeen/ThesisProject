# various imports in alphabetical order - add whichever others are needed
import csv
import datetime
from holidays import *
import numpy as np
from os import listdir, makedirs, path
from pytz import *
from scipy.optimize import minimize
from stocks import *
import time
from tqdm import tqdm
import yfinance as yf

# various declarations in alphabetical order
current_positions = {}
directory_path = '.'    # path to the directory where CSV files are stored
file_prefixes = ['current_positions', 'stock_data', 'transactions']   # v1 list of file prefixes
list_of_stocks = []	    # list of Stock objects containing information on every stock that will be tested
market_open = False	    # beginning value of False to be tested daily
stock_tickers = [
    'A', 'AAL', 'AAPL', 'ABBV', 'ABNB', 'ABT', 'ACGL', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES',
    'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALL', 'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP',
    'AMT', 'AMZN', 'ANET', 'ANSS', 'AON', 'AOS', 'APA', 'APD', 'APH', 'APTV', 'ARE', 'ATO', 'AVB', 'AVGO', 'AVY', 'AWK',
    'AXON', 'AXP', 'AZO', 'BA', 'BAC', 'BALL', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BG', 'BIIB', 'BIO', 'BK', 'BKNG',
    'BKR', 'BLDR', 'BLK', 'BMY', 'BR', 'BRO', 'BSX', 'BWA', 'BX', 'BXP', 'C', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBOE',
    'CBRE', 'CCI', 'CCL', 'CDAY', 'CDNS', 'CDW', 'CE', 'CEG', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL',
    'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO', 'COP', 'COR', 'COST', 'CPB', 'CPRT',
    'CPT', 'CRL', 'CRM', 'CSCO', 'CSGP', 'CSX', 'CTAS', 'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CVS', 'CVX', 'CZR', 'D', 'DAL',
    'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ', 'DRI', 'DTE', 'DUK', 'DVA',
    'DVN', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EG', 'EIX', 'EL', 'ELV', 'EMN', 'EMR', 'ENPH', 'EOG', 'EPAM',
    'EQIX', 'EQR', 'EQT', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG',
    'FAST', 'FCX', 'FDS', 'FDX', 'FE', 'FFIV', 'FI', 'FICO', 'FIS', 'FITB', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRT', 'FSLR',
    'FTNT', 'FTV', 'GD', 'GE', 'GEHC', 'GEN', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GNRC', 'GOOG', 'GOOGL', 'GPC', 'GPN',
    'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HCA', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOLX', 'HON', 'HPE', 'HPQ',
    'HRL', 'HSIC', 'HST', 'HSY', 'HUBB', 'HUM', 'HWM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INTC',
    'INTU', 'INVH', 'IP', 'IPG', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JBL', 'JCI', 'JKHY',
    'JNJ', 'JNPR', 'JPM', 'K', 'KDP', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'KVUE', 'L',
    'LDOS', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNT', 'LOW', 'LRCX', 'LULU', 'LUV', 'LVS', 'LW', 'LYB',
    'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'META', 'MGM', 'MHK', 'MKC',
    'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOH', 'MOS', 'MPC', 'MPWR', 'MRK', 'MRNA', 'MRO', 'MS', 'MSCI', 'MSFT',
    'MSI', 'MTB', 'MTCH', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NDSN', 'NEE', 'NEM', 'NFLX', 'NI', 'NKE', 'NOC', 'NOW', 'NRG',
    'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWS', 'NWSA', 'NXPI', 'O', 'ODFL', 'OKE', 'OMC', 'ON', 'ORCL', 'ORLY',
    'OTIS', 'OXY', 'PANW', 'PARA', 'PAYC', 'PAYX', 'PCAR', 'PCG', 'PEAK', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH',
    'PHM', 'PKG', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PODD', 'POOL', 'PPG', 'PPL', 'PRU', 'PSA', 'PSX', 'PTC', 'PWR',
    'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK', 'ROL', 'ROP', 'ROST',
    'RSG', 'RTX', 'RVTY', 'SBAC', 'SBUX', 'SCHW', 'SHW', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STE',
    'STLD', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TDY', 'TECH', 'TEL', 'TER',
    'TFC', 'TFX', 'TGT', 'TJX', 'TMO', 'TMUS', 'TPR', 'TRGP', 'TRMB', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TT',
    'TTWO', 'TXN', 'TXT', 'TYL', 'UAL', 'UBER', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'USB', 'V', 'VFC',
    'VICI', 'VLO', 'VLTO', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WBD', 'WDC', 'WEC',
    'WELL', 'WFC', 'WHR', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WTW', 'WY', 'WYNN', 'XEL', 'XOM', 'XRAY', 'XYL',
    'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS'
]   # list of Fortune 500 ticker symbols, took out BF.B and BRK.B
tz = timezone('US/Eastern')    # timezone used for determining market open status
us_holidays = country_holidays('US')   # list of holidays used for determining market open status


# define methods in alphabetical order
def buy_or_sell(prices, weights):
    decisions = {}
    portfolio_value = 0
    for item in current_positions:
        portfolio_value += current_positions[item]['value']
    for item in weights:
        # print(item + ': ' + weights[item])
        if item in current_positions:
            if current_positions[item]['value'] / portfolio_value == weights[item]:
                continue
            else:
                decisions[item] = round(((weights[item] - (current_positions[item]['value'] / portfolio_value)) *
                                         portfolio_value) / prices[item][-1], 4)
        elif weights[item] == 0:
            continue
        else:
            decisions[item] = round((weights[item] * portfolio_value) / prices[item][-1], 4)
    # TODO: See if this works, then delete the print statement
    print('Decisions: ', decisions)
    return decisions


def create_directory(directory, prefix):
    prefix_directory = path.join(directory, prefix)
    makedirs(prefix_directory, exist_ok=True)


def create_stock_objects(missing_stocks):
    global list_of_stocks
    if len(missing_stocks) > 0:
        for item in missing_stocks:
            temp_stock = Stock(item, missing_stocks[item]['prices'], missing_stocks[item]['returns'])
            list_of_stocks.append(temp_stock)


def daily_steps():  # we will cycle through this one every day
    global market_open
    market_open = is_market_open()  # changes value to True if the stock market is open that day
    # temp_sell_decisions = {}    # used to store temporary ticker:shares pairs to execute trades later
    # temp_buy_decisions = {}     # used to store temporary ticker:shares pairs to execute trades later

    if market_open:
        # stock_tickers = update_ticker_list()
        # with open('ticker_symbols.csv', 'w', newline='') as fp:
        #     write_csv = csv.writer(fp)
        #     for item in stock_tickers:
        #         write_csv.writerow(item)
        temp_stock_data = fetch_stock_data()
        temp_stock_prices = temp_stock_data['stock_prices']
        temp_stock_returns = temp_stock_data['stock_returns']
        missing_stocks = find_missing_stocks(temp_stock_prices, temp_stock_returns)
        create_stock_objects(missing_stocks)
        update_stock_values(temp_stock_prices, temp_stock_returns)
        temp_weights = optimal_weights(temp_stock_returns)
        temp_trade_decisions = buy_or_sell(temp_stock_prices, temp_weights)
        execute_orders(temp_stock_prices, temp_trade_decisions)
        # if len(current_positions) > 1:   # 'Cash' will always be there, so checking if there is anything else
        #     temp_sell_decisions = to_sell_or_not_to_sell(temp_stock_data)
        #     if len(temp_sell_decisions) > 0:
        #         execute_orders(temp_stock_data, temp_sell_decisions)
        # if current_positions['Cash']['value'] > 0:
        #     temp_buy_decisions = to_buy_or_not_to_buy(temp_stock_data)
        #     if len(temp_buy_decisions) > 0:
        #         execute_orders(temp_stock_data, temp_buy_decisions)
        with open(write_csv_file(directory_path, 'current_positions'), 'w', newline='') as fp:
            write_csv = csv.writer(fp)
            write_csv.writerow(['Item', 'Shares', 'Value ($)'])
            for key in current_positions:
                write_csv.writerow([key, current_positions[key]['shares'], current_positions[key]['value']])

    print('DONE!!')
    market_open = False


# TODO: change this into actual code
def execute_orders(prices, trade_decisions):
    global current_positions
    global recent_files_for_prefixes
    existing_content = []
    if get_most_recent_csv_file(directory_path, 'transactions'):
        with open(get_most_recent_csv_file(directory_path, 'transactions'), 'r') as fp:
            reader = csv.reader(fp)
            next(reader)
            existing_content = list(reader)
            # TODO: This printing statement only for debugging
            print(existing_content)
    # TODO: See if the above appends everything, then delete the below
    # if recent_files_for_prefixes['transactions']:
    #     with open(recent_files_for_prefixes['transactions'], 'r') as fp:
    #         reader = csv.reader(fp)
    #         next(reader)
    #         existing_content = list(reader)
    for item in tqdm(trade_decisions, desc='Execute Orders'):
        if trade_decisions[item] != 0:
            if item not in current_positions:
                current_positions[item] = {'shares': 0.0, 'value': 0.0}
            current_positions[item]['shares'] += trade_decisions[item]
            current_positions[item]['value'] = round(current_positions[item]['shares'] * prices[item][-1], 2)
            # if item in current_positions:
            #     current_positions[item]['shares'] += trade_decisions[item]
            # else:
            #     current_positions[item] = {'shares': 0.0, 'value': 0.0}
            #     current_positions[item]['shares'] = float(trade_decisions[item])
            # if trade_decisions[item] == -current_positions[item]['shares']:
            #     current_positions['Cash']['value'] += current_positions[item]['value']
            # else:
            #     current_positions['Cash']['value'] -= trade_decisions[item] * prices[item][-1]
            current_positions['Cash']['value'] -= round(trade_decisions[item] * prices[item][-1], 2)
            if current_positions['Cash']['value'] < 0:
                current_positions['Cash']['value'] = 0
            # add or subtract the number of shares from current_positions
            # add or subtract the amount of cash from current_positions
            if current_positions[item]['shares'] == 0.0:
                del current_positions[item]
            # if not path.isfile('transactions.csv'):

    # TODO: See if this works, then delete
    print(trade_decisions)

    with open(write_csv_file(directory_path, 'transactions'), 'w', newline='') as fp:
        write_csv = csv.writer(fp)
        write_csv.writerow(['DateTime', 'Ticker', 'Old Balance', 'Transaction Amount', 'New Balance'])
        # write existing content to the new file
        write_csv.writerows(existing_content)

    for item in trade_decisions:
        if trade_decisions[item] != 0:
            with open(write_csv_file(directory_path, 'transactions'), 'a', newline='') as fp:
                write_csv = csv.writer(fp)
                write_csv.writerow([datetime.datetime.now(tz).strftime('%Y-%m-%d'),
                                    item,
                                    current_positions[item]['value'] -
                                    trade_decisions[item] * prices[item][-1],
                                    trade_decisions[item] * prices[item][-1],
                                    current_positions[item]['value']])
            # with open('transactions.csv', 'a', newline='') as fp:
            #     write_csv = csv.writer(fp)
            #     write_csv.writerow([datetime.datetime.now(tz).strftime('%Y-%m-%d'),
            #                         item,
            #                         current_positions[item]['value'] -
            #                         trade_decisions[item] * temp_stock_data[item]['current_price'],
            #                         trade_decisions[item] * temp_stock_data[item]['current_price'],
            #                         current_positions[item]['value']])


# TODO: change this to pull the actual data needed for algorithms
def fetch_stock_data():
    global stock_tickers
    # Calculate yesterday's date
    end_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    stock_prices = {}
    stock_returns = {}
    for ticker in tqdm(stock_tickers, desc='Fetch Data'):
        try:
            temp_data = yf.download(ticker, start='2023-07-01', end=end_date)  # Adjust the date range as needed
            stock_prices[ticker] = temp_data['Adj Close'].tolist()
            stock_returns[ticker] = temp_data['Adj Close'].pct_change().dropna().tolist()
        except:
            pass
    # with open(write_csv_file(directory_path, 'stock_data'), 'w', newline='') as fp:
    #     write_csv = csv.writer(fp)
    #     write_csv.writerow(['ticker', 'open_price', 'current_price', 'year_high', 'year_low', 'company_name'])
    #     for key in stock_data:
    #         write_csv.writerow([key,
    #                             stock_data[key]['open_price'],
    #                             stock_data[key]['current_price'],
    #                             stock_data[key]['year_high'],
    #                             stock_data[key]['year_low'],
    #                             stock_data[key]['company_name']])
    return {'stock_prices': stock_prices, 'stock_returns': stock_returns}


def find_missing_stocks(tickers_and_prices, tickers_and_returns):
    temp_missing_stocks = {}
    for item in tickers_and_prices:
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
            temp_missing_stocks[item] = {'prices': tickers_and_prices[item], 'returns': tickers_and_returns[item]}
    return temp_missing_stocks


def generate_csv_filename(prefix):
    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y%m%d%H%M')
    filename = f'{prefix}_{formatted_date}.csv'
    return filename


def get_most_recent_csv_file(directory, prefix):
    prefix_files = [file for file in listdir(directory) if file.startswith(prefix)]

    if prefix_files:
        prefix_files.sort(key=lambda x: path.getmtime(path.join(directory, x)), reverse=True)
        most_recent_csv = prefix_files[0]
        # TODO: See if this actually worked
        if most_recent_csv[-4:0] == '.csv':
            return most_recent_csv
        else:
            return None # The 'file' it found was not actually a file
    else:
        return None  # No files found with the specified prefix


# Function to get the most recent file for each prefix
def get_most_recent_files_for_prefixes(directory, prefixes):
    most_recent_files = {}
    for prefix in prefixes:
        most_recent_files[prefix] = get_most_recent_csv_file(directory, prefix)
    return most_recent_files


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


def optimal_weights(returns):
    expected_returns = {}
    # Calculate expected returns and risks
    for item in list_of_stocks:
        expected_returns[item.ticker] = sum(item.returns) / len(item.returns)
    covariance_matrix = [[sum((ret_i - expected_returns[ticker_i]) * (ret_j - expected_returns[ticker_j])
                              for ret_i, ret_j in zip(returns[ticker_i], returns[ticker_j])) /
                          (len(returns[ticker_i]) - 1)
                          for ticker_j in stock_tickers] for ticker_i in stock_tickers]
    # covariance_matrix = [[sum((ret_i - expected_returns[ticker_i]) * (ret_j - expected_returns[ticker_j])
    #                           for ret_i, ret_j in zip(returns[ticker_i], returns[ticker_j])) /
    #                       (len(returns[ticker_i]) - 1)
    #                       for ticker_j in stock_tickers] for ticker_i in stock_tickers]

    # Generate random portfolios
    np.random.seed(42)  # For reproducibility
    num_portfolios = 10000

    weights = np.random.random(size=(num_portfolios, len(expected_returns)))
    weights /= np.sum(weights, axis=1)[:, np.newaxis]

    # Calculate portfolio returns and risks
    portfolio_returns = [sum(weight * expected_return for weight, expected_return
                             in zip(portfolio, expected_returns.values())) for portfolio in weights]
    portfolio_volatility = [np.sqrt(np.dot(weight, np.dot(covariance_matrix, weight))) for weight in weights]

    # Efficient Frontier
    portfolios = {'Return': portfolio_returns, 'Volatility': portfolio_volatility}

    # Optimal portfolio
    def objective(weights):
        return (-sum(weight * expected_return for weight, expected_return in zip(weights, expected_returns.values())) /
                np.sqrt(np.dot(weights, np.dot(covariance_matrix, weights))))

    constraints = ({'type': 'eq', 'fun': lambda weights: sum(weights) - 1})
    bounds = tuple((0, 1) for asset in range(len(expected_returns)))

    initial_weights = np.ones(len(expected_returns)) / len(expected_returns)

    optimal_portfolio = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

    # Extract optimal weights
    temp_optimal_weights = optimal_portfolio.x

    # Store optimal weights in a dictionary
    optimal_weights_dict = {ticker: weight for ticker, weight in zip(returns.keys(), temp_optimal_weights)}

    # Output optimal weights
    # print("Optimal Weights:")
    # for ticker, weight in optimal_weights_dict.items():
    #     print(f"{ticker}: {weight: .4f}")

    return optimal_weights_dict


# TODO: change this when I figure out what information I actually need
def update_stock_values(stock_prices, stock_returns):
    global list_of_stocks
    global current_positions
    for item in list_of_stocks:
        if item.ticker not in stock_prices:
            print(item.ticker + ' is not listed in stock_data')
        else:
            item.prices = stock_prices[item.ticker]
            item.prices = stock_returns[item.ticker]
            # item.open_price = stock_data[item.ticker]['open_price']
            # item.current_price = stock_data[item.ticker]['current_price']
            # item.year_high = stock_data[item.ticker]['year_high']
            # item.year_low = stock_data[item.ticker]['year_low']
            if item.ticker in current_positions:
                current_positions[item.ticker]['value'] = (float(current_positions[item.ticker]['shares']) *
                                                           stock_prices[item.ticker][-1])


def write_csv_file(directory, prefix):
    create_directory(directory, prefix)
    filename = generate_csv_filename(prefix)
    file_path = path.join(directory, prefix, filename)
    return file_path


start_time = time.time()

# TODO: Maybe move this stuff below to the daily_steps method so it runs every time, not just the first time
recent_files_for_prefixes = get_most_recent_files_for_prefixes(directory_path, file_prefixes)
# print(recent_files_for_prefixes)
if recent_files_for_prefixes['current_positions']:
    with open(get_most_recent_csv_file(directory_path, 'current_positions')) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)    # toss headers
        for ticker, shares, value in reader:
            current_positions[ticker] = {'shares': float(shares), 'value': float(value)}
            # load dictionary with existing positions
else:
    current_positions = {'Cash': {'shares': 0.0, 'value': 100000.0}}  # adding tickers when purchased
# if not path.isfile('current_positions.csv'):
#     current_positions = {'Cash': {'shares': 0.0, 'value': 100000.0}}  # adding tickers when purchased
# else:
#     with open('current_positions.csv', 'r', newline='') as f:
#         reader = csv.reader(f, delimiter=',')
#         next(reader)  # toss headers
#         for ticker, shares, value in reader:
#             current_positions[ticker] = {'shares': float(shares), 'value': float(value)}
#             # load dictionary with existing positions

# daily_steps()
for i in range(2):
    daily_steps()
    print("time elapsed: {:.2f}s".format(time.time() - start_time))















# import time
# start_time = time.time()
#
# # Calculate yesterday's date
# end_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
#
# # Step 1: Collect Data using yfinance
# symbols = [
#     'A', 'AAL', 'AAPL', 'ABBV', 'ABNB', 'ABT', 'ACGL', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES',
#     'AFL', 'AIG', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALL', 'ALLE', 'AMAT', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMP',
#     'AMT', 'AMZN', 'ANET', 'ANSS', 'AON', 'AOS', 'APA', 'APD', 'APH', 'APTV', 'ARE', 'ATO', 'AVB', 'AVGO', 'AVY', 'AWK',
#     'AXON', 'AXP', 'AZO', 'BA', 'BAC', 'BALL', 'BAX', 'BBWI', 'BBY', 'BDX', 'BEN', 'BG', 'BIIB', 'BIO', 'BK', 'BKNG',
#     'BKR', 'BLDR', 'BLK', 'BMY', 'BR', 'BRO', 'BSX', 'BWA', 'BX', 'BXP', 'C', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBOE',
#     'CBRE', 'CCI', 'CCL', 'CDAY', 'CDNS', 'CDW', 'CE', 'CEG', 'CF', 'CFG', 'CHD', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL',
#     'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COO', 'COP', 'COR', 'COST', 'CPB', 'CPRT',
#     'CPT', 'CRL', 'CRM', 'CSCO', 'CSGP', 'CSX', 'CTAS', 'CTLT', 'CTRA', 'CTSH', 'CTVA', 'CVS', 'CVX', 'CZR', 'D', 'DAL',
#     'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DLR', 'DLTR', 'DOV', 'DOW', 'DPZ', 'DRI', 'DTE', 'DUK', 'DVA',
#     'DVN', 'DXCM', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EG', 'EIX', 'EL', 'ELV', 'EMN', 'EMR', 'ENPH', 'EOG', 'EPAM',
#     'EQIX', 'EQR', 'EQT', 'ES', 'ESS', 'ETN', 'ETR', 'ETSY', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FANG',
#     'FAST', 'FCX', 'FDS', 'FDX', 'FE', 'FFIV', 'FI', 'FICO', 'FIS', 'FITB', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRT', 'FSLR',
#     'FTNT', 'FTV', 'GD', 'GE', 'GEHC', 'GEN', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GNRC', 'GOOG', 'GOOGL', 'GPC', 'GPN',
#     'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HCA', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOLX', 'HON', 'HPE', 'HPQ',
#     'HRL', 'HSIC', 'HST', 'HSY', 'HUBB', 'HUM', 'HWM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INTC',
#     'INTU', 'INVH', 'IP', 'IPG', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JBL', 'JCI', 'JKHY',
#     'JNJ', 'JNPR', 'JPM', 'K', 'KDP', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'KVUE', 'L',
#     'LDOS', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNT', 'LOW', 'LRCX', 'LULU', 'LUV', 'LVS', 'LW', 'LYB',
#     'LYV', 'MA', 'MAA', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'META', 'MGM', 'MHK', 'MKC',
#     'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOH', 'MOS', 'MPC', 'MPWR', 'MRK', 'MRNA', 'MRO', 'MS', 'MSCI', 'MSFT',
#     'MSI', 'MTB', 'MTCH', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NDSN', 'NEE', 'NEM', 'NFLX', 'NI', 'NKE', 'NOC', 'NOW', 'NRG',
#     'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NVR', 'NWS', 'NWSA', 'NXPI', 'O', 'ODFL', 'OKE', 'OMC', 'ON', 'ORCL', 'ORLY',
#     'OTIS', 'OXY', 'PANW', 'PARA', 'PAYC', 'PAYX', 'PCAR', 'PCG', 'PEAK', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH',
#     'PHM', 'PKG', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PODD', 'POOL', 'PPG', 'PPL', 'PRU', 'PSA', 'PSX', 'PTC', 'PWR',
#     'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK', 'ROL', 'ROP', 'ROST',
#     'RSG', 'RTX', 'RVTY', 'SBAC', 'SBUX', 'SCHW', 'SHW', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STE',
#     'STLD', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TDY', 'TECH', 'TEL', 'TER',
#     'TFC', 'TFX', 'TGT', 'TJX', 'TMO', 'TMUS', 'TPR', 'TRGP', 'TRMB', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TT',
#     'TTWO', 'TXN', 'TXT', 'TYL', 'UAL', 'UBER', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNP', 'UPS', 'URI', 'USB', 'V', 'VFC',
#     'VICI', 'VLO', 'VLTO', 'VMC', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WBD', 'WDC', 'WEC',
#     'WELL', 'WFC', 'WHR', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WTW', 'WY', 'WYNN', 'XEL', 'XOM', 'XRAY', 'XYL',
#     'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS'
# ]
#
# returns = {}
# for symbol in symbols:
#     stock_data = yf.download(symbol, start='2023-07-01', end=end_date)  # Adjust the date range as needed
#     returns[symbol] = stock_data['Adj Close'].pct_change().dropna().tolist()
#
# # Step 2: Calculate Expected Returns and Risks
# expected_returns = {ticker: sum(ret) / len(ret) for ticker, ret in returns.items()}
# covariance_matrix = [[sum((ret_i - expected_returns[ticker_i]) * (ret_j - expected_returns[ticker_j]) for ret_i, ret_j in zip(returns[ticker_i], returns[ticker_j])) / (len(returns[ticker_i]) - 1) for ticker_j in symbols] for ticker_i in symbols]
#
# # Step 3: Generate Random Portfolios
# np.random.seed(42)  # For reproducibility
# num_portfolios = 10000
#
# weights = np.random.random(size=(num_portfolios, len(expected_returns)))
# weights /= np.sum(weights, axis=1)[:, np.newaxis]
#
# # Step 4-5: Calculate Portfolio Returns and Risks
# portfolio_returns = [sum(weight * expected_return for weight, expected_return in zip(portfolio, expected_returns.values())) for portfolio in weights]
# portfolio_volatility = [np.sqrt(np.dot(weight, np.dot(covariance_matrix, weight))) for weight in weights]
#
# # Step 6: Efficient Frontier
# portfolios = {'Return': portfolio_returns, 'Volatility': portfolio_volatility}
#
#
# # Step 7: Optimal Portfolio
# def objective(weights):
#     return -sum(weight * expected_return for weight, expected_return in zip(weights, expected_returns.values())) / np.sqrt(np.dot(weights, np.dot(covariance_matrix, weights)))
#
#
# constraints = ({'type': 'eq', 'fun': lambda weights: sum(weights) - 1})
# bounds = tuple((0, 1) for asset in range(len(expected_returns)))
#
# initial_weights = np.ones(len(expected_returns)) / len(expected_returns)
#
# optimal_portfolio = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
#
# # Extract optimal weights
# optimal_weights = optimal_portfolio.x
#
# # Step 8: Rebalance
# # You can use optimal_weights to allocate proportions in your actual portfolio.
#
# # Store optimal weights in a dictionary
# optimal_weights_dict = {ticker: weight for ticker, weight in zip(returns.keys(), optimal_weights)}
#
# # Output Optimal Weights
# print("Optimal Weights:")
# for ticker, weight in optimal_weights_dict.items():
#     print(f"{ticker}: {weight:.4f}")
#
# print("time elapsed: {:.2f}s".format(time.time() - start_time))
#
# # print(returns)