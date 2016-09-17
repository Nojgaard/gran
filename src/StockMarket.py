import quandl
from Stock import Stock

class StockMarket:
    def __init__(self, stocks_path):
        self.m_stocks = []
        sf = open(stocks_path, 'r')
        for line in sf:
            attrs = line.split(",")
            self.m_stocks.append(Stock(attrs[1].strip(), attrs[0].strip()))

    def stocks(self):
        return self.m_stocks

    def history(self):
        req_stocks = [x.code() + ".4" for x in self.stocks()]
        data = quandl.get(req_stocks, start_date="2015-06-01", end_date="2016-01-01")
        return data

