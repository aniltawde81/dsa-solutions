nums = [1, 1, 2, 2, 3]

result = []

for num in nums:
    if num not in result:
        result.append(num)

print(result)
