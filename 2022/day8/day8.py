import numpy as np

with open('input/input.txt') as f:
	lines = f.read().split('\n')
	forest = np.matrix(" ".join([" ".join(i) + ';' for i in lines])[:-1])

	mask = np.zeros((forest.shape[0], forest.shape[1]), dtype=int)
	mask[0, :] = 1
	mask[:, 0] = 1
	mask[mask.shape[0] - 1, :] = 1
	mask[:, mask.shape[0] - 1] = 1
	print(forest)

	for i in range(1, forest.shape[0] - 1):
		for j in range(1, forest.shape[1] - 1):

			is_visible = True
			# check up
			for k in range(0, i):
				if forest[k, j] >= forest[i, j]:
					is_visible = False
			if is_visible:
				mask[i, j] = 1
			# check down
			if mask[i, j] == 0:
				is_visible = True

				for k in range(i + 1, forest.shape[0]):
					if forest[k, j] >= forest[i, j]:
						is_visible = False
				if is_visible:
					mask[i, j] = 1
			# check left
			if mask[i, j] == 0:
				is_visible = True

				for k in range(0, j):
					if forest[i, k] >= forest[i, j]:
						is_visible = False
				if is_visible:
					mask[i, j] = 1

			# check right
			if mask[i, j] == 0:
				is_visible = True

				for k in range(j + 1, forest.shape[1]):
					if forest[i, k] >= forest[i, j]:
						is_visible = False
				if is_visible:
					mask[i, j] = 1
	print(mask)

	print(sum(sum(mask)))