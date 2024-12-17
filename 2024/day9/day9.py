with open('input/input.txt', 'r') as f:
	data = list(map(int, f.read().split('\n')[0]))

	result = []
	is_num = True
	cur_ID = 0
	while len(data) > 0:
		cur = data.pop(0)
		if is_num:
			for i in range(cur):
				result.append(cur_ID)
			cur_ID += 1
		else:
			for i in range(cur):
				result.append(-1)
		is_num = not is_num

	last_idx = -1
	step = 0
	for i in range(len(result) - 1, -1, -1):
		if result[i] != -1:
			last_idx = i
			break
	while -1 in result[:last_idx + 1]:
		for i in range(len(result)):
			if result[i] == -1:
				temp = result[last_idx]
				result = result[:i] + [result[last_idx]] + result[i+1:]
				result = result[:last_idx] + [-1] + result[last_idx + 1:]
				last_idx -= 1
				print(f'on step {step}')
				step += 1
				break
	compr_res = list(map(int, result[:last_idx + 1]))
	check_sum = 0
	for i in range(len(compr_res)):
		check_sum += i * compr_res[i]
	print(check_sum)
