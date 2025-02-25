# Defining a Stack class
class Stack:
    # Constructor to initialize the stack
    def __init__(self, maxsize):
        self.maxsize = maxsize  # Maximum size of stack
        self.top = -1           # Stack starts empty (-1 means no elements)
        self.list = []          # List to store stack elements

    # Method to check if the stack is empty
    def is_empty(self):
        return self.top == -1

    # Method to check if the stack is full
    def is_full(self):
        return self.top == self.maxsize - 1

    # Method to insert an element into the stack
    def push(self, value):
        if self.is_full():  # Check if stack is full before inserting
            print("Stack is full")
        else:
            self.list.append(value)  # Add value to stack
            self.top += 1            # Increase the top pointer
            print(value, "has been inserted")

    # Method to remove an element from the stack
    def pop(self):
        if self.is_empty():  # Check if stack is empty before removing
            print("The stack is empty")
        else:
            popped_item = self.list.pop()  # Remove last element
            self.top -= 1                  # Decrease the top pointer
            print("Popped item =", popped_item)

    # Method to display stack contents
    def display(self):
        if self.is_empty():  # Check if stack is empty before displaying
            print("The stack is empty")
        else:
            print("Contents of the stack are:", self.list)

# Creating a Stack object with a maximum size of 4
s = Stack(4)

# Performing stack operations
s.push(10)   # Insert 10
s.push(20)   # Insert 20
s.push(30)   # Insert 30
s.display()  # Show stack contents
s.pop()      # Remove top element (30)
s.pop()      # Remove top element (20)
s.display()  # Show remaining stack contents
