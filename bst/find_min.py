class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)

current = root

while current.left:
    current = current.left

print(current.data)
