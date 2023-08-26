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
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def getCount(self):
        if self.head is None:
            return 0
        else:
            count = 0
            curr = self.head
            while curr:
                count += 1
                curr = curr.next
                if curr == self.head:
                    break
            return count

    def printList(self):
        if self.head is None:
            return
        else:
            curr = self.head
            while curr:
                print(curr.data, end="-->")
                curr = curr.next
                if curr == self.head:
                    break
            print()

    def reverseList(self):
        if self.head is None:
            return
        else:
            prev = None
            curr = self.head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr



ll = LinkedList()
ll.AddStart(1)
ll.AddStart(2)
ll.AddStart(3)
ll.AddStart(4)
ll.printList()
print()
ll.reverseList()
ll.printList()
print()
print(ll.getCount())
