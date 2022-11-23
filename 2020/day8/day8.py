
class Operation:
	def __init__(self, instruction, sign, number):
		self.instruction = instruction
		self.sign = sign
		self.number = number
		self.was_used = False


with open('input/smallinput.txt') as f:
	lines = f.read().split('\n')
	print(lines)
	line = lines[0]