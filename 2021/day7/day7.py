with open('input.txt', 'r') as f:
	nums = list(map(int, f.read().split(',')))
	f.close()
	print(nums)

	furthest = max(nums)
	fuel_loads = [0] * furthest

	for i in range(furthest):
		fuel_loads[i] = sum([abs(x - i) for x in nums])
	print(min(fuel_loads))
