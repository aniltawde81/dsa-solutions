class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

target = 20
current = head

while current:
    if current.data == target:
        print("Found")
        break
    current = current.next
