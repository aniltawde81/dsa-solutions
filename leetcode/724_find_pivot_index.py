nums = [1, 7, 3, 6, 5, 6]

total = sum(nums)
left_sum = 0

for i in range(len(nums)):
    if left_sum == total - left_sum - nums[i]:
        print(i)
        break

    left_sum += nums[i]
