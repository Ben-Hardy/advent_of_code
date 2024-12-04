import re


def find_mul(in_str):
	return sum(list(map(lambda x: x[0] * x[1], [list(map(int, i[4:-1].split(','))) for i in re.findall(r'mul\(\d+\,\d+\)', in_str)])))


with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')
	print(sum(list(map(find_mul, lines))))
