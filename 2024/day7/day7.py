import itertools


with open('input/input.txt', 'r') as f:
	data = f.read().split('\n')

	chunks = [i.split(':') for i in data]
	total = 0

	for chunk in chunks:
		goal = int(chunk[0])
		nums = list(map(int, chunk[1][1:].split(' ')))

		# generate combinations of signs
		combos = list(itertools.product(['+', '*'], repeat=len(nums) - 1))

		combos = [''.join(i) for i in combos]
		goal_met = False
		for combo in combos:

			temp = nums.copy()
			signs = list(combo)
			cur_total = 0
			while len(temp) > 1:
				first = temp.pop(0)
				second = temp.pop(0)
				cur_sign = signs.pop(0)
				if cur_sign == '+':
					temp.insert(0, first + second)
				elif cur_sign == '*':
					temp.insert(0, first * second)
			# print(f'combo:{combo}, total: {temp[0]}, goal: {goal}')
			if temp[0] == goal:
				goal_met = True
		if goal_met:
			total += goal

	print(total)
