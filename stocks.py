# TODO: change this to use variables needed for algorithms
class Stock:
    def __init__(self, ticker, prices, returns):
        self.ticker = ticker
        self.prices = prices
        self.returns = returns
        # self.open_price = open_price
        # self.current_price = current_price
        # self.year_high = year_high
        # self.year_low = year_low
        # self.company_name = company_name

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        self._ticker = ticker

    @property
    def prices(self):
        return self._prices

    @prices.setter
    def prices(self, prices):
        self._prices = prices

    @property
    def returns(self):
        return self._returns

    @returns.setter
    def returns(self, returns):
        self._returns = returns

    # @property
    # def open_price(self):
    #     return self._open_price
    #
    # @open_price.setter
    # def open_price(self, open_price):
    #     self._open_price = open_price
    #
    # @property
    # def current_price(self):
    #     return self._current_price
    #
    # @current_price.setter
    # def current_price(self, current_price):
    #     self._current_price = current_price
    #
    # @property
    # def year_high(self):
    #     return self._year_high
    #
    # @year_high.setter
    # def year_high(self, year_high):
    #     self._year_high = year_high
    #
    # @property
    # def year_low(self):
    #     return self._year_low
    #
    # @year_low.setter
    # def year_low(self, year_low):
    #     self._year_low = year_low
    #
    # @property
    # def company_name(self):
    #     return self._company_name
    #
    # @company_name.setter
    # def company_name(self, company_name):
    #     self._company_name = company_name

# TODO: maybe add a __str__ method?
