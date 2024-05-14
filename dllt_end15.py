class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating the nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Setting the head of the list
head = node1

# Deleting node at the end
current = head
while current.next.next is not None:
    current = current.next
current.next = None

# To verify, let's print the linked list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")