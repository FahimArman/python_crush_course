#dictionary in a dictionary

users = {

	'aeinstein':{
		'first':'albert',
		'last': 'einstine',
		'location' : 'priceton',
	},
	
	'mcurie':{
		'first':'madam',
		'last':'curie',
		'location':'paris',
	},
}


for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\n\tFull Name: "+full_name.title())
	print("\tLocation: " + location.title())







