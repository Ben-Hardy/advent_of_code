
class Operation:
	def __init__(self, instruction, sign, number):
		self.instruction = instruction
		self.sign = sign
		self.number = number
		self.was_used = False

	def __str__(self):
		return f"{self.instruction} {self.sign}{self.number} {self.was_used}"


with open('input/input.txt') as f:
	lines = f.read().split('\n')

	operations = []
	for line in lines:
		chunks = line.split()
		opsign = chunks[1][0]
		num = chunks[1][1:]
		operations.append(Operation(chunks[0], opsign, int(num)))

	acc = 0
	idx = 0

	is_looping = True

	while is_looping:
		#print(f"Current instruction: {operations[idx].instruction} {operations[idx].sign}{operations[idx].number}")
		if operations[idx].was_used:
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

	print(f'Final accumulator amount: {acc}')
