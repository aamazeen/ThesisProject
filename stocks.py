# TODO: change this to use variables needed for algorithms
class Stock:
    def __init__(self, ticker, prices, returns):
        self.ticker = ticker
        self.prices = prices
        self.returns = returns

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
