
#def solver(input):
#	pass

def stock(input):
	stock_price = {}
	stock_num   = {}
	todo = []
	for data in input: 
		data = data.split("|")
		if len(data) == 2:
			DAY,PRICE = int(data[0]),int(data[1])
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
	ans = []
	ans1 = []
	keys = stock_num.keys()
	values = stock_num.values()
	for i in range(len(todo)):
		if todo[i] == "BUY" :
			DAY,TRADER = keys[i][0],keys[i][1]
			AMOUNT = stock_num[(DAY,TRADER)]
			if changein3ri(DAY,stock_price,AMOUNT,1):
				ans.append((DAY,TRADER)) 
		elif todo[i] == "SELL"  :
			DAY,TRADER = keys[i][0],keys[i][1]
			AMOUNT = stock_num[(DAY,TRADER)]
			if changein3ri(DAY,stock_price,AMOUNT,-1):
				ans.append((DAY,TRADER))
		else:
		 	print("error in SELL and BUY, DSV format is broken")
		 	return		 
	ans.sort(key=lambda tup: tup[0])
	for x in ans:
		k = str(x[0]) + "|"+ str(x[1])
		ans1.append(k)
	return ans1		
	
def changein3ri(day,stock_price,amount,trade_type):
	fm = 5000000
	init_PRICE = stock_price[day]
	for x in range(day+1,day+4):
		if x in stock_price.keys():
			PRICE = stock_price[x]
		else:
			continue 	
		print(PRICE,"this i",day,(PRICE - init_PRICE),amount)
		if trade_type*(PRICE - init_PRICE)*amount >= fm:
			return True
	return False		


def driver():
	import sys
	arg = sys.stdin.readlines()
	for rec in stock(arg):
		print(rec)
driver()














