f = open("day2_input.txt", "r")

instructions = f.read().split("\n")[:-1]
distance = 0
depth = 0
aim = 0

for instruction in instructions:
	chunks = instruction.split(" ")

	if chunks[0] == "forward":
		distance += int(chunks[1])
		depth += int(chunks[1]) * aim
	elif chunks[0] == "down":
		aim += int(chunks[1])
	elif chunks[0] == "up":
		aim -= int(chunks[1])

print(f"{distance} {depth} {aim}")
print(f"{distance * depth}")