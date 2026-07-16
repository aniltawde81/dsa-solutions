nums = [1, 2, 3, 1]
k = 3

window = set()
left = 0

for right in range(len(nums)):
    if nums[right] in window:
        print(True)
        break

    window.add(nums[right])

    if len(window) > k:
        window.remove(nums[left])
        left += 1
else:
    print(False)
