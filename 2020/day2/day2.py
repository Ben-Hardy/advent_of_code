# part 1
with open('input/input.txt') as f:
	lines = f.read().split('\n')
	
	good_passwords = 0

	for line in lines:
		parts = line.split(":")
		password = parts[1].strip()
		rule = parts[0].split()
		bounds = list(map(int, rule[0].split("-")))

		if bounds[0] <= password.count(rule[1]) <= bounds[1]:
			good_passwords += 1

	print(f"number of valid passwords: {good_passwords}")
