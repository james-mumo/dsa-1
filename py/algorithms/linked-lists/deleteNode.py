class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = newNode
        else:
            curr = self.head
            while curr