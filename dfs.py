from bst import Node, BinarySearchTree


class Stack:  # LIFO
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def print_items(self):
        for item in self.items:
            print(item.val)


class DepthFirstSearch:
    def __init__(self):
        self.bst = BinarySearchTree()

    def fill_bst(self, nums):
        for num in nums:
            self.add(num)

    def add(self, num):
        self.bst.add(num)

    def prints(self):
        print(f'Postorder: {self.postorder_traversal()}')
        print(f'Preorder: {self.preorder_traversal()}')
        print(f'Inorder: {self.inorder_traversal()}')

    def postorder_traversal(self):
        cur = self.bst.head
        return self._post_helper(cur, '')

    def _post_helper(self, node, string):
        if node:
            string = self._post_helper(node.left, string)
            string = self._post_helper(node.right, string)
            string += str(node.val) + '-'

        return string

    def preorder_traversal(self):
        cur = self.bst.head
        return self._pre_helper(cur, '')

    def _pre_helper(self, node, string):
        if node:
            string += str(node.val) + '-'
            string = self._pre_helper(node.left, string)
            string = self._pre_helper(node.right, string)

        return string

    def inorder_traversal(self):
        cur = self.bst.head
        return self._in_helper(cur, '')

    def _in_helper(self, node, string):
        if node:
            string = self._post_helper(node.left, string)
            string += str(node.val) + '-'
            string = self._post_helper(node.right, string)

        return string


dfs = DepthFirstSearch()

A = [5, 2, 8, 1, 4, 3, 6, 10, 7, 9]

dfs.fill_bst(A)
dfs.prints()
