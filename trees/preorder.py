class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)

preorder(root)
