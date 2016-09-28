from math import floor, ceil
from StockMarket import StockMarket
from Portfolio import Portfolio
import pandas as pd
from datetime import date, datetime
import PairTrading

def get_history_from_date(history, period):
	return history.tail(period)
	

def back_test(history, pair_trader, start_balance):
    ratio = 2.0 / 3
    training_data = history.head(floor(len(history) * ratio))
    test_data = history.tail(ceil(len(history) * (1 - ratio)))
    
    # Pairs bliver pt. lavet på baggrund af training_data. Vi skal have lavet en rigtig pair inddeling.
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
    
    # 2. Backtesting ved at rulle igennem den ønskede test periode.
    
    start_period = date(2015, 10, 1)
    end_period = date(2016, 1, 1)
    
    # 2.1 Denne funktion trækker den daglige pris for hver dag i history variablen og gemmes som daily_price.
    pairs = pair_trader.pairs
    active_pairs = pd.Series(False, index=[pairs])
    longs = []
    shorts = []
    month = ''
    period = 10
    
    # 2.1.1 Dette loop kører hver enkelte dato igennem.
    for d in StockMarket.daterolling(start_period, end_period):
    	monthly_call = d.month
    	d = d.strftime('%Y%m%d')
    	if any(history.index == d):
    		# Gem daglig pris og historik periode
    		daily_price = history.loc[d]
    		history_period = get_history_from_date(history, period)
    		
    		# 2.1.2 Nedenstående if bliver kun kaldt hver måned.
    		if month == '' or month != monthly_call:
    			month = monthly_call
    			
    			# 2.1.3 Finder nu pairs for hver måned
    			pairs = PairTrading.compute_pairs(history_period)
    			print('Monthly Pairs')
    			print(pairs)
    			
    		# 2.1.2 Slut
    		
    		# 2.2 Her handler vi de pairs vi har i pair_trader.pairs
    		for pair in pair_trader.pairs:
    			# Antager her alle pairs skal handles.
    			if active_pairs.loc[pair] == False:
    				active_pairs.loc[pair] = True
    				for stock in pair:
    					if stock == pair[0]:
    						longs.append([stock, d])
    					else:
    						shorts.append([stock, d])
    
    print('Longs:')
    print(longs)
    print('Shorts')
    print(shorts)
    
    # 3. Check profits. Hvis handler stadig er åbne, medregnes disse som var de lukket i dag.
    # Tjekker først profits i longs.
    profit = 0
    for trades in longs:
    	price = history.loc[trades[1]][trades[0]]
    	close = history[trades[0]].iloc[-1]
    	print(close - price)
    	profit = profit + close - price
    
    for trades in shorts:
    	price = history.loc[trades[1]][trades[0]]
    	close = history[trades[0]].iloc[-1]
    	print(price - close)
    	profit = profit + price - close
    	
    print('Profits:')
    print(profit)
    
    stock_market = StockMarket(test_data)
    portfolio = Portfolio(stock_market, pair_trader.pairs, start_balance)

    while stock_market.end_day():
        print(stock_market.current_date() + ": $" + str(portfolio.value()))

    # print(training_data)
    # print(len(history))
    # print(len(training_data))
    # print(len(test_data))