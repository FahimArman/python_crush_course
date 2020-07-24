filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("Writting in a append mode.\n")


with open(filename) as file_object:
	print(file_object.read())
