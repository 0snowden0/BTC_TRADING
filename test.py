#importing different modules
import ccxt
from datetime import datetime,date
import time

def trade():
	#getting today's date
	today = date.today()

	#choosing binance as my exchange in ccxt
	binance = ccxt.binance()

	#taking the close value of the previous day
	btc_usdt_ohlcv = binance.fetch_ohlcv('BTC/USDT','1d', limit = 2)
	yesterday_close = btc_usdt_ohlcv[0][4]

	#making the conditions accurate to meet the buying scenario
	required_cp = 0.005*yesterday_close + yesterday_close
	buy_flag = False

	#A while loop the runs every five 5 throughout the day
	while True:
		#if the day changes, exit the loop
		now = date.today()
		if now != today:
			break
	
		#fetching the close price of BTC in the recent 5 minute time frame
		current = binance.fetch_ohlcv('BTC/USDT','5m', limit = 2)
		current_close = current[1][4]
		
		#exiting from the loop if the required conditions from buying are met
		if current_close >= required_cp:
			buy_flag = True
			break
			
		time.sleep(300)
		
	#if we have bought BTC then we will proceed with the selling scenario	
	if buy_flag is True:
		#getting the quantity of BTC to be bought as a user input and thus calculation the 	cp
		quantity = input("Your Buying conditions are ripe, Enter the BTC to buy : ")
		quantity = float(quantity)
		cp = current_close*quantity
		
		#getting the selling conditions from the cp calculated
		required_sp = 0.002*cp+cp
		sell_flag = False
		
		#another while loop that runs every 5 minutes
		while True:
			#breakout from the loop if the date changes
			now = date.today()
			if now != today:
				break
		
			#getting the close value of BTC in the recent 5 minute timeframe
			current = binance.fetch_ohlcv('BTC/USDT','5m', limit = 2)
			current_close = current[1][4]
			
		
			#checking if the requirred conditions for selling are met
			if current_close >= required_sp:
				sell_flag = True
				break
				
			time.sleep(300)
			
		#if we did sell the BTC bought, then we can calculate the profit	
		if sell_flag is True:
			#Calculating our selling price by selling the same quantity of BTC that we 	bought
			sp = current_close*quantity
			print('your profit for the day is: ', sp-cp)
			
		else:
			print('The price did not match the selling conditions today, you currently have ',cp,' worth of BTC with you from the day')
			
	else:
		print("your buying conditions did not match for the day. Let's give it a shot tomorrow")
		
if __name__ == '__main__':
	trade()
