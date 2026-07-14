nums = [1, 2, 3, 4]

result = []

for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
        if i != j:
            product *= nums[j]
    result.append(product)

print(result)
