prompt = "\nTell me somethhing, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the programme.  "

message = ""

while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print("-->" + message)







