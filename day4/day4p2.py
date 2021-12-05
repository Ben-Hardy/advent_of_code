
# our bingo class from part 1 will still be fine for this
from day4 import Bingo

with open("input.txt", "r") as f:
	numbers_to_call = [int(i) for i in f.readline().split(',')]
	
	boards = [[int(j) for j in i.split()] for i in f.read().split('\n') if i]
	f.close()

	boards = [boards[i:i+5] for i in range(0, len(boards), 5)]
	
	bingo_cards = []
	for board in boards:
		bingo_cards.append(Bingo(board))

	is_won = False
	winner = -1
	winning_call = -1
	mark_pruned = [False for i in range(len(boards))]
	for num in numbers_to_call:
		for i in range(len(bingo_cards)):
			bingo_cards[i].assess_called_value(num)

			if bingo_cards[i].check_win():
				mark_pruned[i] = True
				if len(boards) - sum(mark_pruned) == 1:
					cur_num = num
					is_won = True
					break
		
		if is_won:
			break
	
	worst_board = mark_pruned.index(False)
	remaining_numbers = numbers_to_call[numbers_to_call.index(cur_num):]

	winning_num = -1
	for num in remaining_numbers:
		bingo_cards[worst_board].assess_called_value(num)

		if bingo_cards[worst_board].check_win():
			winning_num = num
			break
	
	print(bingo_cards[worst_board].calculate_score(winning_num))
	
	


