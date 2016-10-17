
#def solver(input):
#	pass
def stock(input):
	stock_price = {}
	stock_num   = {}
	todo = []
	#collect data
	for data in input: 
		data = data.split("|")
		#length 2 means stock, length 4 means trade
		if len(data) == 2:
			DAY,PRICE = int(data[0]), int(data[1])
			stock_price[DAY] = PRICE
		elif len(data) == 4:
			DAY,TRADER,TRADE_TYPE,AMOUNT = int(data[0]),data[1],data[2],int(data[3])
			if TRADER not in stock_num:
				stock_num[(DAY,TRADER)] = AMOUNT
			else:
				stock_num[(DAY,TRADER)] = stock_num[TRADER]+ AMOUNT	
			todo.append(TRADE_TYPE)
		else:
			print("error, DSV format is broken")
			return
	# find traget trader insert into result list
	#print(stock_price)        
	ans = []
	ans1 = []
	keys = stock_num.keys()
	#print(keys)
	values = stock_num.values()
	#print(values)
	for i in range(len(todo)):
		if todo[i] == "BUY" :
			#print(keys[i][0])
			DAY,TRADER = keys[i][0],keys[i][1]
			AMOUNT = stock_num[(DAY,TRADER)]
			if Change_3_Day(DAY,stock_price,AMOUNT,1):
				ans.append((DAY,TRADER)) 
		elif todo[i] == "SELL" :
			DAY,TRADER = keys[i][0],keys[i][1]
			AMOUNT = stock_num[(DAY,TRADER)]
			if Change_3_Day(DAY,stock_price,AMOUNT,-1):
				ans.append((DAY,TRADER))
		else:
		 	print("error in SELL and BUY, DSV format is broken")
		 	return

	#sort by date then by name
	ans.sort(key=lambda tup: tup[0])
	#ans = {(day,trade),(day2,trade2)}
	for x in ans:
		k = str(x[0]) + "|"+ str(x[1])
		ans1.append(k)
	return ans1		
	
# increase after sell , decrase after buy
def Change_3_Day(day,stock_price,amount,trade_type):
	fm = 5000000
	# Some day might not inside if the stock price does not change
	keys = stock_price.keys()
	sortedkey = sorted(keys)
	#goal: update init_PRICE when it is the same as previous
	if day not in sortedkey: #[2,3,4,7,12]  8 would be day
		for i in range(len(sortedkey)):
			# find largest number smaller than x
			if( day < keys[i]):
				init_PRICE = stock_price[keys[i-1]] 
	else:	
		init_PRICE = stock_price[day]

	for x in range(day+1,day+4):
		#print("day",x)
		if x in stock_price:
			PRICE = stock_price[x]
		else:
			continue 	
		if trade_type*(PRICE - init_PRICE)*amount >= fm:
			return True
	return False		


def driver():
	import sys
	arg = sys.stdin.readlines()
	#read all lines 
	#turn into a list 
	#like line1 line2 line3
	for rec in stock(arg):
		print(rec)

driver()














