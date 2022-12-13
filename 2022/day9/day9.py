import unittest


def recalculate_tail(h_x, h_y, t_x, t_y):
	# head is 2 right of tail, on same y
	if h_x - t_x == 2 and h_y - t_y == 0:
		t_x += 1
	# head is 2 right of tail, head 1 up from tail
	elif h_x - t_x == 2 and h_y - t_y == 1:
		t_x += 1
		t_y += 1
	# head is 2 right of tail, head 1 down from tail
	elif h_x - t_x == 2 and t_y - h_y == 1:
		t_x += 1
		t_y -= 1
	# head is 2 left of tail, on same y
	elif t_x - h_x == 2 and h_y - t_y == 0:
		t_x -= 1
	# head is 2 left of tail, head 1 up from tail
	elif t_x - h_x == 2 and h_y - t_y == 1:
		t_x -= 1
		t_y += 1
	# head is 2 left of tail, head 1 down from tail
	elif t_x - h_x == 2 and t_y - h_y == 1:
		t_x -= 1
		t_y -= 1
	# head is 2 above tail, on same x
	elif h_x - t_x == 0 and h_y - t_y == 2:
		t_y += 1
	# head is 2 above tail, head one right of tail
	elif h_x - t_x == 1 and h_y - t_y == 2:
		t_y += 1
		t_x += 1
	# head is 2 above tail, head one left of tail
	elif t_x - h_x == 1 and h_y - t_y == 2:
		t_y += 1
		t_x -= 1
	# head is 2 below tail, on same x
	elif h_x - t_x == 0 and t_y - h_y == 2:
		t_y -= 1
	# head is 2 below tail, head right of tail
	elif h_x - t_x == 1 and t_y - h_y == 2:
		t_y -= 1
		t_x += 1
	# head is 2 below tail, head left of tail
	elif t_x - h_x == 1 and t_y - h_y == 2:
		t_y -= 1
		t_x -= 1

	return t_x, t_y


with open('input/input.txt', 'r') as f:
	lines = [i.split() for i in f.read().split('\n')]
	print(lines)

	VERBOSE = False
	head_x = 0
	head_y = 0

	tail_x = 0
	tail_y = 0

	visited_tail_locs = set()
	visited_tail_locs.add((0, 0))

	for line in lines:
		direction = line[0]
		to_move = int(line[1])
		print(line)
		for i in range(to_move):
			if direction == 'R':
				head_x += 1
			elif direction == 'L':
				head_x -= 1
			elif direction == 'U':
				head_y += 1
			elif direction == 'D':
				head_y -= 1

			tail_x, tail_y = recalculate_tail(head_x, head_y, tail_x, tail_y)
			visited_tail_locs.add((tail_x, tail_y))
			if VERBOSE:
				print(f"Current head location: {head_x}, {head_y}")
				print(f"Current tail location: {tail_x}, {tail_y}")
	# print(list(visited_tail_locs))
	print(len(list(visited_tail_locs)))


class Tests(unittest.TestCase):
	def test_tail_two_left(self):
		hx, hy = 3, 1
		tx, ty = 1, 1
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 1))

	def test_tail_two_left_one_up(self):
		hx, hy = 3, 3
		tx, ty = 1, 4
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_tail_two_left_one_down(self):
		hx, hy = 3, 3
		tx, ty = 1, 2
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_tail_two_right(self):
		hx, hy = 2, 2
		tx, ty = 4, 2
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (3, 2))

	def test_tail_two_right_one_up(self):
		hx, hy = 2, 2
		tx, ty = 4, 3
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (3, 2))

	def test_tail_two_up(self):
		hx, hy = 2, 4
		tx, ty = 2, 2
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_tail_two_up_one_left(self):
		hx, hy = 2, 2
		tx, ty = 1, 4
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_tail_two_up_one_right(self):
		hx, hy = 2, 2
		tx, ty = 3, 4
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_tail_two_down(self):
		hx, hy = 2, 2
		tx, ty = 2, 4
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_tail_two_down_one_left(self):
		hx, hy = 2, 2
		tx, ty = 1, 4
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_tail_two_down_one_right(self):
		hx, hy = 2, 2
		tx, ty = 3, 4
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))

	def test_adjacent(self):
		hx, hy = 2, 2
		tx, ty = 2, 3
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 3))
		tx, ty = 2, 1
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (2, 1))
		tx, ty = 1, 2
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (1, 2))
		tx, ty = 3, 2
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (3, 2))
		tx, ty = 1, 1
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (1, 1))
		tx, ty = 3, 3
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (3, 3))
		tx, ty = 1, 3
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (1, 3))
		tx, ty = 3, 1
		self.assertEqual(recalculate_tail(hx, hy, tx, ty), (3, 1))


if __name__ == '__main__':
	unittest.main()
