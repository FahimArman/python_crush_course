prompt = "\nTell me somethhing, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the programme.  "

active = True

while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print("--->" + message)
