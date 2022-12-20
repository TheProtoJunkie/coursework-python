
# linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # denotes lack of any value

# singly linked list(one directional)


class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node  # new tail
        print("appended new node with value:", node.next.value)

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return
        else:
            node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node  # new tail
        print("prepended new node with value:", node.next.value)


llist = linkedlist()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
