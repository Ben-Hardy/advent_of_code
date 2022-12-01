with open('input/input.txt') as f:
	top_three = sum(sorted([sum(map(int, j.split('\n'))) for j in f.read().split('\n\n')])[-3:])
	print(top_three)
