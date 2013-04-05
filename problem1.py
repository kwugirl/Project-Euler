multiples = []

for number in range(1, 1000):
	if number % 5 == 0:
		multiples.append(number)
	elif number % 3 == 0:
		multiples.append(number)
	else:
		pass

sum = 0

for index in range(len(multiples)):
	sum += multiples[index]
	
print sum