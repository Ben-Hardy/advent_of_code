import numpy as np


# I'm treating this problem like drawing on a canvas from one point to another
class GridCanvas:
	def __init__(self, width, height):
		self.grid = np.zeros((width, height), dtype=int)

	def draw(self, first, second):
		# columns match but first row bigger than second
		if first[0] > second[0]:
			self.grid[second[0]:first[0]+1, first[1]] += 1
		# columns match but second row bigger than first
		elif second[0] > first[0]:
			self.grid[first[0]:second[0]+1, first[1]] += 1
		# rows match but first column bigger than second
		elif first[1] > second[1]:
			self.grid[second[0], second[1]:first[1]+1] += 1
		# rows match but second column bigger than first
		elif second[1] > first[1]:
			self.grid[second[0], first[1]:second[1]+1] += 1

	def print_grid(self):
		print(self.grid)

	def count_overlaps(self):
		total = 0
		for i in range(self.grid.shape[0]):
			for j in range(self.grid.shape[1]):
				if self.grid[i, j] > 1:
					total += 1
		return total


with open('small_input.txt', 'r') as f:
	my_grid = GridCanvas(10, 10)
	contents = f.read().split('\n')[:-1]
	f.close()

	for line in contents:
		cur_pair = line.split(' -> ')
		first_point = [int(i) for i in cur_pair[0].split(',')]
		second_point = [int(i) for i in cur_pair[1].split(',')]

		if first_point[0] == second_point[0] or first_point[1] == second_point[1]:
			my_grid.draw(first_point, second_point)
			my_grid.print_grid()

	my_grid.print_grid()
	print(my_grid.count_overlaps())

with open('input.txt', 'r') as f:
	my_grid = GridCanvas(1000, 1000)
	contents = f.read().split('\n')[:-1]
	f.close()

	for line in contents:
		cur_pair = line.split(' -> ')
		first = [int(i) for i in cur_pair[0].split(',')]
		second = [int(i) for i in cur_pair[1].split(',')]

		if first[0] == second[0] or first[1] == second[1]:
			my_grid.draw(first, second)

	print(my_grid.count_overlaps())
