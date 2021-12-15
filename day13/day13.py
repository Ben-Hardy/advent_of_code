from collections import deque
import numpy as np


def fold(fold_instructions, paper, old_x, old_y):
	
	if fold_instructions[0] == 'y':
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
		
		for point in points_below_fold:
			dist_from_fold = abs(fold_instructions[1] - point[0])
			point[0] = fold_instructions[1] - dist_from_fold
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
		for y in range(paper.shape[0]):
			for x in range(fold_instructions[1], paper.shape[1]):
				if paper[y, x] == 1:
					points_after_fold.append([y, x])
		
		for point in points_after_fold:
			dist_from_fold = abs(fold_instructions[1] - point[1])
			point[1] = fold_instructions[1] - dist_from_fold
		
		new_paper = np.zeros((old_y + 1, old_x - (old_x - fold_instructions[1])), dtype=int)
		print(new_paper.shape)
		for point in points_before_fold:
			new_paper[point[0], point[1]] = 1
		
		for point in points_after_fold:
			new_paper[point[0], point[1]] = 1
		
		return new_paper


with open('input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	
	folds_start = -1
	
	points_to_mark = deque()  # I just read about these, let's try them out
	for i in range(len(lines)):
		if lines[i] == '':
			folds_start = i + 1
			break
		else:
			c, r = lines[i].split(',')
			points_to_mark.append([int(c), int(r)])
	# print(points_to_mark)
	dim_y = max([i[0] for i in points_to_mark])
	dim_x = max([i[1] for i in points_to_mark])
	cur_paper = np.zeros((dim_x + 1, dim_y + 1), dtype=int)

	for p in points_to_mark:
		cur_paper[p[1], p[0]] = 1
		
	folds = deque()
	
	for i in range(folds_start, len(lines)):
		direction, along = lines[i].split('=')
		direction = direction.split()[-1]
		folds.append((direction, int(along)))
	
	for fol in folds:
		cur_paper = fold(fol, cur_paper, cur_paper.shape[0], cur_paper.shape[1])
	
	# for part 1
	# print(np.sum(cur_paper))
	
	# for part 2
	for r in range(cur_paper.shape[0]):
		row = "["
		for c in range(cur_paper.shape[1]):
			row += " " + str(cur_paper[r, c])
		print(row + ']')
