import heapq

stones = [2, 7, 4, 1, 8, 1]

stones = [-stone for stone in stones]
heapq.heapify(stones)

while len(stones) > 1:
    first = -heapq.heappop(stones)
    second = -heapq.heappop(stones)

    if first != second:
        heapq.heappush(stones, -(first - second))

print(-stones[0] if stones else 0)
