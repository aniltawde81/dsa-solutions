from collections import deque

grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

queue = deque()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            queue.append((i, j))

print(list(queue))
