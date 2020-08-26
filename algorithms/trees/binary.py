class Node(object):
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

    def insert(self, data):
        if data > self.data:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)

    def contain(self, data):
        if data == self.data:
            return True

        if data > self.data:
            if not self.right:
                return False
            self.right.contain(data)
        else:
            if not self.left:
                return False
            self.left.contain(data)

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()


if __name__ == '__main__':
    arr = [2, 1, 8, 2, 6, 1, 7, 2]
    tree = Node(0)
    for _data in arr:
        tree.insert(_data)

    tree.print()

