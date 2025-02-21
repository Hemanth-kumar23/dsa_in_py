class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linkedList is empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" -> ")  # Print node data
                n = n.ref
            print("None")

    def add_begn(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

ll1 = LinkedList()
ll1.add_begn(10)
ll1.add_end(20)
ll1.print_ll()
