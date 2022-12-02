def score_pairing(pair):
	opp, you = pair.split()

	opp_choices = 'ABC'
	choices = 'XYZ'

	you_idx = choices.index(you)
	opp_idx = opp_choices.index(opp)

	# this is basially a lookup table of all possible outcomes
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