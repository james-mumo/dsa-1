# Stack implementation in python
# LIFO
# pop push and pop methods


# creating the stack
def create():
    stack = []
    return stack

# check if empty
def checkEmpty(stack):
    return len(stack) == 0

def addItem(stack, item):
    stack.append(item)
    print("Added item, ", item)

def rmvItem(stack):
    if (checkEmpty(stack)):
        return "Its emppty"
    stack.pop()
    print("Removed the Item", str(stack))



stack = create()
addItem(stack, 1)
addItem(stack, 2)
addItem(stack, 3)
rmvItem(stack)

addItem(stack, 3)
















# 
# 
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Creating a stack
my_stack = Stack()

# Pushing items onto the stack
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# Peeking at the top item
print("Top item:", my_stack.peek())

# Popping items from the stack
print("Popped:", my_stack.pop())
print("Popped:", my_stack.pop())

# Checking if the stack is empty
print("Is the stack empty?", my_stack.is_empty())

# Getting the size of the stack
print("Stack size:", my_stack.size())
