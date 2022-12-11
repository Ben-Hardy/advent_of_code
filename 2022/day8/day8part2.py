import numpy as np
from functools import reduce
with open('input/input.txt') as f:
	lines = f.read().split('\n')
	forest = np.matrix(" ".join([" ".join(i) + ';' for i in lines])[:-1])

	mask = np.zeros((forest.shape[0], forest.shape[1]), dtype=int)
	mask[0, :] = 1
	mask[:, 0] = 1
	mask[mask.shape[0] - 1, :] = 1
	mask[:, mask.shape[0] - 1] = 1

	overall_scores = []
	for i in range(1, forest.shape[0] - 1):
		for j in range(1, forest.shape[1] - 1):

			# score going upward
			scores = [0, 0, 0, 0]
			it = list(range(i - 1, 0 - 1, -1))
			to_comp = forest[i, j]
			for k in it: # i - 1 because it will include current index otherwise
				cur = forest[k, j]
				if cur >= to_comp:
					scores[0] += 1
					break
				else:
					scores[0] += 1
			# score downward
			it = list(range(i + 1, forest.shape[0])) # i + 1 to avoid comparing to_comp to itself
			for k in it:
				cur = forest[k, j]
				if cur >= to_comp:
					scores[1] += 1
					break
				else:
					scores[1] += 1
			# score left
			it = list(range(j - 1, 0 - 1, -1))
			for k in it:
				cur = forest[i, k]
				if cur >= to_comp:
					scores[2] += 1
					break
				else:
					scores[2] += 1
			# score downward
			it = list(range(j + 1, forest.shape[1]))
			for k in it:
				cur = forest[i, k]
				if cur >= to_comp:
					scores[3] += 1
					break
				else:
					scores[3] += 1

			overall_scores.append(reduce(lambda x, y: x * y, scores))

	print(overall_scores)
	print(max(overall_scores))