with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')

	extras = []
	for line in lines:
		first_half = set(line[:len(line)//2])
		second_half = set(line[len(line)//2:])
		# use set intersection to find the item in both sets
		extras.append(list(first_half.intersection(second_half))[0])

	total = sum(['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(i) + 1 for i in extras])
	print(total)
