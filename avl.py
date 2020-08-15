import numpy as np


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, num):
        new_node = Node(num)
        if not self.root:
            self.root = new_node
            return

        cur = self.root
        self.add(cur, new_node)
        self.adjust_heights(new_node.parent)
        self.fix_balance(new_node.parent)

    def add(self, node, new_node):
        if new_node.val > node.val:
            if node.right:
                self.add(node.right, new_node)
            else:
                node.right = new_node
                new_node.parent = node
        elif new_node.val <= node.val:
            if node.left:
                self.add(node.left, new_node)
            else:
                node.left = new_node
                new_node.parent = node

    def adjust_heights(self, node):
        if node:
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0

            node.height = max(left_height, right_height) + 1
            self.adjust_heights(node.parent)

    def fix_balance(self, node):
        if node:
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0

            balance = left_height - right_height

            new_parent = None

            if balance > 1:
                successor = node.left
                if not successor.left:
                    self.left_rot(successor)
                new_parent = self.right_rot(node)
                new_parent.right.height -= 2

            elif balance < -1:
                successor = node.right
                if not successor.right:
                    self.right_rot(successor)
                new_parent = self.left_rot(node)
                new_parent.left.height -= 2

            if new_parent:
                if new_parent.parent:
                    new_parent.parent.height -= 1
                self.fix_balance(new_parent.parent)
            else:
                self.fix_balance(node.parent)

    def right_rot(self, node):
        if node:
            predecessor = node.parent
            successor = node.left

            if predecessor:
                predecessor.left = successor
                successor.parent = predecessor
            else:
                self.root = successor
                successor.parent = None

            new_left = successor.right
            successor.right = node
            node.parent = successor
            node.left = new_left

            return successor

    def left_rot(self, node):
        if node:
            predecessor = node.parent
            successor = node.right

            if predecessor:
                predecessor.right = successor
                successor.parent = predecessor
            else:
                self.root = successor
                successor.parent = None

            new_right = successor.left
            successor.left = node
            node.parent = successor
            node.right = new_right

            return successor

    def print_avl(self):
        cur = self.root
        order = self.inorder_traversal('', cur)
        print(order + ' : ' + str(self.root.val))

    def inorder_traversal(self, string, cur):
        if cur:
            string = self.inorder_traversal(string, cur.left)
            string += str(cur.val) + f':{cur.height} - '
            string = self.inorder_traversal(string, cur.right)

        return string


# A = [50, 25, 75, 67, 100, 12, 37, 10, 9]
# A = [1, 2, 3, 4, 5, 50, 75, 67, 100]
A = np.random.randint(low=0, high=50, size=10)

avl = AVL()

for num in A:
    print(f'num: {num}')
    avl.insert(num)

avl.print_avl()
