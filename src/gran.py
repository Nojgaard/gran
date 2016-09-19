from StockMarket import StockMarket
import PairTrading
import Database

# stocks_path = "data/WIKI_subset.csv"

stocks = Database.get_stocks("crude oil")
for stock in stocks:
    print(stock)



# sm = StockMarket(stocks_path)
print()
sh = Database.get_history(stocks, "2015-06-01","2016-01-01")
print(sh)
# print(sh.corr())

#print(sh)
#print(PairTrading.example())

# print(PairTrading.compute_pairs(sh))

# clean_sh = sm.clean_history(sh)
# print(clean_sh.corr())
#print(clean_sh)
# Check correlation
#sc = sm.correlation(clean_sh)
#print(sc)
