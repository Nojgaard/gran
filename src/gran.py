# from StockMarket import StockMarket
import PairTrading
from PairTrader import PairTrader
import Database
from BackTest import back_test
from datetime import date

balance = 10000



# stocks_path = "data/WIKI_subset.csv"

stocks = Database.get_stocks("tele communication")
for stock in stocks:
    print(stock)



# sm = StockMarket(stocks_path)
#print()
sh = Database.get_history(stocks, "2015-06-01","2016-01-01")
#print(sh)
print()
sh = Database.get_history(stocks, "2015-10-01","2016-01-01")
pair_trader = PairTrader()
print(pair_trader)





back_test(sh, pair_trader, balance)
# print(sh)
# sm = StockMarket(stocks_path)
#sh = sm.history("2015-06-01","2016-01-01")
#print(sh.corr())
#print(sh)
#print(PairTrading.example())

'''sm = StockMarket()
start_date = date(2015, 5, 20)
end_date = date(2015, 6, 2)
pairs = compute_pairs(stocks)
#print(StockMarket.daterange(start_date, end_date))
print(sm.trade(stocks, start_date, end_date))
# clean_sh = sm.clean_history(sh)
# print(clean_sh.corr())
#print(clean_sh)
# Check correlation
#sc = sm.correlation(clean_sh)
#print(sc)'''
