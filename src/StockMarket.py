import quandl
from Stock import Stock
import pandas as pd
from datetime import timedelta

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

    def history(self, start, end):
        req_stocks = [x.code() + ".4" for x in self.stocks()]
        data = quandl.get(req_stocks, start_date=start, end_date=end)
        data = data.dropna(axis = 1)
        return data
        
    def daterolling(start, end):
        for n in range(int((end - start).days)):
            single_date = start + timedelta(n)
            
            #print(single_date.strftime("%Y-%m-%d"))
            yield single_date
    
    def trade(stocks, start, end):
        trading_stocks = [x.code() + ".4" for x in self.stocks()]
        for single_date in (StockMarket.daterolling(start, end)):      
            prices = quandl.get(trading_stocks, start_date=single_date, end_date=single_date)
            print(prices)