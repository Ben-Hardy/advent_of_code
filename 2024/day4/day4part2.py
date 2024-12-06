import numpy as np


def count_xmas(arr):
	xmas_count = 0
	dim_x = arr.shape[1]
	dim_y = arr.shape[0]

	valid = ['312', '213']
	for j in range(dim_y):
		for i in range(dim_x):
			if arr[j, i] == 1:
				if (i - 1 >= 0 and i + 1 < dim_x) and (j - 1 >= 0 and j + 1 < dim_y):
					lr_diag = ''.join(map(str, [arr[j - 1, i - 1], arr[j, i], arr[j + 1, i + 1]]))
					rl_diag = ''.join(map(str, [arr[j - 1, i + 1], arr[j, i], arr[j + 1, i - 1]]))
					if lr_diag in valid and rl_diag in valid:
						xmas_count += 1

	print(xmas_count)


with open('input/input.txt', 'r') as f:
	data = f.read().split('\n')

	conversions = {'.': 0, 'X': 0, 'M': 3, 'A': 1, 'S': 2}
	data_as_nums = [[conversions[i] for i in line] for line in data]

	input_arr = np.array(data_as_nums)
	count_xmas(input_arr)