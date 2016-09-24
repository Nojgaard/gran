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

    def history(self, start, end):
        req_stocks = [x.code() + ".4" for x in self.stocks()]
        data = quandl.get(req_stocks, start_date=start, end_date=end)
        data = data.dropna(axis = 1)
        return data
        
    '''def daterolling(start, end):
        for n in range(int((end - start).days)):
            single_date = start + timedelta(n)
            
            #print(single_date.strftime("%Y-%m-%d"))
            yield single_date'''
    
    def trade(self, securities, start, end):
        trading_stocks = [x.code() + ".4" for x in self.stocks()]
        prices = quandl.get(trading_stocks, start_date=start, end_date=end)
        for i in range(0, len(prices)):
            print(prices.iloc[i])

    def end_day(self):
        self.day = self.day + 1
        return self.day < len(self.history)
