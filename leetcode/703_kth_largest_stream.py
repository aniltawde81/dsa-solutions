import heapq

nums = [4, 5, 8, 2]
k = 3

heap = nums[:]
heapq.heapify(heap)

while len(heap) > k:
    heapq.heappop(heap)

new_value = 10

if len(heap) < k:
    heapq.heappush(heap, new_value)
elif new_value > heap[0]:
    heapq.heapreplace(heap, new_value)

print(heap[0])
