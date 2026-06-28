from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

visited = set()
queue = deque(["A"])

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            queue.append(neighbor)
