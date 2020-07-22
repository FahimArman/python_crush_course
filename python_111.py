pizza = {
	'crust': 'thick',
	'topping': ['mushrooms','extra cheese'],
}

print("You ordered a "+pizza['crust']+"-crust pizza. " + "With the following toppings:")

for topping in pizza['topping']:
	print("\t" + topping)





