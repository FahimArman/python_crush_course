my_foods = ['pizza','falafel', 'carrot cake']

friend_foods = my_foods[:]


print("My favourite foods are: ")
print(my_foods)

print("My friends favourite foods are: ")
print(friend_foods) 

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are: ")
print(my_foods)

print("My friends favourite foods are: ")
print(friend_foods) 


### this will not work

a_foods=['pizza','falafel', 'carrot cake']

#this will not work
b_foods = a_foods

print("A foods are: ")
print(a_foods)

print("B foods are: ")
print(b_foods) 

a_foods.append('cannoli')
b_foods.append('ice cream')


print("A foods are: ")
print(a_foods)

print("B foods are: ")
print(b_foods)





