f = open("input.txt", "r")

nums = [int(i) for i in f.read().split('\n')[:-1]]

# a list of binary representing if a given number is smaller than the next one. summing the list gives us the total number of depth increases
increase_sum = sum([1 if nums[i] < nums[i+1] else 0 for i in range(len(nums) - 1)])

print(increase_sum)


