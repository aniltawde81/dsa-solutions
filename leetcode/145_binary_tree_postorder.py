class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

postorder(root)
