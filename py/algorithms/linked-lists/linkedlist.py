class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def AddStart(self, data):
        newNode = Node(data)

        if self.head is None:
            newNode.next = self.head
            self.head = newNode

        else:
            self.head.next = newNode

    def getCount(self):

        if self.head is None:
            return 0

        else:
            current = self.head
            count = 0
            while current:
                count += 1
                current = current.next
                if current.next is self.head:
                    break
            return count


ll = LinkedList()
ll.AddStart(1)
ll.AddStart(1)
ll.AddStart(1)
ll.AddStart(1)
print(ll.getCount())
