with open('input/smallinput.txt') as f:
	lines = list(map(int, f.read().split('\n')))
	numbers = sorted(lines)
	not_found = True

	start = 0
	while not_found:
		if numbers[start] + numbers[-1] < 2020:
			start += 1
		elif numbers[start] + numbers[-1] > 2020:
			numbers.pop(-1)
			start = 0
		else:
			not_found = False
	print(f"first: {numbers[start]}\nsecond: {numbers[-1]}\nproduct: {numbers[start] * numbers[-1]}")

	# part 2
