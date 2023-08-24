class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addStart(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def display(self):
        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data)
            current = current.next

ll = LinkedList()
# ll.addStart(1)
# ll.addStart(1)
# ll.addStart(1)
# ll.addStart(2)
ll.display()
