with open('input/input.txt') as f:
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
	pairs = {}
	numbers = sorted(lines)
	for i in range(len(numbers) - 2):
		for j in range(i, len(numbers) - 1):
			if numbers[i] + numbers[j] < 2020 and numbers[i] != numbers[j]:
				pairs[(numbers[i], numbers[j])] = numbers[i] + numbers[j]

	print(pairs)

	for p in pairs:
		for num in numbers:
			if pairs[p] + num == 2020:
				print(f"The triplet {p[0]}, {p[1]}, and {num} equal 2020")
				print(f"Their product is {p[0] * p[1] * num}")