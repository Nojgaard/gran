class Asset:
    def __init__(self, stock_market, stock, num_stocks):
        self.stock_market = stock_market
        self.stock = stock
        self.num_stocks = num_stocks

    def value(self):
        return self.num_stocks * self.stock_market.stock_value(self.stock)
