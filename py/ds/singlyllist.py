# we create the node
class Node:
    def __init__(self, data="None", ref="None"):
        self.data = data
        self.ref = ref

class LList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def printme(self):
        if self.head is None:
            print("List is empty")
            return


