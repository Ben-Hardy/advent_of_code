with open('biginput.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	print("\n".join(lines))

	total = 0
	num_winning_nums = 10
	num_player_nums = 25

	card_counts = [1 for i in range(len(lines))]
	for card in range(len(lines)):
		chunks = lines[card].split()
		cur_card = int(chunks[1][:-1])

		chunks = chunks[2:]
		print(f"Processing card {cur_card}")
		print(chunks)

		winning_nums = [int(i) for i in chunks[:num_winning_nums]]
		player_nums = [int(i) for i in chunks[num_winning_nums + 1:]]

		score = 0
		for num in player_nums:
			if num in winning_nums:
				score += 1
		if score > 0:
			for i in range(card + 1, card + 1 + score):
				card_counts[i] += card_counts[card]
		print(f"Total: {sum(card_counts)}")


