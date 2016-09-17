from StockMarket import StockMarket

stocks_path = "../data/WIKI_subset.csv"

sm = StockMarket(stocks_path)
sh = sm.history("2015-06-01","2016-01-01")
clean_sh = sm.clean_history(sh)
print(clean_sh.corr())
#print(clean_sh)
# Check correlation
#sc = sm.correlation(clean_sh)
#print(sc)