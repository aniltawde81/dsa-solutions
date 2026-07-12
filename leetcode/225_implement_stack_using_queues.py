from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print("Top:", stack[-1])

stack.pop()

print("After Pop:", list(stack))
