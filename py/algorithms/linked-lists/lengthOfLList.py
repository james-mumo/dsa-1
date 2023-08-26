class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def addStart(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.tail
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head

    def search(self, key):
        if self.head is None:
            print("It's Empty")
            return
        else:
            current = self.head
            while current:
                if current.data == key:
                    print("Key found")
                    return True
                current = current.next
            return "False"

    def getCount(self):
        if self.head is None:
            print("Empty llist")
            return 0
        else:
            current = self.head
            i = 1
            while current:
                i += 1
                current = current.next
                if current.next is self.head:
                    break
            return i


ll = LLists()
ll.addStart(1)
ll.addStart(13)
ll.addStart(12)
ll.addStart(11)
ll.search(1)
print(ll.getCount())
