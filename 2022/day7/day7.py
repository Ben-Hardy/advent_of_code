with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')

	cur_dir = '/'
	prev_dirs = []
	path = '/'
	files = {}
	dirs = {}
	for line in lines:
		if line[0] == '$':
			chunks = line.split()
			if chunks[1] == 'cd':
				if chunks[2] == '/':
					path = '/'
					dirs['/'] = 0
					prev_dirs = []
				elif chunks[2] == '..':
					if len(prev_dirs) == 2:
						prev_dirs = []
						path = '/'
						cur_dir = '/'
					if path != '/':
						path = path[:-1 * (len(cur_dir) + 1)]
						prev_dirs.pop(-1)
				else:
					prev_dirs.append(path)
					path += f'{chunks[2]}/'
					cur_dir = chunks[2]

				#print(path)

		else:
			chunks = line.split()
			if chunks[0] != 'dir':
				files[chunks[0] + " " + path + chunks[1]] = prev_dirs + [path]
				dirs[path] = 0

	print(files)

	for fi in files.keys():
		amount = int(fi.split()[0])

		for d in files[fi]:
			if d not in dirs:
				dirs[d] = amount
			else:
				dirs[d] += amount
	print(dirs)
	filtered = [i for i in dirs.values() if i <= 100000]
	print(filtered)
	print(sum(filtered))
