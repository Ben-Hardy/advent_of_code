# O(1) solution
def score_pairing(pair):
	opp, you = pair[0], pair[-1]

	opp_choices = {'A': 0, 'B': 1, 'C': 2}
	choices = {'X': 0, 'Y': 1, 'Z': 2}
	opp_idx = opp_choices[opp]
	you_idx = choices[you]

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