import numpy as np


with open('input.txt', 'r') as f:

	nums = list(map(int, f.read().split(',')))
	f.close()
	furthest = max(nums)
	fuel_loads = [0] * furthest

	# to handle the part 2 fuel loads, we're going to pre-compute them to save time
	# rather than computing each one individually.

	# it's just a cumulative sum so I'm going to use numpy to make it easier
	fuel_per_distance = np.cumsum(np.array(list(range(furthest + 1)), int))

	# now we can just use fuel_per_distance as a lookup table for each crab's distance
	for i in range(furthest):
		fuel_loads[i] = sum([fuel_per_distance[abs(x - i)] for x in nums])
	print(min(fuel_loads))
