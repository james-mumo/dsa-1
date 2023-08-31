from sys import maxsize


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def pushItem(stack, item):
    stack.append(item)
    print(item, "pushed to stack")


def popItem(stack):
    if len(stack) == 0:
        return
    return stack.pop()


def peekLast(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]


stack = createStack()
pushItem(stack, 1)
pushItem(stack, 1)
pushItem(stack, 2)
pushItem(stack, 4)
