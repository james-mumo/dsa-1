class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LList:
    def __init__(self):
        self.head = None

    def addStart(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def search(self, key):
        if self.head is None:
            print(f"{key} not found as List is empty!!!")
            return
        else:
            current = self.head
            while(current):
                if current.data == key:
                    print(f"{key} was found")
                    return True
                current = current.next

            return "False"



ll = LList()
ll.addStart(1)
ll.addStart(1)
ll.addStart(1)
ll.addStart(2)
ll.addEnd(3)
ll.addStart(2)
ll.addEnd(3)
ll.addEnd(3)
ll.display()
ll.search(1)


key = 2
the_head = ll.head
items = []

while(the_head):
    items.append(the_head.data)
    the_head = the_head.next
#
# if key in items:
#     print(f"{key} was found")
# else:
#     print(f"{key} wasn't found")
