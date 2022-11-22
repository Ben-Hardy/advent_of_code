with open('input/input.txt') as f:
	lines = f.read().split('\n')
	print(lines)
	seat_IDs = []

	for line in lines:
		iterations = [64, 32, 16, 8, 4, 2]
		row_range = [0, 127]
		row = -1
		for i in range(len(iterations)):
			if line[i] == 'F':
				row_range[1] -= iterations[i]
			else:
				row_range[0] += iterations[i]
		if line[6] == 'F':
			row = row_range[0]
		else:
			row = row_range[1]
		column = line[-3:]
		col_range = [0, 7]
		col_iters = [4, 2]

		for i in range(len(col_iters)):
			if column[i] == 'R':
				col_range[0] += col_iters[i]
			else:
				col_range[1] -= col_iters[i]
		if column[-1] == 'L':
			col = col_range[0]
		else:
			col = col_range[1]
		seat_ID = row * 8 + col
		seat_IDs.append(seat_ID)
		print(f'row {row}, column {col}, seat ID {seat_ID}')

	print(f'Max seat ID: {max(seat_IDs)}')

	for i in range(12, 872):
		if i not in seat_IDs:
			print(f'missing seat ID: {i}')


