class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class AVL:
    def __init__(self):
        self.head = None


A = [50, 25, 75, 67, 100, 12, 37, 10, 9]

avl = AVL()

# for num in A:
#     avl.insert(num)

avl.insert(3)
avl.insert(2)
# avl.insert(1)

avl.print_avl('inorder')
