candies = [2, 3, 5, 1, 3]
extraCandies = 3

maximum = max(candies)

result = []

for candy in candies:
    result.append(candy + extraCandies >= maximum)

print(result)
