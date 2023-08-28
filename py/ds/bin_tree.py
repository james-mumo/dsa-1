class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * (size + 1)
        self.size = size

    def insert(self, value):
        if self.tree[1] is None:
            self.tree[1] = value
        else:
            index = 1
            while index <= self.size:
                if self.tree[index] is None:
                    self.tree[index] = value
                    break
                elif value <= self.tree[index]:
                    index = 2 * index
                else:
                    index = 2 * index + 1

    def display(self):
        for i in range(1, self.size + 1):
            if self.tree[i] is not None:
                print(self.tree[i], end=' ')
            else:
                print("-", end=' ')
        print()

# Create a binary tree with a size of 7
tree = BinaryTree(7)

# Insert values into the binary tree
values = [4, 2, 6, 1, 3, 5, 7]
for value in values:
    tree.insert(value)

# Display the binary tree
tree.display()