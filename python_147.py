def greet_user(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)


usernames= ['hannah', 'ty', 'margot']

greet_user(usernames)
