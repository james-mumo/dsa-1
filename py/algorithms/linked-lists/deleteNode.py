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
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

    def displayNodes(self):
        if self.head is None:
            print("Empty")
        else:
            curr = self.head
            while curr:
                print(curr.data, end=" -> ")
                curr = curr.next
            print()

    def delStart(self):
        if self.head is None:
            print("Empty List")
        else:
            self.head = self.head.next

    def endNode(self):
        if self.head is None:
            print("Empty List")
        else:
            curr = self.head
            prev = None;
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None

    def delStart(self):
        if self.head is None:
            print("Empty List")
            return
        else:
            self.head = self.head.next



ll = Linkedlist()
ll.addEnd(5)
ll.addEnd(4)
ll.addEnd(3)
ll.addEnd(2)
ll.addEnd(1)
ll.displayNodes()
ll.endNode()
ll.displayNodes()
ll.delStart()
ll.displayNodes()
