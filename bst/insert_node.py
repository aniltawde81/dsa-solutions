class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(10)
root.right = Node(30)

print(root.data)
