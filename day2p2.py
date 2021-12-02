f = open("day2_input.txt", "r")

instructions = f.read().split("\n")[:-1]
distance = 0
depth = 0
aim = 0

for instruction in instructions:
	inst_chunks = instruction.split(" ")
	inst_value = int(inst_chunks[1])
	
	if inst_chunks[0] == "forward":
		distance += inst_value
		depth += inst_value * aim
	elif inst_chunks[0] == "down":
		aim += inst_value
	elif inst_chunks[0] == "up":
		aim -= inst_value

print(f"{distance} {depth} {aim}")
print(f"{distance * depth}")