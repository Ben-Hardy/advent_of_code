from collections import deque
import os
with open('input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	polymer = lines[0]
	
	lines = lines[2:]
	lines = [i.split(' -> ') for i in lines]
	
	insertions = {i[0]: i[1] for i in lines}

	steps = 10
	
	for step in range(steps):
		print(f"step {step + 1}")

		buffer = open("buffer.txt", 'w')
		buffer.seek(0)
		for i in range(len(polymer) - 1):
			result = deque()
			result.append(polymer[i])
			result.append(insertions[polymer[i:i+2]])
			buffer.write("".join(result))
		buffer.write(polymer[-1])
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
	os.remove('buffer.txt')
