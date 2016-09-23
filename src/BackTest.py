from math import floor, ceil
from StockMarket import StockMarket
from Portfolio import Portfolio

def back_test(history, pair_trader):
    ratio = 2.0 / 3
    training_data = history.head(floor(len(history) * ratio))
    test_data = history.tail(ceil(len(history) * (1 - ratio)))

    pair_trader.learn_pairs(training_data)
    print("PAIRS:")
    print(pair_trader.pairs)
    print()

    stock_market = StockMarket(test_data)
    portfolio = Portfolio(stock_market, pair_trader.pairs, 1000)

    while stock_market.end_day():
        print(stock_market.current_date() + ": $" + str(portfolio.value()))



    # print(training_data)
    # print(len(history))
    # print(len(training_data))
    # print(len(test_data))
