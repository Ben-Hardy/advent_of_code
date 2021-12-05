f = open("input.txt", "r")

nums = [int(i) for i in f.read().split('\n')[:-1]]

# each entry in this list will be a window sum for a given 3 entry range of values. 
# once this is created it's simply a case of repeating part 1 to create a list of
# binary values representing whether a window sum is smaller than its successor or not
window_sums = [nums[i] + nums[i+1] + nums[i+2] for i in range(len(nums)  - 2)]

increases_sum = sum([1 if window_sums[i] < window_sums[i+1] else 0 for i in range(len(window_sums) - 1)])

print(increases_sum)