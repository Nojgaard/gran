from math import floor, ceil
from StockMarket import StockMarket
from Portfolio import Portfolio
import pandas as pd

def back_test(history, pair_trader, start_balance):
    ratio = 2.0 / 3
    training_data = history.head(floor(len(history) * ratio))
    test_data = history.tail(ceil(len(history) * (1 - ratio)))
    
    pair_trader.learn_pairs(training_data)
    print("PAIRS:")
    print(pair_trader.pairs)
    print()
    
    # 1. Snippets herunder forsøger at give handelssignaler
    # 1.1 Finder spread af trading pairs
    assets_to_trade = pd.DataFrame([])
    for pairs in pair_trader.pairs:
    	for stock in pairs:
    		assets_to_trade = pd.concat([assets_to_trade, history[[stock]]], axis = 1)
    assets_history1 = assets_to_trade[assets_to_trade.columns[::2]]
    assets_history2 = assets_to_trade[assets_to_trade.columns[1::2]]
    pair_spread = pd.DataFrame(assets_history1.values-assets_history2.values, columns=assets_history1.columns)
    print('Pair spread')
    print(pair_spread)
    
    # 1.2 Finder middelværdi af spread
    pair_mean = pair_spread.mean(axis = 0)
    print('Pair middelværdi')
    print(pair_mean)
    
    # 1.3 Finder std. afvigelse
    pair_std = pair_spread.std(axis = 0)
    print('Pair std. afvigelse')
    print(pair_std)
    
    # 1.4 Finder z-score - Er zscore højere end 3 eller lavere end -3, så skal handel eksekveres for det givne pair.
    todays_spread = 100 # Denne variabel skal have dagens spread
    pair_zscore = (todays_spread - pair_mean) / pair_std
    print('Pair zscore')
    print(pair_zscore)
    
    stock_market = StockMarket(test_data)
    portfolio = Portfolio(stock_market, pair_trader.pairs, start_balance)

    while stock_market.end_day():
        print(stock_market.current_date() + ": $" + str(portfolio.value()))

    # print(training_data)
    # print(len(history))
    # print(len(training_data))
    # print(len(test_data))