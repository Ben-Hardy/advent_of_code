f = open("input.txt", "r")

nums = [int(i) for i in f.read().split('\n')[:-1]]

window_sums = [nums[i] + nums[i+1] + nums[i+2] for i in range(len(nums)  - 2)]

print(sum([1 if window_sums[i] < window_sums[i+1] else 0 for i in range(len(window_sums) - 1)]))