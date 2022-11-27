import copy


class Operation:
	def __init__(self, instruction, sign, number):
		self.instruction = instruction
		self.sign = sign
		self.number = number
		self.was_used = False

	def __str__(self):
		return f"{self.instruction} {self.sign}{self.number} {self.was_used}"


def process_instructions(operations):
	acc = 0
	idx = 0
	is_looping = True

	while is_looping:

		if idx >= len(operations):
			is_looping = False
		elif operations[idx].was_used:
			is_looping = False

		elif operations[idx].instruction == 'nop':
			operations[idx].was_used = True
			idx += 1
		elif operations[idx].instruction == 'acc':
			if operations[idx].sign == '+':
				acc += operations[idx].number
			elif operations[idx].sign == '-':
				acc -= operations[idx].number
			operations[idx].was_used = True
			idx += 1
		elif operations[idx].instruction == 'jmp':
			operations[idx].was_used = True
			if operations[idx].sign == '+':
				idx += operations[idx].number
			elif operations[idx].sign == '-':
				idx -= operations[idx].number

	return acc, idx


with open('input/input.txt') as f:
	lines = f.read().split('\n')

	ops = []
	for line in lines:
		chunks = line.split()
		opsign = chunks[1][0]
		num = chunks[1][1:]
		ops.append(Operation(chunks[0], opsign, int(num)))

	ops_to_swap = [i for i in range(len(ops)) if ops[i].instruction in ['nop', 'jmp'] and ops[i].number != 0]

	result = None
	for o in ops_to_swap:
		temp_ops = copy.deepcopy(ops)
		if temp_ops[o].instruction == 'jmp':
			temp_ops[o].instruction = 'nop'
		else:
			temp_ops[o].instruction = 'jmp'
		result = process_instructions(temp_ops)

		if result[1] != len(ops):
			pass
		else:
			print(f"Bad instruction was \"{temp_ops[o]}\" at index {o}")
			break
	print(f"Final acc total: {result[0]}")
	print(f"Final idx: {result[1]}")
