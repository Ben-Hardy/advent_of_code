
def find_encoding_error(numbers, preamble):
	# this being n^3 is painful but it's only for up to 25 numbers so it doesn't matter.
	for i in range(preamble,len(numbers)):
		prevs = sorted(numbers[i-preamble:i])

		sums = []

		for j in range(len(prevs)):
			for k in range(1, len(prevs)):
				sums.append(prevs[j] + prevs[k])

		if numbers[i] not in sums:
			return numbers[i]

	return -1


def find_range_nums(numbers, total):
	max_idx = numbers.index(total)

	for i in range(2, max_idx):
		for j in range(max_idx - i):
			cur = numbers[j : j + i]
			cur_total = sum(cur)
			if cur_total == total:
				return min(cur), max(cur)
	return -1, -1


with open('input/input.txt') as f:
	lines = list(map(int, f.read().split('\n')))
	a = find_encoding_error(lines, 25)
	result = find_range_nums(lines, a)
	print(f"{result[0] + result[1]}")
