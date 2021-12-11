import numpy as np


def calculate_flashes(filename: str):
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
		
		did_sync_flash = False
		day_count = 0
		while not did_sync_flash:
			octopi += 1
			already_flashed = []
			did_flash = True
			
			while did_flash:
				did_flash = False
				
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
							elif i == top and j == right:
								octopi[i, j - 1] += 1
								octopi[i + 1, j - 1] += 1
								octopi[i + 1, j] += 1
							elif i == bottom and j == left:
								octopi[i, j + 1] += 1
								octopi[i - 1, j + 1] += 1
								octopi[i - 1, j] += 1
							elif i == bottom and j == right:
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
							else:  # gonna do this clockwise
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
			
			if len(already_flashed) == 100:
				did_sync_flash = True
			
			day_count += 1
		
		print(day_count)


if __name__ == '__main__':
	calculate_flashes('input.txt')
