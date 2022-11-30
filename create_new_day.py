import os


year = int(input("which year: "))
day = int(input("which day: "))

directory = f"{year}/day{day}"
input_dir = f"{directory}/input"

os.makedirs(directory)
os.makedirs(input_dir)

input_path = f"{input_dir}/input.txt"
small_input_path = f"{input_dir}/smallinput.txt"
day_part_one = f"{directory}/day{day}.py"
day_part_two = f"{directory}/day{day}part2.py"

with open(input_path, 'x') as f:
	print(f"{input_path} created!")
	f.close()
with open(small_input_path, 'x') as f:
	print(f"{small_input_path} created!")
	f.close()
with open(day_part_one, 'x') as f:
	print(f"{day_part_one} created!")
	f.close()
with open(day_part_two, 'x') as f:
	print(f"{day_part_two} created!")
	f.close()
