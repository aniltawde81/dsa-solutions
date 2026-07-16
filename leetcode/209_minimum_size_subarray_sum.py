target = 7
nums = [2, 3, 1, 2, 4, 3]

left = 0
current_sum = 0
minimum = float("inf")

for right in range(len(nums)):
    current_sum += nums[right]

    while current_sum >= target:
        minimum = min(minimum, right - left + 1)
        current_sum -= nums[left]
        left += 1

if minimum == float("inf"):
    print(0)
else:
    print(minimum)
