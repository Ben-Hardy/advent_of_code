with open('input/input.txt') as f:
	lines = f.read().split('\n')

	group_answer_counts = []

	cur_answers = ''
	for line in lines:
		if line != '':
			cur_answers += line
		else:
			allowed_letters = 'abcxyz'
			valid_answers = ''
			for answer in cur_answers:
				if answer in allowed_letters:
					valid_answers += answer
			group_answer_counts.append(len(sorted(set(cur_answers))))
			cur_answers = ''
	print(sum(group_answer_counts))
	print(group_answer_counts)