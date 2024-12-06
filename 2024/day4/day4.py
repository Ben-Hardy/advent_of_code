import numpy as np


def count_xmas(arr):
	xmas_count = 0
	dim_x = arr.shape[1]
	dim_y = arr.shape[0]
	valid = ['1234', '4321']

	for j in range(dim_y):
		for i in range(dim_x):
			if arr[j, i] == 1:
				# check west
				if i - 3 >= 0:
					is_xmas = ''.join(map(str, list(arr[j, i-3:i + 1]))) in valid
					if is_xmas:
						xmas_count += 1
				# check northwest
				if i - 3 >= 0 and j - 3 >= 0:
					temp = []
					for k in range(4):
						temp.append(arr[j - k, i - k])
					if ''.join(map(str, temp)) in valid:
						xmas_count += 1
				# check north
				if j - 3 >= 0:
					is_xmas = ''.join(map(str, list(arr[j-3:j+1, i]))) in valid
					if is_xmas:
						xmas_count += 1
				# check northeast:
				if j - 3 >= 0 and i + 3 < dim_x:
					temp = []
					for k in range(4):
						temp.append(arr[j - k, i + k])
					if ''.join(map(str, temp)) in valid:
						xmas_count += 1
				# check east:
				if i + 3 < dim_x:
					is_xmas = ''.join(map(str, list(arr[j, i: i + 4]))) in valid
					if is_xmas:
						xmas_count += 1
				# check southeast
				if i + 3 < dim_x and j + 3 < dim_y:
					temp = []
					for k in range(4):
						temp.append(arr[j + k, i + k])
					if ''.join(map(str, temp)) in valid:
						xmas_count += 1
				# check south:
				if j + 3 < dim_y:
					is_xmas = ''.join(map(str, list(arr[j: j + 4, i]))) in valid
					if is_xmas:
						xmas_count += 1
				# check southwest
				if j + 3 < dim_y and i - 3 >= 0:
					temp = []
					for k in range(4):
						temp.append(arr[j + k, i - k])
					if ''.join(map(str, temp)) in valid:
						xmas_count += 1
	print(xmas_count)


with open('input/input.txt', 'r') as f:
	data = f.read().split('\n')
	conversions = {'.': 0, 'X': 1, 'M': 2, 'A': 3, 'S': 4}
	data_as_nums = [[conversions[i] for i in line] for line in data]
	input_arr = np.array(data_as_nums)

	count_xmas(input_arr)
