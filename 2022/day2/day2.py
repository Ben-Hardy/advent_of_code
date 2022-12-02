def score_pairing(pair):
	opp, you = pair[0], pair[-1]

	you_idx = 'XYZ'.index(you)
	opp_idx = 'ABC'.index(opp)

	# this is basically a lookup table of all possible outcomes
	outcomes = [
		[3, 6, 0],
		[0, 3, 6],
		[6, 0, 3]
	]

	return you_idx + 1 + outcomes[opp_idx][you_idx]


with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')

	total = 0
	for line in lines:
		total += score_pairing(line)
	print(total)
