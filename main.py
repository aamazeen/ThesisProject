# various imports - add whichever others are needed
from time import *
from stocks import *
from os import path
import csv
import schedule

# various declarations
marketOpen = False	# beginning value of False to be tested daily
listOfStocks = []	# list of Stock objects containing information on every stock that will be tested
listOfMarketClosures = []	# list of dates when the market is closed
currentPositions = {'Cash' : 100000}    # starting amount of $100,000, adding tickers when purchased

# define methods
def create_stock_objects(missingStocks):
    if len(missingStocks) > 0:
        for item in missingStocks:
            # TODO: pull the correct info from tempStockData for __init__ function
            tempStock = Stock(ticker, openPrice, currentPrice, yearHigh, yearLow, companyName)
            listOfStocks.append(tempStock)

def daily_steps():	# we will cycle through this one every day, and this will call other methods as needed along the path
    marketOpen = is_market_open()	# changes value to True if the stock market is open that day
    tempSellDecisions = {}	# used to store temporary ticker:shares pairs to execute trades later
    tempBuyDecisions = {}	# used to store temporary ticker:shares pairs to execute trades later

    if marketOpen:
        tempStockData = fetch_stock_data()
        missingStocks = find_missing_stocks(tempStockData)
        create_stock_objects(missingStocks)
        update_stock_values(listOfStocks)
        if len(currentPositions) > 1:   # 'cash' will always be there, so checking if there is anything else
            tempSellDecisions = to_sell_or_not_to_sell(tempStockData, currentPositions)
            if len(tempSellDecisions) > 0:
                execute_orders(tempStockData, tempSellDecisions, currentPositions)
        if currentPositions['Cash'] > 0:
            tempBuyDecisions = to_buy_or_not_to_buy(tempStockData, currentPositions)
            if len(tempBuyDecisions) > 0:
                execute_orders(tempStockData, tempBuyDecisions, currentPositions)
        with open('currentpositions.csv', 'w', newline='') as fp:
            write_csv = csv.writer(fp)
            write_csv.writerow(['Item', 'Shares', 'Value ($)'])
            for key in currentPositions:
                if key == 'Cash':
                    write_csv.writerow(['Cash', 0, currentPositions['Cash']])
                else:
                    # TODO: pull the correct price from tempStockData
                    write_csv.writerow([key, currentPositions[key], currentPositions[key] * tempStockData[key]['price']])

    marketOpen = False

def execute_orders(tempStockData, tradeDecisions, currentPositions):
    for item in tradeDecisions:
        add or subtract the number of shares from currentPositions
        add or subtract the amount of cash from currentPositions
        if the new number of shares is now zero:
            remove the ticker from currentPositions
        if there is no .csv file to store transactions:
            create .csv file to store transactions
        append transactions to .csv file with trade info

def fetch_stock_data():
    access the internet and pull a list of all available ticker symbols, storing in stockTickers list
    for item in stockTickers:
        access the internet and pull a dictionary with stock info, storing in stockData dictionary
        stockData dictionary should have the ticker as the key, and other info in same order
    ALTERNATIVELY scrape the webpage and combine the above two into one step
    return stockData

def find_missing_stocks(tempStockData):
    tempMissingStocks = {}
    for item in tempStockData:
        stockFound = False		# changes value to True if the match is found
        for stock in listOfStocks:
            if item == stock.ticker():
                stockFound = True
                break
            else:
                continue
        if stockFound:
            continue
        else:
            tempMissingStocks[item] = tempStockData[item]
    return tempMissingStocks

def is_market_open():
    if today’s date is a weekend or among list of holidays using listOfMarketClosures:
        return False
    else:
        return True

def to_buy_or_not_to_buy(tempStockData, currentPositions):
    tempDecisions = {}
    for item in tempStockData:
        perform tests to see if an amount should be bought/how much
        if shares should be bought and we have sufficient cash:
            add ticker:shares(+) pair to tempDecisions
        else:
            continue
    return tempDecisions

def to_sell_or_not_to_sell(tempStockData, currentPositions):
    tempDecisions = {}
    for item in currentPositions:
        if item is cash:
            continue
        else:
            perform tests to see if an amount should be sold/how much
            if shares should be sold and we have sufficient shares:
                add ticker:shares(-) pair to tempDecisions
            else:
                continue
    return tempDecisions

def update_stock_values(listOfStocks):
    for Stock object in listOfStocks:
        update Stock object with current values


schedule.every().day.at("12:00").do(daily_steps)

while True:
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
