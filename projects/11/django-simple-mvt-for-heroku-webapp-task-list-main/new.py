import random


class BinaryTreeInstance:
    def __init__(self, data: int):
        self.data: int = data
        self.right: BinaryTreeInstance | None = None
        self.left: BinaryTreeInstance | None = None

    def __repr__(self):
        lines, *_ = self.__display()
        for line in lines:
            print(line)
        return '\n'

    def insert(self, data: int) -> None:
        if self.data <= data:
            if self.right is None:
                self.right = BinaryTreeInstance(data)
            else:
                self.right.insert(data)
        elif self.data > data:
            if self.left is None:
                self.left = BinaryTreeInstance(data)
            else:
                self.left.insert(data)

    def __display(self):
        line = f"{self.data}"
        width = len(line)

        # todo none child
        if self.right is None and self.left is None:
            return [line], width, 1, width // 2

        # todo right child
        if self.left is None:
            lines, n, p, x = self.right.__display()
            return [line + x * '_' + (n - x) * ' ', (width + x) * ' ' + '\\' + (n - x - 1) * ' '] + \
                   [width * ' ' + line for line in lines], n + width, p + 2, width // 2

        # todo left child
        if self.right is None:
            lines, n, p, x = self.left.__display()
            return [(x + 1) * ' ' + (n - x - 1) * '_' + line, x * ' ' + '/' + (n - x - 1 + width) * ' '] + \
                   [line + width * ' ' for line in lines], n + width, p + 2, n + width // 2

        # todo both child
        if self.right is not None and self.left is not None:
            left, n, p, x = self.left.__display()
            right, m, q, y = self.right.__display()
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            return [
                       (x + 1) * ' ' + (n - x - 1) * '_' + line + y * '_' + (m - y) * ' ',
                       x * ' ' + '/' + (n - x - 1 + width + y) * ' ' + '\\' + (m - y - 1) * ' '
                   ] + [a + width * ' ' + b for a, b in zip(left, right)], n + m + width, max(p,
                                                                                              q) + 2, n + width // 2

tree1 = BinaryTreeInstance(0)
for i in range(1, 500 + 1):
    # tree1.insert(i)
    tree1.insert(random.randint(0, 1000))
print(tree1)





# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left_neel = None
        self.rightChild = None

    def insert(self, data):
        if data < self.data:
            if self.left_neel:
                self.left_neel.insert(data)
            else:
                self.left_neel = Node(data)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    def PrintTree(self):
        if self.left_neel:
            self.left_neel.PrintTree()
        print(self.data),
        if self.rightChild:
            self.rightChild.PrintTree()


# Creating root node
root = Node(27)
# Inserting values in BST
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
# printing BST
root.PrintTree()
# https://www.educative.io/answers/binary-trees-in-python

