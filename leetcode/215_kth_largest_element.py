import heapq

nums = [3, 2, 1, 5, 6, 4]
k = 2

result = heapq.nlargest(k, nums)

print(result[-1])
