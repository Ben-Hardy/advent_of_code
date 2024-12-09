
with open('input/input.txt', 'r') as f:
	data = f.read().split('\n')
	rule_cnt = 0
	while data[rule_cnt] != '':
		rule_cnt += 1
	rules = data[:rule_cnt]
	afters = {}
	for rule in rules:
		chunks = list(map(int, rule.split('|')))
		if chunks[0] not in afters.keys():
			afters[chunks[0]] = [chunks[1]]
		else:
			afters[chunks[0]].append(chunks[1])

	total = 0
	updates = data[rule_cnt + 1:]
	afters_keys = list(afters.keys())
	for u in updates:
		update = list(map(int, u.split(',')))
		is_valid = True
		for i in range(len(update)):
			if update[i] in afters_keys:
				for j in afters[update[i]]:
					if j in update[:i]:
						is_valid = False

		if is_valid:
			total += update[len(update)//2]
	print(total)
