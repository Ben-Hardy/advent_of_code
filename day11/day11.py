import numpy as np


def calculate_flashes(filename: str, num_steps: int):
	with open(filename, 'r') as f:
		lines = f.read().split('\n')[:-1]
		f.close()
		lines = [[int(i) for i in row] for row in lines]

		octopi = np.array(lines, dtype=int)

		print("Before any steps")
		print(octopi)

		# bust out the edge coordinates like in part 9.
		top = 0
		bottom = octopi.shape[0] - 1
		left = 0
		right = octopi.shape[1] - 1

		total_flashes = 0
		for step in range(num_steps):
			octopi += 1
			already_flashed = []
			did_flash = True

			while did_flash:
				did_flash = False

				# I really should just write a class for this since it's gonna be messy
				# my solution here really emphasizes that I've done an image processing class
				# since we had to solve problems like this a dozen times
				for i in range(octopi.shape[0]):
					for j in range(octopi.shape[1]):
						if octopi[i, j] > 9 and not (i, j) in already_flashed:
							did_flash = True
							already_flashed.append((i, j))

							# corner cases:
							if i == top and j == left:  # top left corner
								octopi[i, j + 1] += 1
								octopi[i + 1, j + 1] += 1
								octopi[i + 1, j] += 1
							elif i == top and j == right:  # top right corner
								octopi[i, j - 1] += 1
								octopi[i + 1, j - 1] += 1
								octopi[i + 1, j] += 1
							elif i == bottom and j == left:  # bottom left corner
								octopi[i, j + 1] += 1
								octopi[i - 1, j + 1] += 1
								octopi[i - 1, j] += 1
							elif i == bottom and j == right:  # bottom right corner
								octopi[i, j - 1] += 1
								octopi[i - 1, j - 1] += 1
								octopi[i - 1, j] += 1
							# edge cases: HA THE EDGE CASE JOKE HAS RETURNED
							elif i == top:
								octopi[i, j - 1] += 1
								octopi[i, j + 1] += 1
								octopi[i + 1, j - 1] += 1
								octopi[i + 1, j + 1] += 1
								octopi[i + 1, j] += 1
							elif i == bottom:
								octopi[i, j - 1] += 1
								octopi[i, j + 1] += 1
								octopi[i - 1, j - 1] += 1
								octopi[i - 1, j + 1] += 1
								octopi[i - 1, j] += 1
							elif j == left:
								octopi[i + 1, j] += 1
								octopi[i - 1, j] += 1
								octopi[i + 1, j + 1] += 1
								octopi[i - 1, j + 1] += 1
								octopi[i, j + 1] += 1
							elif j == right:
								octopi[i + 1, j] += 1
								octopi[i - 1, j] += 1
								octopi[i + 1, j - 1] += 1
								octopi[i - 1, j - 1] += 1
								octopi[i, j - 1] += 1
									# the general case
							else:   # gonna do this clockwise
								octopi[i - 1, j] += 1
								octopi[i - 1, j + 1] += 1
								octopi[i, j + 1] += 1
								octopi[i + 1, j + 1] += 1
								octopi[i + 1, j] += 1
								octopi[i + 1, j - 1] += 1
								octopi[i, j - 1] += 1
								octopi[i - 1, j - 1] += 1
			
			# zero out everything bigger than 9
			for i in range(octopi.shape[0]):
				for j in range(octopi.shape[1]):
					if octopi[i, j] > 9:
						octopi[i, j] = 0
			
			show_steps = True
			
			if show_steps:
				if step % 10 == 0:
					print(f"After step {step}")
					print(octopi)
					print(f"Total flashes: {total_flashes}")
			total_flashes += len(already_flashed)
			
		print(total_flashes)


if __name__ == '__main__':
	calculate_flashes('input.txt', 100)
