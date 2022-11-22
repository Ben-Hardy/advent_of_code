with open('input/input.txt') as f:
	lines = f.read().split('\n')

	passports = []
	cur_passport = {}
	for line in lines:
		if line != '':
			chunks = line.split()
			for chunk in chunks:
				sections = chunk.split(':')
				cur_passport[sections[0]] = sections[1]
		else:
			passports.append(cur_passport)
			cur_passport = {}

	valid_passports = 0
	for passport in passports:
		if len(passport.keys()) == 8:
			valid_passports += 1
		elif len(passport.keys()) == 7 and 'cid' not in passport.keys():
			valid_passports += 1
	print(f'Number of valid passports: {valid_passports}')

