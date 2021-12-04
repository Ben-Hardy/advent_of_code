f = open("input.txt", "r")

nums = f.read().split('\n')[:-1]

num_rows = len(nums)
num_cols = len(nums[0])

col_counts = [0 for i in range(num_cols)]

for num in nums:
	for i in range(num_cols):
		if num[i] == '1':
			col_counts[i] += 1

gamma = []
epsilon = []

for col_count in col_counts:
	if col_count > num_rows - col_count:
		gamma.append('1')
		epsilon.append('0')
	else:
		gamma.append('0')
		epsilon.append('1')

gamma_str = ''.join(gamma)
eps_str = ''.join(epsilon)

gamma_int = int(gamma_str, 2)
eps_int = int(eps_str, 2)

print(gamma_int * eps_int)

# part 2: doing this in the same file to avoid just copying and pasting most of part 1

def count_col(l, idx):
	total = 0
	for i in l:
		if i[idx] == '1':
			total += 1
	return total

ox_rating = nums.copy()
co2_rating = nums.copy()

cur = count_col(ox_rating, 0)

cur_col = 0

while len(ox_rating) != 1:
	cur = count_col(ox_rating, cur_col)
	if cur > len(ox_rating) - cur:
		ox_rating = [i for i in ox_rating if i[cur_col] == '1']
	elif cur < len(ox_rating) - cur:
		ox_rating = [i for i in ox_rating if i[cur_col] == '0']
	else:
		ox_rating = [i for i in ox_rating if i[cur_col] == '1']

	cur_col += 1

cur_col = 0

while len(co2_rating) != 1:
	cur = count_col(co2_rating, cur_col)
	if cur > len(co2_rating) - cur:
		co2_rating = [i for i in co2_rating if i[cur_col] == '0']
	elif cur < len(co2_rating) - cur:
		co2_rating = [i for i in co2_rating if i[cur_col] == '1']
	else:
		co2_rating = [i for i in co2_rating if i[cur_col] == '0']

	cur_col += 1

co2_rating_int = int(co2_rating[0],2)
ox_rating_int = int(ox_rating[0], 2)

print(co2_rating_int * ox_rating_int)

