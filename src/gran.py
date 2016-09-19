from StockMarket import StockMarket
import PairTrading
import Database
from datetime import date

# stocks_path = "data/WIKI_subset.csv"

stocks = Database.get_stocks("crude oil")
for stock in stocks:
    print(stock)



# sm = StockMarket(stocks_path)
print()
sh = Database.get_history(stocks, "2015-06-01","2016-01-01")
print(sh)
# sm = StockMarket(stocks_path)
#sh = sm.history("2015-06-01","2016-01-01")
# print(sh.corr())
#print(sh)
#print(PairTrading.example())

start_date = date(2015, 5, 20)
end_date = date(2015, 6, 2)
#print(StockMarket.daterange(start_date, end_date))
# print(sm.trade(start_date, end_date))
# clean_sh = sm.clean_history(sh)
# print(clean_sh.corr())
#print(clean_sh)
# Check correlation
#sc = sm.correlation(clean_sh)
#print(sc)
