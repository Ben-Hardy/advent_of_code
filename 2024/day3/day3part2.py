import re


def find_mul(in_str):
	return sum(list(map(lambda x: x[0] * x[1], [list(map(int, i[4:-1].split(','))) for i in re.findall(r'mul\(\d+\,\d+\)', in_str)])))


def process_str(line):
	return sum([find_mul(i.split('don\'t')[0]) for i in line.split('do()')])


with open('input/input.txt', 'r') as f:
	print(process_str(f.read()))
