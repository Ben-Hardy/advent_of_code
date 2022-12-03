with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')

	extras = []
	for i in range(0, len(lines), 3):
		overlaps = set(lines[i]).intersection(lines[i + 1])
		overlaps = overlaps.intersection(lines[i + 2])
		extras.append(list(overlaps)[0])

	total = sum(['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(i) + 1 for i in extras])
	print(total)
