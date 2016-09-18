import quandl
from Stock import Stock
import pandas as pd

# quandl api authentication
quandl.ApiConfig.api_key = '-b2fk-v3un2si3_FB18U'

class StockMarket:
    def __init__(self, stocks_path):
        self.m_stocks = []
        sf = open(stocks_path, 'r')
        for line in sf:
            attrs = line.split(",")
            self.m_stocks.append(Stock(attrs[1].strip(), attrs[0].strip()))

    def stocks(self):
        return self.m_stocks

    def history(self,start,end):
        req_stocks = [x.code() + ".4" for x in self.stocks()]
        data = quandl.get(req_stocks, start_date=start, end_date=end)
        data = data.dropna(axis = 1)
        return data
