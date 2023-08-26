class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            curr = self.head
            while curr:
                tmp = curr.next
                del curr
                curr = tmp
            self.head = None
            print("Linked list deleted")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create a linked list
linked_list = LinkedList()
linked_list.insert(8)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(1)
linked_list.insert(7)

print("Original Linked List:")
linked_list.display()

# Delete the linked list
linked_list.delete_list()
linked_list.display()  # This will show that the list is empty
