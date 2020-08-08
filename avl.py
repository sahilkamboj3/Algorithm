class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class AVL:
    def __init__(self):
        self.head = None

    def insert(self, num):
        new_node = Node(num)

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        self.add(cur, new_node)

    def add(self, cur, new_node):
        if new_node.val < cur.val:
            if cur.left:
                self.add(cur.left, new_node)
            else:
                cur.left = new_node
                new_node.parent = cur
        elif new_node.val >= cur.val:
            if cur.right:
                self.add(cur.right, new_node)
            else:
                cur.right = new_node
                new_node.parent = cur

    def find_height(self, node, height):
        if node.right:
            right_height = self.find_height(node.right, height + 1)
        else:
            right_height = height
        if node.left:
            left_height = self.find_height(node.left, height + 1)
        else:
            left_height = height

        return max(right_height, left_height)

    def find_balance(self, node):
        if node.left:
            left_node_balance = self.find_height(node.left, 0)  # or 0
        else:
            left_node_balance = -1
        if node.right:
            right_node_balance = self.find_height(node.right, 0)  # or 0
        else:
            right_node_balance = -1

        # print(left_node_balance, right_node_balance)
        return left_node_balance - right_node_balance

    def fix_balance(self, node, balance):
        balance = self.find_balance(node)

        if balance < -1:
            self.left_rot(node)
        elif balance > 1:
            self.right_rot(node)

    def left_rot(self, node):
        self.swap(node, node.right)

    def right_rot(self, node):
        self.swap(node, node.left)

    def swap(self, node1, node2, direction):
        head = False
        if node1 == self.head:
            head = True

        node1_parent = node1.parent
        # print(node1_parent.val)

        node_2_left = node2.left
        node_2_right = node2.right

        node1.right = node_2_right
        node1.left = node_2_left

        if direction == 'right':
            node2.right = node1
        elif direction == 'left':
            node2.left = node1

        node2.parent = node1_parent
        node1.parent = node2

        if node1_parent and direction == 'right':
            node1_parent.right = node2
        elif node1_parent and direction == 'left':
            node1_parent.left = node2

        if head:
            self.head = node2

    def print_avl(self):  # this is an inorder traversal
        cur = self.head
        print(self.print_helper('', cur))
        return

    def print_helper(self, string, cur):
        if cur:
            string = self.print_helper(string, cur.left)
            string += str(cur.val) + '-'
            string = self.print_helper(string, cur.right)

        return string


A = [50, 25, 75, 67, 100, 12, 37, 10, 9]
# A = [1, 2, 3]

avl = AVL()

for num in A:
    avl.insert(num)

# avl.insert(5)
# avl.insert(3)
# avl.insert(7)
# avl.insert(1)
avl.print_avl()
# print(avl.find_height(avl.head, 0))
# print(avl.find_balance(avl.head))
