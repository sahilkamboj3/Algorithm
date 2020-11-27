from bst import Node, BinarySearchTree


class Queue:  # FIFO
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]


class BreadthFirstSearch:
    def __init__(self):
        self.bst = BinarySearchTree()

    def fill_bst(self, nums):
        for num in nums:
            self.add(num)

    def add(self, num):
        self.bst.add(num)

    def bfs_print(self):
        stack = Queue()
        cur = self.bst.head
        string = ''

        stack.enqueue(cur)

        while not stack.is_empty():
            node = stack.dequeue()

            if node.left:
                stack.enqueue(node.left)
            if node.right:
                stack.enqueue(node.right)

            string += str(node.val) + '-'

        return string


bfs = BreadthFirstSearch()

A = [5, 2, 8, 1, 4, 3, 6, 10, 5, 7, 9]

bfs.fill_bst(A)
print(bfs.bfs_print())
