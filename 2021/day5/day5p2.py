import numpy as np


# Grid Canvas 2: Now with 45 degree diagonal lines
class GridCanvas2:
	def __init__(self, width, height):
		self.grid = np.zeros((width, height), dtype=int)

	def draw(self, first, second):
		# this first block handles vertical and horizontal lines
		if first[0] == second[0] or first[1] == second[1]:
			# columns match but first row bigger than second
			if first[0] > second[0]:
				self.grid[first[1], second[0]:first[0]+1] += 1
			# columns match but second row bigger than first
			elif second[0] > first[0]:
				self.grid[first[1], first[0]:second[0]+1] += 1
			# rows match but first column bigger than second
			elif first[1] > second[1]:
				self.grid[second[1]:first[1]+1, second[0]] += 1
			# rows match but second column bigger than first
			elif second[1] > first[1]:
				self.grid[first[1]:second[1]+1, second[0]] += 1
			else: # if this is reached, the first and second point are the same point
				self.grid[first[1], first[0]] += 1

		# here's where the actual part 2 stuff is:
		elif abs(first[0] == second[0]) == abs(first[1] == second[1]):  # because math
			to_mark = None

			# here we will be calculating all of the intermediate points
			# between the first point and the second point along the
			# diagonal line between them. unfortunately slicing doesn't work well here
			# so we just have to create the actual pairs of points then draw them out that way
			if first[0] < second[0] and first[1] < second[1]:
				xs = [i for i in range(first[0] + 1, second[0])]
				ys = [i for i in range(first[1] + 1, second[1])]
				to_mark = [[xs[i], ys[i]] for i in range(len(xs))]
			elif first[0] < second[0] and first[1] > second[1]:
				xs = [i for i in range(first[0]+1, second[0])]
				ys = [i for i in range(second[1] + 1, first[1])][::-1]
				to_mark = [[xs[i], ys[i]] for i in range(len(xs))]
			elif first[0] > second[0] and first[1] < second[1]:
				xs = [i for i in range(second[0] + 1, first[0])][::-1]
				ys =[i for i in range(first[1] + 1, second[1])]
				to_mark = [[xs[i], ys[i]] for i in range(len(xs))]
			elif first[0] > second[0] and first[1] > second[1]:
				xs = [i for i in range(second[0] + 1, first[0])][::-1]
				ys = [i for i in range(second[1] + 1, first[1])][::-1]
				to_mark = [[xs[i], ys[i]] for i in range(len(xs))]
			# finally, append the start and end points to the list of points to complete the line
			to_mark.append(first)
			to_mark.append(second)
			self.draw_list(to_mark)

	def draw_list(self, list_to_draw):
		if list_to_draw:
			for pair in list_to_draw:
				self.grid[pair[1], pair[0]] += 1

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
	my_grid = GridCanvas2(10, 10)
	contents = f.read().split('\n')[:-1]
	f.close()

	for line in contents:
		cur_pair = line.split(' -> ')
		first_point = [int(i) for i in cur_pair[0].split(',')]
		second_point = [int(i) for i in cur_pair[1].split(',')]

		print(cur_pair)
		my_grid.draw(first_point, second_point)
		my_grid.print_grid()
		# uncomment the below line if you want to see it marking out the canvas each go around
		# input()

	my_grid.print_grid()
	print(my_grid.count_overlaps())

with open('input.txt', 'r') as f:
	my_grid = GridCanvas2(1000, 1000)
	contents = f.read().split('\n')[:-1]
	f.close()

	for line in contents:
		cur_pair = line.split(' -> ')
		first_point = [int(i) for i in cur_pair[0].split(',')]
		second_point = [int(i) for i in cur_pair[1].split(',')]

		my_grid.draw(first_point, second_point)

	print(my_grid.count_overlaps())
