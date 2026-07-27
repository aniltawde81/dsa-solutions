from itertools import combinations

nums = [1, 2, 3]

result = [[]]

for r in range(1, len(nums) + 1):
    for subset in combinations(nums, r):
        result.append(list(subset))

print(result)
