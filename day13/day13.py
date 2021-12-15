from collections import deque
import numpy as np


def fold(fold_instructions, paper, old_x, old_y):
	#print(fold_instructions)
	
	if fold_instructions[0] == 'y' and fold_instructions[1] >= old_x//2:
		points_below_fold = deque()
		points_above_fold = deque()
		for y in range(0, fold_instructions[1]):
			for x in range(paper.shape[1]):
				if paper[y, x] == 1:
					points_above_fold.append([y, x])
		
		for y in range(fold_instructions[1], paper.shape[0]):
			for x in range(paper.shape[1]):
				if paper[y, x] == 1:
					points_below_fold.append([y, x])
		#print(points_below_fold)
		
		for point in points_below_fold:
			dist_from_fold = abs(fold_instructions[1] - point[0])
			point[0] = fold_instructions[1] - dist_from_fold
		#print(points_below_fold)
		new_paper = np.zeros((old_x - fold_instructions[1], old_y + 1), dtype=int)
		
		for point in points_below_fold:
			new_paper[point[0], point[1]] = 1
		
		for point in points_above_fold:
			new_paper[point[0], point[1]] = 1
		
		return new_paper
	elif fold_instructions[0] == 'y' and fold_instructions[1] < old_x//2:
		points_below_fold = deque()
		points_above_fold = deque()
		for y in range(0, fold_instructions[1]):
			for x in range(paper.shape[1]):
				if paper[y, x] == 1:
					points_above_fold.append([y, x])
		
		for y in range(fold_instructions[1], paper.shape[0]):
			for x in range(paper.shape[1]):
				if paper[y, x] == 1:
					points_below_fold.append([y, x])
		print(points_above_fold)
		for point in points_above_fold:
			original_value = point[0]
			point[0] = fold_instructions[1] + (fold_instructions[1] - point[0])
			
		print(points_above_fold)
		print(points_below_fold)
		new_paper = np.zeros((old_x - fold_instructions[1], old_y + 1), dtype=int)
		
		for point in points_below_fold:
			new_paper[point[0], point[1]] = 1
		
		for point in points_above_fold:
			new_paper[point[0], point[1]] = 1
		
		return new_paper
	
	elif fold_instructions[0] == 'x':
		points_before_fold = deque()
		points_after_fold = deque()
		
		for y in range(paper.shape[0]):
			for x in range(0, fold_instructions[1]):
				if paper[y, x] == 1:
					points_before_fold.append([y, x])
		print(points_before_fold)
		for y in range(paper.shape[0]):
			for x in range(fold_instructions[1], paper.shape[1]):
				if paper[y, x] == 1:
					points_after_fold.append([y, x])
		
		
		for point in points_after_fold:
			dist_from_fold = abs(fold_instructions[1] - point[1])
			point[1] = fold_instructions[1] - dist_from_fold
		
		new_paper = np.zeros((old_y + 1, old_x - fold_instructions[1]), dtype=int)
		print(new_paper.shape)
		for point in points_before_fold:
			new_paper[point[0], point[1]] = 1
		
		for point in points_after_fold:
			new_paper[point[0], point[1]] = 1
		
		return new_paper


with open('input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	
	folds_start = -1
	
	points_to_mark = deque() # I just read about these, let's try them out
	for i in range(len(lines)):
		if lines[i] == '':
			folds_start = i + 1
			break
		else:
			x, y = lines[i].split(',')
			points_to_mark.append([int(x),int(y)])
	# print(points_to_mark)
	dim_y = max([i[0] for i in points_to_mark])
	dim_x = max([i[1] for i in points_to_mark])
	starting_paper = np.zeros((dim_x + 1, dim_y + 1), dtype=int)

	for point in points_to_mark:
		starting_paper[point[1], point[0]] = 1
		
	# print(starting_paper)
	
	folds = deque()
	
	for i in range(folds_start, len(lines)):
		direction, along = lines[i].split('=')
		direction = direction.split()[-1]
		folds.append((direction, int(along)))
	
	finished_paper = fold(folds[0], starting_paper, dim_x, dim_y)
	print(sum(finished_paper))
