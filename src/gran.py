from StockMarket import StockMarket

stocks_path = "../data/WIKI_subset.csv"

sm = StockMarket(stocks_path)

print(sm.history())
