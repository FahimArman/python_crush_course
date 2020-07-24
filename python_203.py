filename = 'alice.txt'

try:
	with open(filename) as f_object:
		contents = f_object.read()

except FileNotFoundError:
	print("sorry, the file" + filename + "does not exist in the directory.")









