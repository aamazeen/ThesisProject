# various imports in alphabetical order - add whichever others are needed
import csv
import datetime
from holidays import *
import numpy as np
from os import listdir, makedirs, path
from pytz import *
import schedule
from scipy.optimize import minimize
from stocks import *
import time
from tqdm import tqdm
import yfinance as yf

# various declarations in alphabetical order
current_positions = {}
directory_path = '.'    # path to the directory where CSV files are stored
file_prefixes = ['current_positions', 'transactions']   # v1 list of file prefixes
list_of_stocks = []	    # list of Stock objects containing information on every stock that will be tested
market_open = False	    # beginning value of False to be tested daily
recent_files_for_prefixes = {}
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
        if item in current_positions:
            if current_positions[item]['value'] == round_up(portfolio_value * 0.9999 * weights[item], 2):
                continue
            else:
                decisions[item] = round(((weights[item] - (current_positions[item]['value'] /
                                                           (portfolio_value * 0.9999)))
                                         * portfolio_value * 0.9999) / prices[item][-1], 4)
        elif weights[item] == 0:
            continue
        else:
            decisions[item] = round((weights[item] * portfolio_value * 0.9999) / prices[item][-1], 4)
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

    start_time = time.time()
    market_open = is_market_open()  # changes value to True if the stock market is open that day

    if market_open:
        print('\n' * 100)
        establish_current_positions()
        temp_stock_data = fetch_stock_data()
        temp_stock_prices = temp_stock_data['stock_prices']
        temp_stock_returns = temp_stock_data['stock_returns']
        missing_stocks = find_missing_stocks(temp_stock_prices, temp_stock_returns)
        create_stock_objects(missing_stocks)
        update_stock_values(temp_stock_prices, temp_stock_returns)
        temp_weights = optimal_weights(temp_stock_returns)
        temp_trade_decisions = buy_or_sell(temp_stock_prices, temp_weights)
        execute_orders(temp_stock_prices, temp_trade_decisions)
        update_current_positions()

    print("Time elapsed: {:.2f}s".format(time.time() - start_time))
    market_open = False


def establish_current_positions():
    global current_positions
    global recent_files_for_prefixes
    recent_files_for_prefixes = get_most_recent_files_for_prefixes(directory_path, file_prefixes)
    if recent_files_for_prefixes['current_positions']:
        with open(get_most_recent_csv_file(directory_path, 'current_positions')) as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # toss headers
            for ticker, shares, value in reader:
                current_positions[ticker] = {'shares': float(shares), 'value': float(value)}
                # load dictionary with existing positions
    else:
        current_positions = {'Cash': {'shares': 0.0, 'value': 100000.0}}  # adding tickers when purchased


def execute_orders(prices, trade_decisions):
    global current_positions
    global recent_files_for_prefixes
    existing_content = []
    if get_most_recent_csv_file(directory_path, 'transactions'):
        with open(get_most_recent_csv_file(directory_path, 'transactions'), 'r') as fp:
            reader = csv.reader(fp)
            next(reader)
            existing_content = list(reader)
    for item in trade_decisions:
        if round_up(trade_decisions[item] * prices[item][-1], 2) != 0:
            if item not in current_positions:
                current_positions[item] = {'shares': 0.0, 'value': 0.0}
            current_positions[item]['shares'] += trade_decisions[item]
            current_positions[item]['value'] = round_up(current_positions[item]['shares'] * prices[item][-1], 2)
            current_positions['Cash']['value'] -= round_up(trade_decisions[item] * prices[item][-1], 2)

    with open(write_csv_file(directory_path, 'transactions'), 'w', newline='') as fp:
        write_csv = csv.writer(fp)
        write_csv.writerow(['Date', 'Ticker', 'Old Balance', 'Transaction Amount', 'New Balance'])
        # write existing content to the new file
        write_csv.writerows(existing_content)

    for item in trade_decisions:
        if round_up(trade_decisions[item] * prices[item][-1], 2) != 0:
            with open(write_csv_file(directory_path, 'transactions'), 'a', newline='') as fp:
                write_csv = csv.writer(fp)
                write_csv.writerow([datetime.datetime.now(tz).strftime('%Y-%m-%d'),
                                    item,
                                    round_up((current_positions[item]['shares'] - trade_decisions[item]) *
                                             prices[item][-1], 2),
                                    round_up(trade_decisions[item] * prices[item][-1], 2),
                                    current_positions[item]['value']])
            if current_positions[item]['shares'] == 0.0:
                del current_positions[item]


def fetch_stock_data():
    global stock_tickers
    # Calculate yesterday's date
    end_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    stock_prices = {}
    stock_returns = {}
    for ticker in tqdm(stock_tickers, desc='Fetch Data'):
        # noinspection PyBroadException
        try:
            # Adjust the date range as needed
            temp_data = yf.download(ticker, start='2023-07-01', end=end_date, progress=False)
            stock_prices[ticker] = temp_data['Adj Close'].tolist()
            stock_returns[ticker] = temp_data['Adj Close'].pct_change().dropna().tolist()
        except:     # Catch any exception that might happen
            pass
    return {'stock_prices': stock_prices, 'stock_returns': stock_returns}


def find_missing_stocks(prices, returns):
    temp_missing_stocks = {}
    for item in prices:
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
            temp_missing_stocks[item] = {'prices': prices[item], 'returns': returns[item]}
    return temp_missing_stocks


def generate_csv_filename(prefix):
    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y%m%d%H%M')
    filename = f'{prefix}_{formatted_date}.csv'
    return filename


def get_most_recent_csv_file(directory, prefix):
    prefix_directory = path.join(directory, prefix)

    # Check if the prefix directory exists
    if path.exists(prefix_directory) and path.isdir(prefix_directory):
        # List all files in the prefix directory
        prefix_files = [file for file in listdir(prefix_directory) if file.endswith('.csv')]
        # Get the most recent CSV file based on file modification time
        if prefix_files:
            prefix_files = [path.join(prefix_directory, file) for file in prefix_files]
            prefix_files.sort(key=lambda x: path.getmtime(x), reverse=True)
            most_recent_csv = prefix_files[0]
            return most_recent_csv
    return None  # No files found with the specified prefix or directory does not exist


# Function to get the most recent file for each prefix
def get_most_recent_files_for_prefixes(directory, prefixes):
    most_recent_files = {}
    for prefix in prefixes:
        most_recent_files[prefix] = get_most_recent_csv_file(directory, prefix)
    return most_recent_files


def get_time_until_next_run():
    now = datetime.datetime.now()
    next_run_time = datetime.datetime(now.year, now.month, now.day, 11, 0)  # Next run at 11:00
    if now > next_run_time:
        next_run_time += datetime.timedelta(days=1)  # If it's already past 12:00 today, schedule for tomorrow
    time_until_run = next_run_time - now
    return time_until_run


def is_market_open():
    now = datetime.datetime.now(tz)
    open_time = datetime.time(hour=9, minute=30, second=0)
    close_time = datetime.time(hour=16, minute=0, second=0)
    # If a holiday
    if now.strftime('%Y-%m-%d') in us_holidays:
        return False
    # If it's before 0930 or after 1600
    elif (now.time() < open_time) or (now.time() > close_time):
        return False
    # If it's a weekend
    elif now.date().weekday() > 4:
        return False
    else:
        return True


def optimal_weights(returns):
    expected_returns = {}
    # Calculate expected returns and risks
    for item in list_of_stocks:
        expected_returns[item.ticker] = sum(item.returns) / len(item.returns)
    covariance_matrix = []
    for ticker_i in stock_tickers:
        cov_row = []
        for ticker_j in stock_tickers:
            cov_sum = 0
            for ret_i, ret_j in zip(returns[ticker_i], returns[ticker_j]):
                cov_sum += (ret_i - expected_returns[ticker_i]) * (ret_j - expected_returns[ticker_j])
            cov_row.append(cov_sum / (len(returns[ticker_i]) - 1))
        covariance_matrix.append(cov_row)

    # Generate random portfolios
    num_portfolios = 1000000
    weights = np.random.random(size=(num_portfolios, len(expected_returns)))
    weights /= np.sum(weights, axis=1)[:, np.newaxis]

    # Optimal portfolio
    def objective(proportions):
        weighted_returns = 0
        for item_weight, expected_return in zip(proportions, expected_returns.values()):
            weighted_returns += item_weight * expected_return

        # noinspection PyTypeChecker
        covariance_term = np.dot(proportions, np.dot(covariance_matrix, proportions))
        return -weighted_returns / np.sqrt(covariance_term)

    constraints = ({'type': 'eq', 'fun': lambda weight_amounts: sum(weight_amounts) - 1})
    bounds_list = []
    for asset in range(len(expected_returns)):
        bounds_list.append((0, 1))
    bounds = tuple(bounds_list)

    initial_weights = np.ones(len(expected_returns)) / len(expected_returns)

    optimal_portfolio = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

    # Extract optimal weights
    temp_optimal_weights = optimal_portfolio.x

    # Store optimal weights in a dictionary
    optimal_weights_dict = {}
    for symbol, weight in zip(returns.keys(), temp_optimal_weights):
        optimal_weights_dict[symbol] = weight

    return optimal_weights_dict


def round_up(number, decimal_places):
    temp_number = number * (10 ** decimal_places)
    adjusted_number = temp_number + 0.5
    rounded_number = round(adjusted_number) / (10 ** decimal_places)
    return rounded_number


def update_current_positions():
    with open(write_csv_file(directory_path, 'current_positions'), 'w', newline='') as fp:
        write_csv = csv.writer(fp)
        write_csv.writerow(['Item', 'Shares', 'Value ($)'])
        for key in current_positions:
            write_csv.writerow([key, current_positions[key]['shares'], current_positions[key]['value']])


def update_stock_values(prices, returns):
    global list_of_stocks
    global current_positions
    for item in list_of_stocks:
        if item.ticker not in prices:
            print(item.ticker + ' is not found')
        else:
            item.prices = prices[item.ticker]
            item.returns = returns[item.ticker]
            if item.ticker in current_positions:
                current_positions[item.ticker]['value'] = round_up(float(current_positions[item.ticker]['shares']) *
                                                                   prices[item.ticker][-1], 2)


def write_csv_file(directory, prefix):
    create_directory(directory, prefix)
    filename = generate_csv_filename(prefix)
    file_path = path.join(directory, prefix, filename)
    return file_path


# This is the part that runs once every day
schedule.every().day.at('11:00').do(daily_steps)

# This loops every second during the remainder of the day
while True:
    print('\n' * 100)
    # Checks whether a scheduled task is pending to run or not
    time_until_next_run = get_time_until_next_run()
    time_until_next_run_formatted = str(time_until_next_run).split('.')[0]  # Extracting hours, minutes, and seconds
    print(f'Time until next run: {time_until_next_run_formatted}')
    schedule.run_pending()
    time.sleep(1)
