from collections import deque

with open('input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	polymer = lines[0]
	
	lines = lines[2:]
	lines = [i.split(' -> ') for i in lines]
	
	insertions = {i[0]: i[1] for i in lines}

	steps = 10
	
	for step in range(steps):
		print(f"step {step + 1}")
		pairs = [polymer[i:i+2] for i in range(len(polymer) - 1)]

		result = deque()
		buffer = open("buffer.txt", 'w')
		buffer.seek(0)
		for i in range(len(pairs)):
			if i % 10000 == 0:
				buffer.write(("".join(result)))
				result = deque()
			result.append(pairs[i][0])
			result.append(insertions[pairs[i]])
			
			if i == len(pairs) - 1:
				result.append(pairs[i][1])
		buffer.write("".join(result))
		buffer.close()
		buffer = open("buffer.txt", 'r')
		polymer = "".join(buffer.read().rstrip())
		buffer.close()
		
	chars = list(set(insertions.values()))
	
	char_counts = {char: polymer.count(char) for char in chars}
	print(char_counts)
	char_max = max(list(set(char_counts.values())))
	char_min = min(list(set(char_counts.values())))
	print(char_max - char_min)
