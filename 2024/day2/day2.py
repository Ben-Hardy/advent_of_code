
def is_safe(nums):
	diffs = [abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]
	return set(diffs) <= {1, 2, 3} or set(diffs) <= {-1, -2, -3}


def is_ascending(nums):
	return sorted(nums) == nums


def is_descending(nums):
	return sorted(nums, reverse=True) == nums


def assess_line(line):
	nums = list(map(int, line.split()))
	return (is_ascending(nums) or is_descending(nums)) and is_safe(nums)
		

with open('input/input.txt', 'r') as f:
	lines = f.read().split('\n')
	
	result = list(map(assess_line, lines))
	print(result)
	print(sum(result))
	