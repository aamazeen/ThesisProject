class Stock:
    def __init__(self, ticker, openPrice, currentPrice, yearHigh, yearLow, companyName):
        self.ticker = ticker
        self.openPrice = openPrice
        self.currentPrice = currentPrice
        self.yearHigh = yearHigh
        self.yearLow = yearLow
        self.companyName = companyName

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        self._ticker = ticker

    @property
    def openPrice(self):
        return self._openPrice

    @openPrice.setter
    def openPrice(self, openPrice):
        self._openPrice = openPrice

    @property
    def currentPrice(self):
        return self._currentPrice

    @currentPrice.setter
    def currentPrice(self, currentPrice):
        self._currentPrice = currentPrice

    @property
    def yearHigh(self):
        return self._yearHigh

    @yearHigh.setter
    def yearHigh(self, yearHigh):
        self._yearHigh = yearHigh

    @property
    def yearLow(self):
        return self._yearLow

    @yearLow.setter
    def yearLow(self, yearLow):
        self._yearLow = yearLow

    @property
    def companyName(self):
        return self._companyName

    @companyName.setter
    def companyName(self, companyName):
        self._companyName = companyName
