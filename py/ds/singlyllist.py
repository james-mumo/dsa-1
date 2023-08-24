# we have a node class with data and ref
class Node:
    def __init__(self, data):
        self.ref = None
        self.data = data

# here is a head node of the chain of nodes
node1 = Node(10)

class LList:
    def __init__(self):
        self.head = None    # since its empty here no head

    def printList(self):
        if self.head is None:
            print("LList is none")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

ll = LList()
ll.printList()


