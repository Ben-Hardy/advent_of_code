# part 2
with open('input/input.txt') as f:
	lines = f.read().split('\n')
	
	good_passwords = 0

	for line in lines:
		parts = line.split(":")
		password = parts[1].strip()
		rule = parts[0].split()
		bounds = list(map(int, rule[0].split("-")))

		counter = 0
		if password[bounds[0] - 1] == rule[1]:
			counter += 1
		if password[bounds[1] - 1] == rule[1]:
			counter += 1
		if counter == 1:
			good_passwords += 1
	
	print(f"number of valid passwords: {good_passwords}")