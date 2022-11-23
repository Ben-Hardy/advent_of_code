with open('input/input.txt') as f:
	lines = f.read().split('\n')

	group_answer_sizes = []

	cur_answers = []
	for line in lines:
		if line != '':
			cur_answers.append(set(line))
		else:
			answer_set = cur_answers[0]
			for answer in cur_answers:
				answer_set = answer_set.intersection(answer) # yay set theory
			group_answer_sizes.append(len(answer_set))
			cur_answers = []
	print(sum(group_answer_sizes))