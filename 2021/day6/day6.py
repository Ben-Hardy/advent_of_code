import time


# this one seems way easier than the last couple days????
def lantern_fish_calc(filename, num_days):
	tic = time.perf_counter()
	with open(filename, 'r') as f:
		current_state = f.read().split('\n')[0]
		f.close()
		print(f"Initial state: {current_state}")
		day_count = 0
		state_list = [int(num) for num in current_state.split(',')]
		while day_count < num_days:
			# state_list = [int(num) for num in current_state.split(',')]
			to_append = 0
			for j in range(len(state_list)):
				if state_list[j] == 0:
					state_list[j] = 6
					to_append += 1
				else:
					state_list[j] -= 1

			for _ in range(to_append):
				state_list.append(8)

			day_count += 1
			# current_state = ','.join([str(j) for j in state_list])
			# print(f"After {day_count: >2} days: {current_state}")

		print(len(state_list))
	toc = time.perf_counter()

	print(f"total time: {toc - tic}")


lantern_fish_calc('input.txt', 80)
