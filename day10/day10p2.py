import unittest


def parse_brackets(bracket_str: str) -> str:
	if not bracket_str:
		return 'complete'

	bracket_list = list(bracket_str)
	open_stack = []

	opens = ['(', '[', '{', '<']
	closes = [')', ']', '}', '>']
	open_stack.append(bracket_list.pop(0))
	# cover the case where the first element is a closing bracket
	if open_stack[0] in closes:
		return open_stack[0]
	else:
		# this basically just follows the normal single stack-based bracket matching method you run into in CS courses
		while bracket_list:
			cur = bracket_list.pop(0)
			if cur in opens:
				open_stack.append(cur)
			elif cur in closes:
				bracket_type = closes.index(cur)
				if not open_stack and cur in closes:  # if there's still closed brackets left and no more opens
					return "incomplete"               # then there's no valid match
				elif opens[bracket_type] == open_stack[-1]:
					open_stack.pop(-1)
				else:
					return cur

		# there were more closed brackets than opens or more opens than closes
		if (open_stack and not bracket_list) or ((not open_stack) and bracket_list):
			return 'incomplete'
		else:
			return 'complete'


# this function is basically the same as parse_brackets but instead passes back the list of brackets that don't match
def find_incomplete(bracket_str: str) -> [str]:
	if not bracket_str:
		return []

	bracket_list = list(bracket_str)
	open_stack = []

	opens = ['(', '[', '{', '<']
	closes = [')', ']', '}', '>']
	open_stack.append(bracket_list.pop(0))

	while bracket_list:
		cur = bracket_list.pop(0)
		if cur in opens:
			open_stack.append(cur)
		elif cur in closes:
			bracket_type = closes.index(cur)
			if not open_stack and cur in closes:
				return "incomplete"
			elif opens[bracket_type] == open_stack[-1]:
				open_stack.pop(-1)
			else:
				return []

	if open_stack and not bracket_list:
		return open_stack
	else:
		return []


def match_broken_brackets(brackets: [str]) -> str:
	matched = []

	for bracket in brackets:
		if bracket == '(':
			matched.append(')')
		elif bracket == '[':
			matched.append(']')
		elif bracket == '{':
			matched.append('}')
		elif bracket == '<':
			matched.append('>')

	return "".join(matched[::-1])


class BracketTests(unittest.TestCase):
	def tests(self):
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

		# a few more tests for part 2
		self.assertEqual(parse_brackets('[({(<(())[]>[[{[]{<()<>>'), 'incomplete')
		self.assertEqual(find_incomplete('[({(<(())[]>[[{[]{<()<>>'), ['[', '(', '{', '(', '[', '[', '{', '{'])
		self.assertEqual(parse_brackets('[(()[<>])]({[<{<<[]>>('), 'incomplete')
		self.assertEqual(find_incomplete('[(()[<>])]({[<{<<[]>>('), ['(', '{', '[',  '<', '{', '('])
		self.assertEqual(match_broken_brackets(['[', '(', '{', '(', '[', '[', '{', '{']), '}}]])})]')


if __name__ == '__main__':
	# unittest.main()
	with open('input.txt', 'r') as f:
		lines = f.read().split('\n')[:-1]
		f.close()
		result = []
		for line in lines:
			result.append(parse_brackets(line))

		broken_brackets = []

		for i in range(len(result)):
			if result[i] == 'incomplete':
				broken_brackets.append(find_incomplete(lines[i]))

		completion_strings = []

		for bb in broken_brackets:
			completion_strings.append(match_broken_brackets(bb))

		scores = {
			')': 1,
			']': 2,
			'}': 3,
			'>': 4
		}

		completion_string_scores = []

		for string in completion_strings:
			score = 0
			for s in string:
				score *= 5
				score += scores[s]
			completion_string_scores.append(score)

		print(sorted(completion_string_scores)[len(completion_string_scores)//2])
