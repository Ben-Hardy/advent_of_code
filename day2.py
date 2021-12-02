f = open("day2_input.txt", "r")

instructions = f.read().split("\n")[:-1]
distance = 0
depth = 0

# fairly straightforward. we just have to go through each instruction and 
# update distance or depth accordingly
for instruction in instructions:
	inst_chunks = instruction.split(" ")

	if inst_chunks[0] == "forward":
		distance += int(inst_chunks[1])
	elif inst_chunks[0] == "down":
		depth += int(inst_chunks[1])
	elif inst_chunks[0] == "up":
		depth -= int(inst_chunks[1])

print(f"{distance} {depth}")
print(f"{distance * depth}")
