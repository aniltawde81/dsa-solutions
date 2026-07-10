nums = [1, 3, 5, 6]
target = 2

left = 0
right = len(nums)

while left < right:
    mid = (left + right) // 2

    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid

print(left)
