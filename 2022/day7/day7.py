with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')

	cur_dir = ''
	prev_dirs = []

	files = {}
	dirs = {}
	for line in lines:
		print(line)
		if line[0] == '$':
			chunks = line.split()
			if chunks[1] == 'cd':
				if chunks[2] == '/':
					cur_dir = '/'
					dirs['/'] = 0
					prev_dirs = []
				elif chunks[2] == '..':
					if cur_dir != '/':
						cur_dir = prev_dirs[-1]
						prev_dirs.pop(-1)
				else:
					prev_dirs.append(cur_dir)
					cur_dir = chunks[2]
					dirs[cur_dir] = 0
		else:
			chunks = line.split()
			if chunks[0] != 'dir':
				files[line] = prev_dirs + [cur_dir]
			else:
				dirs[chunks[1]] = 0
	print(files)
	print(dirs)

	for k in files.keys():
		file_size = int(k.split()[0])
		for d in files[k]:
			dirs[d] += file_size
	totals = [i[1] for i in dirs.items() if i[1] <= 100000]
	print(dirs)
	print(sum(totals))

