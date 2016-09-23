from Asset import Asset

class Portfolio:
    def __init__(self, stock_market, pairs, start_stock_capital):
        self.stock_market = stock_market

        self.asset_pairs = {}
        for pair in pairs:
            asset0 = self.acquire_asset(pair[0], start_stock_capital)
            asset1 = self.acquire_asset(pair[1], start_stock_capital)
            self.asset_pairs[pair] = (asset0, asset1)

        self.trading_pairs = set()

    def acquire_asset(self, stock, capital):
        stock_value = self.stock_market.stock_value(stock)
        num_stocks = int(capital / stock_value)
        return Asset(self.stock_market, stock, num_stocks)

    def value(self):
        total = 0
        for key, val in self.asset_pairs.items():
            total = total + val[0].value() + val[1].value()
        return total
