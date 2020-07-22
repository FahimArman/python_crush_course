def make_pizza(size, *toppings):
	print("Make a - " + str(size) +" - size pizza. With the following toppings : \n")
	for topping in toppings:
		print("-->" + topping)

make_pizza(12,'pepperoni')
make_pizza(16,'mushrooms', 'green peppers', 'extra cheese')

