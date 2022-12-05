with open('input/smallinput.txt', 'r') as f:
	chunks = f.read().split('\n\n')
	first_bit = chunks[0].split('\n')
	num_columns = int(first_bit[-1].split()[-1])

	print(chunks)
	cols = [[] for _ in range(num_columns)]

	for bit in first_bit[:-1]:
		current = bit
		col = 0
		while len(current) > 0:
			if current[:3] != '   ':
				cols[col].append(current[1])
			current = current[3:]
			if len(current) > 0:
				current = current[1:]
			col += 1

	print(cols)

	second_bit = chunks[1].split('\n')

	instructions = []
	for bit in second_bit:
		inst = bit.split()
		instructions.append([int(inst[1]), int(inst[3]), int(inst[5])])

	print(instructions)

	for instruction in instructions:
		num_to_move = instruction[0]
		from_col = instruction[1]
		to_col = instruction[2]

		for _ in range(num_to_move):
			tmp = cols[from_col - 1].pop(0)
			cols[to_col - 1].insert(0, tmp)

	print(cols)

	print(''.join(i[0] for i in cols if i))
