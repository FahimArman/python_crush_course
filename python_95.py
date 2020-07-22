#dictionary

# key-value pair


alien={'color':'green', 'point':5}

print(alien['color'])
print(alien['point'])

print("keys are: %s" % alien.keys())
print("values are: %s" % list(alien.values()))
print("Items are: %s" % alien.items())

alien['x_position'] = 0
alien['y_position'] = 25

print(alien)



user = {
	'username':'alice1234',
	'first':'alica',
	'last':'cutler',
}


for key,value in user.items():
	print("\nKey: "+key)
	print("Values: "+value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]




