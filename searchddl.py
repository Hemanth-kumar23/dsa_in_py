class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  # Replacing 'next' with 'nref'
        self.pref = None  # Replacing 'prev' with 'pref'

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.nref = self.head
            self.head.pref = new_node
        self.head = new_node  # Update head

    # Forward traversal
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" <-> ")
                n = n.nref
            print("None")

    # Reverse traversal
    def print_LL_reverse(self):
        if self.head is None:
            print("DLL is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref  # Move to last node
            while n is not None:
                print(n.data, end=" <-> ")
                n = n.pref
            print("None")

    # Search for an element
    def search(self, key):
        n = self.head
        while n:
            if n.data == key:
                return True  # Found
            n = n.nref
        return False  # Not found

# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)

dll.print_LL()  # Forward traversal
dll.print_LL_reverse()  # Reverse traversal

# Searching
key = 20
print("Found" if dll.search(key) else "Not Found")  # Output: Found
