import numpy as np


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.head = None

    def print_bst(self, traversal):
        if traversal == 'inorder':
            cur = self.head
            print(self.inorder_traversal('', cur))
            return

    def inorder_traversal(self, string, cur):
        if cur:
            string = self.inorder_traversal(string, cur.left)
            string += str(cur.val) + '-'
            string = self.inorder_traversal(string, cur.right)

        return string

    def add(self, num):
        new_node = Node(num)

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        self.insert(cur, new_node)

    def insert(self, cur, new_node):
        if new_node.val < cur.val:
            if not cur.left:
                cur.left = new_node
                new_node.parent = cur
                return

            self.insert(cur.left, new_node)

        elif new_node.val >= cur.val:
            if not cur.right:
                cur.right = new_node
                new_node.parent = cur
                return

            self.insert(cur.right, new_node)

    def find(self, num):
        cur = self.head
        return self.find_helper(cur, num)

    def find_helper(self, node, num):
        if node.val == num:
            return True
        elif num < node.val:
            if not node.left:
                return False
            return self.find_helper(node.left, num)
        else:
            if not node.right:
                return False
            return self.find_helper(node.right, num)

    def delete(self, num):
        cur = self.head
        node = self.find_node(cur, num)
        if node:
            self.delete_node(node)
        else:
            print('is none')

    def find_node(self, cur, num):
        if num == cur.val:
            return cur
        elif num < cur.val:
            if cur.left:
                return self.find_node(cur.left, num)
            else:
                return None
        elif num >= cur.val:
            if cur.right:
                return self.find_node(cur.right, num)
            else:
                return None

    def delete_node(self, node):
        if node.parent:
            parent = node.parent

        if node.left and not node.right:  # only left node
            if node == self.head:
                self.head = node.left
            else:
                parent.right = node.left
                node.left.parent = parent
        elif node.right and not node.left:  # only right node
            if node == self.head:
                self.head = node.right
            else:
                parent.left = node.right
                node.right.parent = parent
        elif not node.left and not node.right:  # leaf node
            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None
        else:  # both node.left and node.right
            num, largest_node = self.find_largest_node_left_tree(node.left)

            node.val = num
            parent = largest_node.parent
            if parent.left == largest_node:
                parent.left = None
            elif parent.right == largest_node:
                parent.right = None

    def find_largest_node_left_tree(self, node):
        if node.right:
            return self.find_largest_node_left_tree(node.right)
        return node.val, node


bst = BST()
traversal = 'inorder'

# A = np.random.randint(low=0, high=25, size=5)
# print(A)

A = [4, 7, 2, 5, 6]

for num in A:
    bst.add(num)

bst.print_bst(traversal)
print(bst.head.val)

bst.delete(4)

bst.print_bst(traversal)
print(bst.head.val)

# for i, num in enumerate(A):
#     print(f'{num}: {bst.find(num)}')

# print(bst.find(1))
