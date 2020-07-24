print("Give me two numbers. I will divide.")
print("Enter 'q' to quit.")

while True:
	first= input("Enter first number: ")
	if first == 'q':
		break

	second = input ("Enter second number: ")
	if second == 'q':
		break

	try:
		answer = int(first)/int(second)
	except ZeroDivisionError:
		print("--> Can't divid by zero.")
	else:
		print("-->" + str(answer))
