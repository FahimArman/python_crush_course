import pygal

from die import Die

die = Die()

results = []

for roll_num in range(100):
	result = die.roll()
	results.append(result)
#print(results)

frequencies = []
for value in range(1, die.num_sides+1):
	frequencie = results.count(value)
	frequencies.append(frequencie)
#print(frequencies)


hist = pygal.Bar()
hist.title = "Results of rolling one D6 100 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')







