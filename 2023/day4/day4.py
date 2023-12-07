with open('p1input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]

	total = 0
	num_winning_nums = 5
	num_player_nums = 8

	for line in lines:
		chunks = line.split()[2:]
		score = 0

		winning_nums = [int(i) for i in chunks[:num_winning_nums]]
		player_nums = [int(i) for i in chunks[num_winning_nums + 1:]]

		for num in player_nums:
			if num in winning_nums:
				if score == 0:
					score += 1
				else:
					score *= 2
		total += score

	print(f"total: {total}")
