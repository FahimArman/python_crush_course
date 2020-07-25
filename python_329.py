import matplotlib.pyplot as plt

x_values = list(range(1,100,1))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values,edgecolor='none', c =(0,1,0),s =20)


plt.title("square numbers", fontsize =24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("square of values", fontsize =14)

plt. tick_params(axis = 'both', which = 'major', labelsize =14)
plt.axis([0,100,0,10000])
plt.show()
