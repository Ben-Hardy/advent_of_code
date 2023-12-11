with open('input/biginput.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]

	pattern = lines[0]
	lines = lines[2:]

	codes = {}
	for line in lines:
		chunks = line.split()
		codes[chunks[0]] = [chunks[2][1:4], chunks[3][:3]]

	cur = "AAA"
	steps = 0
	while cur != "ZZZ":
		for i in range(len(pattern)):
			if cur == "ZZZ":
				break
			steps += 1
			if pattern[i] == "L":
				cur = codes[cur][0]
			elif pattern[i] == "R":
				cur = codes[cur][1]
	print(steps)
