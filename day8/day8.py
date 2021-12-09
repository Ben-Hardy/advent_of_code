with open("input.txt") as f:
	lines = [i.split(' | ') for i in f.read().split('\n')[:-1]]
	outputs = [i[1] for i in lines]

	print(outputs)

	numbers_total = 0

	for i in outputs:
		number_codes = i.split()

		lens_to_look_for = [2, 3, 4, 7]
		for code in number_codes:
			if len(code) in lens_to_look_for:
				numbers_total += 1

	print(numbers_total)
