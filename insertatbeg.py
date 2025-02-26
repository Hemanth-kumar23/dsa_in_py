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

    def delete_beg(self):
        if self.head is None :
            print("the ll is emtyp so we can't delete anything ")
        else:
            self.head = self.head.ref  

ll1 = LinkedList()
ll1.add_begn(10)
ll1.add_begn(20)
ll1.delete_beg()
ll1.print_ll()
