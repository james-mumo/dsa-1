class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addStart(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def reverseList(self):
        if self.head is None:
            print("It's impossible")
        else:
            prev = None
            current = self.head
            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            self.head = prev


    def display(self):
        if self.head is None:
            print("Empty")
            return False
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next


ll = LinkedList()
ll.addStart(1)
ll.addStart(2)
ll.addStart(2)
ll.addStart(12)
ll.display()
ll.reverseList()
print("\n")
ll.display()
