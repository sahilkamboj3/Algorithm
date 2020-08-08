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
        elif new_node.val >= cur.val:
            if cur.right:
                self.add(cur.right, new_node)
            else:
                cur.right = new_node

    # def find_height(self, node, height):
    #     if node:
    #         height = self.find_height(node.left, height)
    #         height += 1
    #         height = self.find_height(node.right, height)
    #    return height

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


avl = AVL()
avl.insert(5)
avl.insert(3)
avl.insert(7)
avl.insert(1)
avl.print_avl()
