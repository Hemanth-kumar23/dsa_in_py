class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyll:

    def __init__(self):
        self.head = None
# travesal forward 
    def print_ll(self):
        if self.head is None:
            print("ddl is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data ,"->",end = " ")
                n = n.nref

# travesal backward
    def print_ll_revrse(self):
        if self.head is None :
            print("ll is empty ")
        else:
            n = self.head
            while n.nref is not None:
                n = n.ref 
            while n is not None:
                print(n.data,"->",end = " ")
                n = n.pref

    
ddl = doublyll()
ddl.print_ll() 