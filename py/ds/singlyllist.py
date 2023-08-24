# we create the node
class Node:
    def __init__(self, data="None", ref="None"):
        self.data = data
        self.ref = ref


class LList:
    def __init__(self):
        self.head = None

    def printme(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_beginning(self, data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode


ll = LList()
ll.add_beginning(12)
ll.add_beginning(12)
ll.add_beginning(22)
ll.add_beginning(233)
ll.printme()
