requests = ['mushrooms','onions','pineapple']

order = 'cheese'

if 'mushrooms' in requests:
	print(True)

if 'pepperoni' in requests:
	print(True)
else:
	print(False)



if order not in requests:
	print("We dont have that.")
else:
	print("we are preparing for you.")





