stack1 = []
stack2 = []

stack1.append(10)
stack1.append(20)
stack1.append(30)

while stack1:
    stack2.append(stack1.pop())

print("Front:", stack2[-1])

stack2.pop()

print("Queue:", stack2)
