with open('input/input.txt', 'r') as f:
	pairs = f.read().split("\n")
	col1 = []
	col2 = []
	for pair in pairs:
		result = [int(i) for i in pair.split()]
		col1.append(result[0])
		col2.append(result[1])
	
	unique_nums = list(set(col1))
	sim_scores = [unique_num * col2.count(unique_num) for unique_num in unique_nums]
	print(sum(sim_scores))
