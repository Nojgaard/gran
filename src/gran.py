from StockMarket import StockMarket
import PairTrading
from datetime import date

stocks_path = "data/WIKI_subset.csv"

sm = StockMarket(stocks_path)
#sh = sm.history("2015-06-01","2016-01-01")
# print(sh.corr())
#print(sh)
#print(PairTrading.example())

#print(PairTrading.compute_pairs(sh))
start_date = date(2015, 5, 1)
end_date = date(2015, 6, 2)
#print(StockMarket.daterange(start_date, end_date))
print(StockMarket.trade(sm, start_date, end_date))

# clean_sh = sm.clean_history(sh)
# print(clean_sh.corr())
#print(clean_sh)
# Check correlation
#sc = sm.correlation(clean_sh)
#print(sc)
