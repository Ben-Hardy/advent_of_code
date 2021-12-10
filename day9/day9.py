# I'm gonna use numpy for this though it'd be just as doable without it. I just like
# the MATLABness of numpy arrays
import numpy as np

with open("input.txt", 'r') as f:
	numbers = f.read().split('\n')[:-1]
	numbers = [list(i) for i in numbers]
	nums_as_ints = []
	for row in numbers:
		nums_as_ints.append([int(i) for i in row])

	num_mat = np.array(nums_as_ints, dtype=int)
	print(num_mat)

	top = 0
	bottom = num_mat.shape[0] - 1

	left = 0
	right = num_mat.shape[1] - 1

	# we're going to store tuples of indices for each low point in lows
	lows = []
	# shape is (5, 10)
	for i in range(num_mat.shape[0]):
		for j in range(num_mat.shape[1]):
			# let's handle the special cases first:

			# first the corner cases:
			if i == top and j == left:
				if num_mat[i, j] < num_mat[i + 1, j] and num_mat[i, j] < num_mat[i, j + 1]:
					lows.append((i, j))
			elif i == top and j == right:
				if num_mat[i, j] < num_mat[i + 1, j] and num_mat[i, j] < num_mat[i, j - 1]:
					lows.append((i, j))
			elif i == bottom and j == left:
				if num_mat[i, j] < num_mat[i - 1, j] and num_mat[i, j] < num_mat[i, j + 1]:
					lows.append((i, j))
			elif i == bottom and j == right:
				if num_mat[i, j] < num_mat[i - 1, j] and num_mat[i, j] < num_mat[i, j - 1]:
					lows.append((i, j))
			# now the edge cases. HA. get it? edge case? ok I'm done now
			elif i == top: # top edge case
				if (num_mat[i, j] < num_mat[i + 1, j] and num_mat[i, j] < num_mat[i, j - 1]) and num_mat[i, j] < num_mat[i, j + 1]:
					lows.append((i, j))
			elif i == bottom:
				if (num_mat[i, j] < num_mat[i - 1, j] and num_mat[i, j] < num_mat[i, j - 1]) and num_mat[i, j] < num_mat[i, j + 1]:
					lows.append((i, j))
			elif j == left:
				if (num_mat[i, j] < num_mat[i + 1, j] and num_mat[i, j] < num_mat[i, j + 1]) and num_mat[i, j] < num_mat[i - 1, j]:
					lows.append((i, j))
			elif j == right:
				if (num_mat[i, j] < num_mat[i + 1, j] and num_mat[i, j] < num_mat[i, j - 1]) and num_mat[i, j] < num_mat[i - 1, j]:
					lows.append((i, j))
			else:
				if (num_mat[i, j] < num_mat[i + 1, j] and num_mat[i, j] < num_mat[i - 1, j]) and (num_mat[i, j] < num_mat[i, j + 1] and num_mat[i, j] < num_mat[i, j - 1]):
					lows.append((i, j))
	low_sum = 0
	for low in lows:
		low_sum += num_mat[low[0], low[1]] + 1

	print(low_sum)
