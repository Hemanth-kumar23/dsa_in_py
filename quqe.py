class Queue:
    def __init__(self):
        self.queue_ds = []
        self.Front = -1
        self.Rear = -1

    def enqueue(self, val):
        self.queue_ds.append(val)
        if self.Front == -1:
            self.Front = 0
        self.Rear += 1

    def dequeue(self):
        if len(self.queue_ds) == 0:
            print("Queue is empty")
            return None
        temp = self.queue_ds.pop(0)  # Remove front element
        self.Rear -= 1
        if len(self.queue_ds) == 0:  # Reset if queue is empty
            self.Front = -1
            self.Rear = -1
        return temp

    def display(self):
        if len(self.queue_ds) == 0:
            print("Queue is empty")
            return
        print("The Queue:")
        for i in range(len(self.queue_ds)):
            if i == 0:
                print(self.queue_ds[i], "<== FRONT")
            elif i == len(self.queue_ds) - 1:
                print(self.queue_ds[i], "<== REAR")
            else:
                print(self.queue_ds[i])
        print("The Queue Ends")


# Main Program
a = Queue()

while True:
    print("************************")
    option = int(input("Enter your choice\n1. Insert\n2. Delete\n3. Display\n4. Exit\n"))

    if option == 1:
        value = int(input("Enter the value you want to add: "))
        a.enqueue(value)
    elif option == 2:
        a.dequeue()
    elif option == 3:
        a.display()
    elif option == 4:
        print("Exiting...")
        break
    else:
        print("Wrong option")
