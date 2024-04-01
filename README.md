<!-- TOC -->
* [Thesis Project Andrew Amazeen](#thesis-project-andrew-amazeen)
  * [Install required libraries](#install-required-libraries)
  * [To run the program](#to-run-the-program)
  * [Functionality](#functionality)
    * [Daily Schedule](#daily-schedule)
  * [Data files](#data-files)
    * [current_positions_YYYYMMDDHHMM.csv](#currentpositionsyyyymmddhhmmcsv)
    * [transactions_YYYYMMDDHHMM.csv](#transactionsyyyymmddhhmmcsv)
  * [Class](#class)
    * [Stock Class](#stock-class)
      * [Variables](#variables)
      * [Properties](#properties)
      * [Methods](#methods)
<!-- TOC -->

# Thesis Project Andrew Amazeen

Users are people looking to create a stock portfolio but
want the process to be automated. The project runs once
per day around noon and cycles through all the instructions
for the day, buying and selling stocks to readjust the
portfolio. CSV files will store a list of current stock
positions as well as a list of all transactions.

## Install required libraries
Ensure that you are in the main directory and
run the following:

_This must be done before you can run the application._

```shell
$ pip install -r requirements.txt
```
or
```shell
$ pip install --upgrade pip
$ pip install holidays
$ pip install numpy
$ pip install pytz
$ pip install Schedule
$ pip install scipy
$ pip install tqdm
$ pip install yfinance
```
Note: You need to import those packages in your
Python file.

## To run the program
Click the green triangle run icon in the
top-right corner of the PyCharm window.

or
```shell
$ python main.py
```

## Functionality
### Daily Schedule
The program's logic executes once per day, regardless of
whether the stock market is open. Once the code starts
running, a countdown will appear, dictating how much time
remains until the next execution.

At the predetermined time of execution each day, the
program first determines whether the stock market is open
(excluding holidays, weekends, and times outside of
trading hours). If it passes each of these tests, then
the main logic will begin executing. If it does not, the
program continues to count down until the following day's
execution.

The program will then go through the steps of downloading
all Adjusted Closing Prices for the predetermined ticker
symbols since 07/01/2023, separating out prices and daily
returns, updating the values of currently owned stocks,
running the Efficient Frontier formula, buying and selling
stocks, and finally outputting .csv files showing your
current positions and a list of all transactions.

The outputs are stored in appropriately-named folders,
showing different versions for each new day (e.g.,
current_positions202403141502 in the YYYYMMDDHHMM format).
The most recent .csv files must remain in these folders,
as this is how the program reminds itself of past
variables in case the execution was interrupted.

## Data files
### current_positions_YYYYMMDDHHMM.csv
The file contains data on stocks currently in your
portfolio, in alphabetical order with Cash at the
beginning, in the following format:

| Item | Shares  | Value ($) |
|------|---------|-----------|
| Cash | 0       | 9.82      |
| A    | 0.0002  | 0.03      |
| ABBV | 41.5133 | 7510.59   |
| AKAM | 6.8164  | 748.31    |
| CBOE | 80.2936 | 14589.35  |

### transactions_YYYYMMDDHHMM.csv
The file contains the transaction data sorted in order of
transactions date, the alphabetized by ticker symbol, in
the following format:

| Date    | Ticker | Old Balance | Transaction Amount | New Balance |
|---------|--------|-------------|--------------------|-------------|
| 3/14/24 | A      | 0           | 0.03               | 0.03        |
| 3/14/24 | ABBV   | 0           | 7510.59            | 7510.59     |
| 3/14/24 | AKAM   | 0           | 748.31             | 748.31      |
| 3/14/24 | CBOE   | 0           | 14589.35           | 14589.35    |

## Class

### Stock Class

#### Variables
Each Stock Class instance has the following instance
variables:
- ticker: private, String data type
- prices: private, list of float data type
- returns: private, list of float data type

#### Properties
Each Major Class instance has the following
properties:
- ticker getter
- ticker setter
- prices getter
- prices setter
- returns getter
- returns setter

#### Methods
The Stock Class has the following methods:
- The dunder__init__(self, ticker, prices, returns) method