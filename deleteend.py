class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linkedList :

    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is emty")
        else:
            n = self.head 
            while n is not None:
                print(n.data)
                n = n.ref
    
    def add_beg(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None :
                n = n.ref
    
    def add_after(self,data,x):
        n = self.head
        while n is not None :
          if n.data == x:
              new_node = Node(data)
              new_node.ref = n.ref
              n.ref = new_node
              return
          n = n.ref

    def delete_beg(self):
        if self.head is None :
            print("the ll is emtyp so we can't delete anything ")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("the ll is emtyp so we can't delete anything ")
        else:
            n = self.head 
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None


ll1=linkedList()
ll1.add_beg(100)
ll1.add_after(200,100)
ll1.delete_end()
ll1.print_ll()
