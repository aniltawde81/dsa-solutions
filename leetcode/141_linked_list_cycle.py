nums = [3, 2, 0, -4]

visited = set()
cycle = False

for num in nums:
    if num in visited:
        cycle = True
        break
    visited.add(num)

print(cycle)
