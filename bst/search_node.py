class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

root = Node(20)
root.left = Node(10)
root.right = Node(30)

print(search(root, 10))
