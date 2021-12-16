# can't brute force it, like that lanternfish question. maybe follow the same approach as that one?

# I ended up looking up to see what a few others did to get a rough idea of whether my idea for
# a solution would work or not. I was like 99% of the way there but missed one small thing.

with open('input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	f.close()
starting_polymer = lines[0]

lines = lines[2:]
lines = [i.split(' -> ') for i in lines]

insertions = {i[0]: i[1] for i in lines}

polymers = {i: 0 for i in insertions.keys()}

counts = {i: 0 for i in insertions.values()}

for i in range(len(starting_polymer) - 1):
	polymers[starting_polymer[i: i + 2]] += 1

for i in range(len(starting_polymer)):
	counts[starting_polymer[i]] += 1

steps = 40

for step in range(steps):
	cur_polymer = polymers.copy()
	
	for key in polymers:
		if polymers[key] > 0:
			cur_polymer[key[0] + insertions[key]] += polymers[key]
			cur_polymer[insertions[key] + key[1]] += polymers[key]
			cur_polymer[key] -= polymers[key]
			counts[insertions[key]] += polymers[key]
		
	polymers = cur_polymer.copy()
	
print(max(counts.values()) - min(counts.values()))
