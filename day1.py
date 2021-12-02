f = open("input.txt", "r")

nums = [int(i) for i in f.read().split('\n')[:-1]]

print(sum([1 if nums[i] < nums[i+1] else 0 for i in range(len(nums) - 1)]))


