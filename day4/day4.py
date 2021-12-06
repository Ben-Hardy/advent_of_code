import numpy as np
import unittest

from numpy.testing._private.utils import assert_equal


class Bingo:
	def __init__(self, input_board):
		self.bingo_board = np.array(input_board)
		self.mask = np.zeros((5, 5), dtype=int)

	def check_win(self):
		for i in range(5):
			if np.sum(np.sum(self.mask[i, :])) == 5 or np.sum(np.sum(self.mask[:, i])) == 5:
				return True

		return False

	def dab(self, i, j):
		self.mask[i, j] = 1

	def contains(self, called_value):
		return called_value in self.bingo_board

	def find_loc(self, called_value):
		for i in range(5):
			for j in range(5):
				if self.bingo_board[i][j] == called_value:
					return i, j
		return None  # this won't happen because this function will only be called if we know the called value

	# is on the bingo card

	def assess_called_value(self, called_value):
		if self.contains(called_value):
			location = self.find_loc(called_value)
			self.dab(location[0], location[1])

	def calculate_score(self, called_value):
		cumulative_total = 0

		for i in range(5):
			for j in range(5):
				if self.mask[i][j] == 0:
					cumulative_total += self.bingo_board[i][j]

		return cumulative_total * called_value


class TestBingo(unittest.TestCase):
	def test_check_win(self):
		b = Bingo(None)  # we don't care about the contents of bingo_board for this test

		# test vertical win detection
		b.mask[:, 1] = 1
		assert_equal(True, b.check_win())

		b.mask[:, 1] = 0

		# test horizontal win detection
		b.mask[1, :] = 1
		assert_equal(True, b.check_win())

	def test_check_contains(self):
		b = Bingo([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
		assert_equal(False, b.contains(26))
		assert_equal(True, b.contains(25))

	def test_find_loc(self):
		b = Bingo([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
		assert_equal((2, 2), b.find_loc(13))

	def test_assess_called_value(self):
		b = Bingo([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
		b.assess_called_value(13)
		assert_equal(1, b.mask[2, 2])

		b.assess_called_value(8)
		b.assess_called_value(3)
		b.assess_called_value(18)
		b.assess_called_value(23)
		assert_equal(1, b.mask[0, 2])
		assert_equal(1, b.mask[1, 2])
		assert_equal(1, b.mask[3, 2])
		assert_equal(1, b.mask[4, 2])
		assert_equal(True, b.check_win())

	def test_calculate_score(self):
		# uncomment this if you want to run the tests on the given example values from the problem.
		# I needed it to debug an issue
		"""
		f = open('small_input.txt.txt', 'r')
		input_vals = f.read()
		f.close()
		numbers_to_call = [int(i) for i in input_vals.split('\n')[0].split(',')]
		#print(calls)

		boards = [[int(j) for j in i.split()] for i in input_vals.split('\n')[2:] if i]
		boards = [boards[i:i+5] for i in range(0, len(boards), 5)]

		bingo_cards = []
		for board in boards:
			bingo_cards.append(Bingo(board))

		for card in bingo_cards:
			print(card.bingo_board)

		is_won = False
		winner = -1
		winning_call = -1
		print(len(bingo_cards))
		for num in numbers_to_call:
			for i in range(len(bingo_cards)):
				bingo_cards[i].assess_called_value(num)

				if bingo_cards[i].check_win() == True:
					winner = i
					is_won = True
					winning_call = num
					break

			print("current status:")
			print(bingo_cards[0].mask)
			print(bingo_cards[1].mask)
			print(bingo_cards[2].mask)
			input("press enter to continue")

			if is_won == True:
				break

		print(f"winner: {winner}")
		print(f"winning call: {winning_call}")
		print(f"winning board: {bingo_cards[winner].bingo_board}")
		print(f"winning marked off squares: {bingo_cards[winner].mask}")
		print(f"score: {bingo_cards[winner].calculate_score(winning_call)}")
		"""
		b = Bingo([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
		b.assess_called_value(8)
		b.assess_called_value(13)
		b.assess_called_value(3)
		b.assess_called_value(18)
		b.assess_called_value(23)
		assert_equal(True, b.check_win())


if __name__ == '__main__':

	# unittest.main()

	with open("input.txt", "r") as f:
		numbers_to_call = [int(i) for i in f.readline().split(',')]

		boards = [[int(j) for j in i.split()] for i in f.read().split('\n') if i]
		f.close()

		boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]

		bingo_cards = []
		for board in boards:
			bingo_cards.append(Bingo(board))

		is_won = False
		winner = -1
		winning_call = -1
		for num in numbers_to_call:
			for i in range(len(bingo_cards)):
				bingo_cards[i].assess_called_value(num)

				if bingo_cards[i].check_win():
					winner = i
					is_won = True
					winning_call = num
					break

			if is_won:
				break

		print(f"winner: {winner}")
		print(f"winning call: {winning_call}")
		print(f"winning board: {bingo_cards[winner].bingo_board}")
		print(f"winning marked off squares: {bingo_cards[winner].mask}")
		print(f"score: {bingo_cards[winner].calculate_score(winning_call)}")
