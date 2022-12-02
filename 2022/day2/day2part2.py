def score_pairing(pair):
	opp, you = pair[0], pair[-1]

	you_idx = 'XYZ'.index(you)
	opp_idx = 'ABC'.index(opp)

	# the table of outcome scores is modified to be what you should do rather than
	# what choice you are making.
	outcomes = [
		[3, 4, 8],
		[1, 5, 9],
		[2, 6, 7]
	]

	return outcomes[opp_idx][you_idx]


with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')

	total = 0
	for line in lines:
		total += score_pairing(line)
	print(total)
