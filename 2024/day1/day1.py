with open('input/input.txt', 'r') as f:
	pairs = f.read().split("\n")
	col1 = []
	col2 = []
	for pair in pairs:
		result = [int(i) for i in pair.split()]
		col1.append(result[0])
		col2.append(result[1])
	
	diffs = [abs(x - y) for x,y in zip(sorted(col1), sorted(col2))]
	print(sum(diffs))
	