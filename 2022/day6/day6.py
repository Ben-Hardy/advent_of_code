with open('input/input.txt', 'r') as f:
	stream = f.read().split('\n')[0]

	# change to 4 to do part 1, change to 14 to do part 2
	window_size = 14

	for i in range(len(stream) - (window_size - 1)):
		if len(list(set(stream[i : i + window_size]))) == len(stream[i : i + window_size]):
			print(i + window_size)
			break
