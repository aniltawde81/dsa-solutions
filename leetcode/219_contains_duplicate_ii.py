nums = [1, 2, 3, 1]
k = 3

index_map = {}
found = False

for i, num in enumerate(nums):
    if num in index_map and i - index_map[num] <= k:
        found = True
        break
    index_map[num] = i

print(found)
