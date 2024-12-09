import numpy as np


def print_map(arr, visited):
	for v in visited:
		arr[v[0], v[1]] = 4
	print(arr)


def traverse_field(arr):
	cur_facing = 'N'
	cur_r = -1
	cur_c = -1
	start = np.where(arr == 2) # will only be 2 in one location in the matrix
	cur_r = start[0][0]
	cur_c = start[1][0]

	visited = [(cur_r, cur_c)]
	exiting = False

	while not exiting:
		did_move = False
		if cur_facing == 'N' and not did_move:
			next_r = cur_r - 1
			next_c = cur_c
			if next_r < 0:
				exiting = True
				did_move = True
			elif arr[next_r, next_c] == 1:
				cur_facing = 'E'
			else:
				cur_r = next_r
				cur_c = next_c
				visited.append((cur_r, cur_c))
				did_move = True
		if cur_facing == 'E' and not did_move:
			next_r = cur_r
			next_c = cur_c + 1
			if next_c >= arr.shape[1]:
				exiting = True
				did_move = True
			elif arr[next_r, next_c] == 1:
				cur_facing = 'S'
			else:
				cur_r = next_r
				cur_c = next_c
				visited.append((cur_r, cur_c))
				did_move = True
		if cur_facing == 'S' and not did_move:
			next_r = cur_r + 1
			next_c = cur_c
			if next_r >= arr.shape[0]:
				exiting = True
				did_move = True
			elif arr[next_r, next_c] == 1:
				cur_facing = 'W'
			else:
				cur_r = next_r
				cur_c = next_c
				visited.append((cur_r, cur_c))
				did_move = True
		if cur_facing == 'W' and not did_move:
			next_r = cur_r
			next_c = cur_c - 1
			if next_c < 0:
				exiting = True
				did_move = True
			elif arr[next_r, next_c] == 1:
				cur_facing = 'N'
			else:
				cur_r = next_r
				cur_c = next_c
				visited.append((cur_r, cur_c))
				did_move = True

	print(len(set(visited)))


with open('input/input.txt', 'r') as f:
	data = f.read().split('\n')
	conversions = {'.': 0, '#': 1, '^': 2}
	data_as_nums = [[conversions[i] for i in line] for line in data]
	input_arr = np.array(data_as_nums)
	traverse_field(input_arr)