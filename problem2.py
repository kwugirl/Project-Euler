first = 1
second = 1

even_fibonacci = []

while first + second < 4000000:
	x = first + second
	if x % 2 == 0:
		even_fibonacci.append(x)

	# reset fibonacci numbers
	first = second
	second = x
# 	print x

# print even_fibonacci

sum = 0

for evens in even_fibonacci:
	sum += evens

print sum