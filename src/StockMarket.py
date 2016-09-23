class StockMarket:
    def __init__(self, history):
        self.history = history
        self.day = 0

    def stocks(self):
        return self.history.columns

    def stock_value(self, stock):
         return float(self.history[stock][self.day])

    def current_date(self):
         return self.history.index[self.day].strftime("%Y-%m-%d")

    def end_day(self):
        self.day = self.day + 1
        return self.day < len(self.history)
