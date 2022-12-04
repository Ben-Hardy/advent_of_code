
# checks if either pairs have any overlap at all
def check_inside(pair_one, pair_two):
	return pair_two[0] <= pair_one[0] <= pair_two[1] or pair_two[0] <= pair_one[1] <= pair_two[1]


with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')

	total = 0
	for line in lines:
		pairs = line.split(',')
		first = list(map(int, pairs[0].split('-')))
		second = list(map(int, pairs[1].split('-')))

		if check_inside(first, second) or check_inside(second, first):
			total += 1

	print(total)
