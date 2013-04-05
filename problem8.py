def product(n, x): # n is number, x is how many digits to multiply together
	s = str(n) # convert to a string
	l = list(s) # convert to a list of characters (to be able to use slices later)

	for i in range(len(l)): # convert each item in list back to an integer
		l[i] = int(l[i])

	max_product = 1

	for i in range(len(l)-(x-1)): # iterate through all indexes up until last set of digits to multiple together at the end

		potential_product = 1

		for num in l[i:i+x]: # multiple together x digits in slice of full number
			potential_product *= num

		if potential_product > max_product: # compare if new product is greater than any previous product produced
			max_product = potential_product

	return max_product

# for problem #8, had to convert 1000-digit number to be all on one line, and then pass in 5 for x