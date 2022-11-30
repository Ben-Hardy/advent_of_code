
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


with open('input/input.txt') as f:
	lines = list(map(int, f.read().split('\n')))
	print(find_encoding_error(lines, 25))