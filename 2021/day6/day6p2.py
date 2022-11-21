# can't just brute force it for bigger values of days. time to actually figure this out


def lantern_fish_calc(filename, num_days):

	with open(filename, 'r') as f:
		fish_list = [int(i) for i in f.read().split(',')]
		days = [0] * 9 # keep a count of the number of fish on each day

		# tally the number of fish with each day
		for i in fish_list:
			days[i] += 1

		for day in range(num_days):
			today_zeros = days[0]
			for i in range(1,len(days)):
				days[i - 1] = days[i]
			days[6] += today_zeros
			days[8] = today_zeros

		print(sum(days))


lantern_fish_calc("input.txt", 256)
