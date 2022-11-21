with open('input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	f.close()

positions = [int(i.split(' ')[-1]) for i in lines]


class Dice:
	def __init__(self):
		self.counter = 1
		self.roll_count = 0
		
	def roll(self):
		result = self.counter
		if self.counter == 100:
			self.counter = 1
		else:
			self.counter += 1
		
		self.roll_count += 1
		return result
	

class Player:
	def __init__(self, initial_location):
		self.loc = initial_location
		self.score = 0
		
	def move(self, num_spaces):
		self.loc += num_spaces
		if self.loc > 10:
			self.loc -= 10
		self.score += self.loc
		

player_1 = Player(positions[0])
player_2 = Player(positions[1])
dice = Dice()

while player_1.score < 1000 and player_2.score < 1000:
	rolls = [dice.roll() for _ in range(3)]
	roll = sum(rolls) % 10
	player_1.move(roll)
	
	if player_1.score >= 1000:
		break
	else:
		rolls = [dice.roll() for _ in range(3)]
		roll = sum(rolls) % 10
		player_2.move(roll)

print(f'player_1 score: {player_1.score}')
print(f'player_2 score: {player_2.score}')
print(f'number of rolls: {dice.roll_count}')
if player_1.score >= 1000:
	final_score = player_2.score * dice.roll_count
	
else:
	final_score = player_1.score * dice.roll_count
	
print(f'final score: {final_score}')
