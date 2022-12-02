with open('input/input.txt') as f:
	highest = max([sum(map(int, j.split('\n'))) for j in f.read().split('\n\n')])
	print(highest)
