class Node(object):
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def insert(self, data):
        if not self.left:
            self.left = Node(data)
        elif not self.right:
            self.right = Node(data)
        else:
            self.left.insert(data)

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()


def sum_leaf_paths(root: Node, s):
    if not root:
        return 0
    s = s * 10 + root.data
    if not root.left and not root.right:
        return s

    return sum_leaf_paths(root.left, s) + sum_leaf_paths(root.right, s)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = Node(arr[0])
    for data in arr[1:]:
        root.insert(data)

    root.print()
    print(sum_leaf_paths(root, 0))
