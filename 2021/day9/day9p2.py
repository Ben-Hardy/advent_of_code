# I'm gonna use numpy for this though it'd be just as doable without it. I just like
# the MATLAB syntax of numpy arrays
import numpy as np

with open("input.txt", 'r') as f:
	numbers = f.read().split('\n')[:-1]
	numbers = [list(i) for i in numbers]
	
	f.close()
	
	nums_as_ints = []

	for row in numbers:
		nums_as_ints.append([int(i) for i in row])

	num_mat = np.array(nums_as_ints, dtype=int)

	top = 0
	bottom = num_mat.shape[0] - 1

	left = 0
	right = num_mat.shape[1] - 1

	# we're going to store tuples of indices for each low point
	lows = []

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
			elif i == top:
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

	basins = []

	for idx in range(len(lows)):
		search_list = [lows[idx]]
		basin = []

		# this is hilarious
		# the gist of this nightmare is that it treats the search list like a queue.
		# while the search_list has items in it, this will pop the top item off, look at all adjacent locations,
		# and if those locations haven't been searched yet and aren't equal to 9, they will be chucked onto the
		# search_list queue. you start out by populating the queue with the low point, and it expands from there.
		# this is basically some technique from image processing class for segmenting out an image using edges
		# but not done in nearly as fancy or formal of a way
		while search_list:
			cur_loc = search_list.pop(0)

			i, j = cur_loc
			# corner cases
			if i == top and j == left:
				if num_mat[i, j + 1] < 9 and ((i, j + 1) not in search_list and (i, j + 1) not in basin):
					search_list.append((i, j + 1))
				if num_mat[i + 1, j] < 9 and ((i + 1, j) not in search_list and (i + 1, j) not in basin):
					search_list.append((i + 1, j))
			elif i == top and j == right:
				if num_mat[i, j - 1] < 9 and ((i, j - 1) not in search_list and (i, j - 1) not in basin):
					search_list.append((i, j - 1))
				if num_mat[i + 1, j] < 9 and ((i + 1, j) not in search_list and (i + 1, j) not in basin):
					search_list.append((i + 1, j))
			elif i == bottom and j == left:
				if num_mat[i, j + 1] < 9 and ((i, j + 1) not in search_list and (i, j + 1) not in basin):
					search_list.append((i, j + 1))
				if num_mat[i - 1, j] < 9 and ((i - 1, j) not in search_list and (i - 1, j) not in basin):
					search_list.append((i - 1, j))
			elif i == bottom and j == right:
				if num_mat[i, j - 1] < 9 and ((i, j - 1) not in search_list and (i, j - 1) not in basin):
					search_list.append((i, j - 1))
				if num_mat[i - 1, j] < 9 and ((i - 1, j) not in search_list and (i - 1, j) not in basin):
					search_list.append((i - 1, j))
			# edge cases. yup there's that bad joke again
			elif i == top:
				if num_mat[i, j + 1] < 9 and ((i, j + 1) not in search_list and (i, j + 1) not in basin):
					search_list.append((i, j + 1))
				if num_mat[i + 1, j] < 9 and ((i + 1, j) not in search_list and (i + 1, j) not in basin):
					search_list.append((i + 1, j))
				if num_mat[i, j - 1] < 9 and ((i, j - 1) not in search_list and (i, j - 1) not in basin):
					search_list.append((i, j - 1))
			elif i == bottom:
				if num_mat[i, j - 1] < 9 and ((i, j - 1) not in search_list and (i, j - 1) not in basin):
					search_list.append((i, j - 1))
				if num_mat[i - 1, j] < 9 and ((i - 1, j) not in search_list and (i - 1, j) not in basin):
					search_list.append((i - 1, j))
				if num_mat[i, j + 1] < 9 and ((i, j + 1) not in search_list and (i, j + 1) not in basin):
					search_list.append((i, j + 1))
			elif j == left:
				if num_mat[i - 1, j] < 9 and ((i - 1, j) not in search_list and (i - 1, j) not in basin):
					search_list.append((i - 1, j))
				if num_mat[i + 1, j] < 9 and ((i + 1, j) not in search_list and (i + 1, j) not in basin):
					search_list.append((i + 1, j))
				if num_mat[i, j + 1] < 9 and ((i, j + 1) not in search_list and (i, j + 1) not in basin):
					search_list.append((i, j + 1))
			elif j == right:
				if num_mat[i - 1, j] < 9 and ((i - 1, j) not in search_list and (i - 1, j) not in basin):
					search_list.append((i - 1, j))
				if num_mat[i + 1, j] < 9 and ((i + 1, j) not in search_list and (i + 1, j) not in basin):
					search_list.append((i + 1, j))
				if num_mat[i, j - 1] < 9 and ((i, j - 1) not in search_list and (i, j - 1) not in basin):
					search_list.append((i, j - 1))
			else: # the general case.
				if num_mat[i, j + 1] < 9 and ((i, j + 1) not in search_list and (i, j + 1) not in basin):
					search_list.append((i, j + 1))
				if num_mat[i + 1, j] < 9 and ((i + 1, j) not in search_list and (i + 1, j) not in basin):
					search_list.append((i + 1, j))
				if num_mat[i, j - 1] < 9 and ((i, j - 1) not in search_list and (i, j - 1) not in basin):
					search_list.append((i, j - 1))
				if num_mat[i - 1, j] < 9 and ((i - 1, j) not in search_list and (i - 1, j) not in basin):
					search_list.append((i - 1, j))
			basin.append((i, j))
		basins.append(basin)

	basin_sizes = [len(b) for b in basins]
	score = 1
	for size in sorted(basin_sizes)[::-1][:3]:
		score *= size
	print(score)
