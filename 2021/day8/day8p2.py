
# this helper function finds which letters are different between two strings and returns them as a list
def find_diff(str1, str2):
	s1 = set(str1)
	s2 = set(str2)
	return list(s1.symmetric_difference(s2))


with open("input.txt") as f:
	lines = [i.split(' | ') for i in f.read().split('\n')[:-1]]
	f.close()
	inputs = [i[0].split() for i in lines]
	output_codes = []

	for idx in range(len(inputs)):
		cur_input = inputs[idx]
		lens = [len(i) for i in cur_input]

		# we are going to organize the display location codes like so:
		# top - top row of display. corresponds to 'a' in the diagram in the problem outline
		# mid - middle horizontal row of display. corresponds to 'd' in the diagram in the problem outline
		# bot - bottom horizontal row of display. corresponds to 'g' in the diagram in the problem outline
		# ul - upper left vertical line on display. corresponds to 'b' in the diagram in the problem outline
		# ll - lower left vertical line on display. corresponds to 'e' in the diagram in the problem outline
		# ur - upper right vertical line on display. corresponds to 'c' in the diagram in the problem outline
		# lr - lower right vertical line on display. corresponds to 'f' in the diagram in the problem outline

		# we can deduce lr and ur from 1, which has a code with two letters in it
		one_index = lens.index(2)
		ur_and_lr = cur_input[one_index]

		# we can deduce top from 7, which has a code with three letters, two we already know from 1:
		seven_idx = lens.index(3)
		top = find_diff(ur_and_lr, cur_input[seven_idx])[0]

		# we can deduce bot by first finding out what the pair of mid and ul are from 4
		four_idx = lens.index(4)
		four = cur_input[four_idx]
		mid_and_ul = "".join(find_diff(ur_and_lr, cur_input[four_idx]))

		# now, we can use our already deduced locations to find bot using 9
		for i in cur_input:
			if len(find_diff(top + ur_and_lr + mid_and_ul, i)) == 1 and len(i) == 6:  # only 9 evaluates to True here
				bot = find_diff(top + ur_and_lr + mid_and_ul, i)[0]
				nine = i

		eight_idx = lens.index(7)
		eight = cur_input[eight_idx]

		# since 8 and 9 only have one code letter different, we can figure out ll by finding that one letter not present
		# in 9.
		ll = find_diff(eight, nine)[0]

		# now we are going to find mid, lr, ul, and ur all by finding the difference between 8, which has 7 characters,
		# and 0 and 6, which both have 6 characters that are one different from each other.
		for i in cur_input:
			if len(i) == 6:
				diff = "".join(find_diff(eight, i))
				if diff in mid_and_ul:   # this case finds which code is 0, which is the same as 8 except it has no mid section.
					mid = diff           # this lets us find mid
					ul = "".join(find_diff(mid, mid_and_ul))    # since we know mid, we can now find ul since we already
																# knew what the combo of mid and ul was
				elif diff in ur_and_lr:  # we use the fact we know which the two rightmost character codes are to find ur
					ur = diff
					lr = "".join(find_diff(ur, ur_and_lr))

		show_codes = False
		if show_codes:
			print(f"top: {top}")
			print(f"bot: {bot}")
			print(f"mid: {mid}")
			print(f"ul: {ul}")
			print(f"ur: {ur}")
			print(f"ll: {ll}")
			print(f"lr: {lr}")

		# we already technically know some of these codes but let's rebuild each using our deduced values anyway for fun
		zero = top + bot + ul + ll + ur + lr
		one = ur + lr
		two = top + mid + bot + ur + ll
		three = top + mid + bot + ur + lr
		four = ul + ur + mid + lr
		five = top + mid + bot + ul + lr
		six = top + mid + bot + ul + ll + lr
		seven = top + ur + lr
		eight = top + mid + bot + ul + ll + ur + lr
		nine = top + mid + bot + ul + ur + lr

		num_codes = [zero, one, two, three, four, five, six, seven, eight, nine]
		num_codes = ["".join(sorted(i)) for i in num_codes]

		cur_output = [i[1].split() for i in lines][idx]

		code = []
		for word in cur_output:
			word = "".join(sorted(word))
			code.append(str(num_codes.index(word)))
		output_codes.append(code)

	output_codes = [int("".join(i)) for i in output_codes]
	# print(output_codes)
	print(sum(output_codes))
