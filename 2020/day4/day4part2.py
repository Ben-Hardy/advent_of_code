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
	print(passports)

	is_valid = False
	num_passports = 0
	for passport in passports:
		if len(passport.keys()) < 7:
			continue
		else:
			valid_score = 0
			if 'byr' in passport.keys():
				if 1920 <= int(passport['byr']) <= 2002:
					valid_score += 1
			if 'iyr' in passport.keys():
				if 2010 <= int(passport['iyr']) <= 2020:
					valid_score += 1
			if 'eyr' in passport.keys():
				if 2020 <= int(passport['eyr']) <= 2030:
					valid_score += 1
			if 'hgt' in passport.keys():
				if passport['hgt'][-2:] == 'cm':
					if 150 <= int(passport['hgt'][:-2]) <= 193:
						valid_score += 1
				if passport['hgt'][-2:] == 'in':
					if 59 <= int(passport['hgt'][:-2]) <= 76:
						valid_score += 1
			if 'hcl' in passport.keys():
				if passport['hcl'][0] == '#' and len(passport['hcl'][1:]) == 6:
					is_valid_hcl = True
					valid_hcl_codes = '0123456789abcdef'
					for i in passport['hcl'][1:]:
						if i not in valid_hcl_codes:
							is_valid_hcl = False
					if is_valid_hcl:
						valid_score += 1
			if 'ecl' in passport.keys():
				if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
					valid_score += 1
			if 'pid' in passport.keys():
				if len(passport['pid']) == 9 and passport['pid'].isdigit():
					valid_score += 1
		if valid_score == 7:
			num_passports += 1

	print(num_passports)