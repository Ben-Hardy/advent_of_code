import unittest


def parse_brackets(s: str) -> str:
	if not s:
		return 'complete'

	bracket_list = list(s)
	open_stack = []

	opens = ['(', '[', '{', '<']
	closes = [')', ']', '}', '>']
	open_stack.append(bracket_list.pop(0))
	# cover the case where the first element is a closing bracket
	if open_stack[0] in closes:
		return open_stack[0]
	else:
		while open_stack and bracket_list:
			cur = bracket_list.pop(0)
			if cur in opens:
				open_stack.append(cur)
			elif cur in closes:
				bracket_type = closes.index(cur)
				if opens[bracket_type] == open_stack[-1]:
					open_stack.pop(-1)
				else:
					return cur

		# there were more closed brackets than opens or more opens than closes
		if (open_stack and not bracket_list) or ((not open_stack) and bracket_list):
			return 'incomplete'
		else:
			return 'complete'


class BracketTests(unittest.TestCase):
	def test_parse_brackets(self):
		self.assertEqual(parse_brackets(''), 'complete')
		self.assertEqual(parse_brackets(')'), ')')
		self.assertEqual(parse_brackets('()'), 'complete')
		self.assertEqual(parse_brackets('(]'), ']')
		self.assertEqual(parse_brackets('((()'), 'incomplete')
		self.assertEqual(parse_brackets('()))'), 'incomplete')

		# all of the part 1 example tests
		self.assertEqual(parse_brackets('{([(<{}[<>[]}>{[]{[(<()>'), '}')
		self.assertEqual(parse_brackets('[[<[([]))<([[{}[[()]]]'), ')')
		self.assertEqual(parse_brackets('[{[{({}]{}}([{[{{{}}([]'), ']')
		self.assertEqual(parse_brackets('[<(<(<(<{}))><([]([]()'), ')')
		self.assertEqual(parse_brackets('<{([([[(<>()){}]>(<<{{'), '>')


if __name__ == '__main__':
	# unittest.main()
	with open('input.txt', 'r') as f:
		lines = f.read().split('\n')[:-1]
		f.close()
		result = []
		for line in lines:
			result.append(parse_brackets(line))

		result = [i for i in result if not i == 'incomplete']

		point_dict = {
			")": 3,
			"]": 57,
			"}": 1197,
			">": 25137
		}

		points_total = 0

		for i in result:
			points_total += point_dict[i]

		print(points_total)
