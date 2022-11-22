with open('input/input.txt') as f:
	lines = f.read().split('\n')
	hill = lines.copy()
	for line in lines:
		print(line)

	height = len(lines)
	width = len(lines[0])
	print(f"height: {height}, width: {width}")

	cur_h = 0
	cur_w = 0
	num_trees = 0

	while cur_h < height:
		if hill[cur_h][cur_w] == '#':
			num_trees += 1
		
		cur_h += 1
		cur_w += 3
		if cur_w >= width:
			cur_w -= width

	# part 2
	heights = [1, 1, 1, 1, 2]
	widths = [1, 3, 5, 7, 1]
	
	tree_amts = []
	cur_trees = 0
	cur_h = 0
	cur_w = 0
	for i in range(len(heights)):
		while cur_h < height:
			if hill[cur_h][cur_w] == '#':
				cur_trees += 1
			cur_h += heights[i]
			cur_w += widths[i]
			if cur_w >= width:
				cur_w -= width
		tree_amts.append(cur_trees)
		cur_trees = 0
		cur_h = 0
		cur_w = 0
	print(tree_amts)
 
	prod = 1
	for amt in tree_amts:
		prod  *= amt
	print(prod)
	