from nodes import LLNode as Node


class SLL:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def prepend(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete(self, val):
        if not self.head:
            return

        prev = None
        cur = self.head

        while cur and cur.val != val:
            prev = cur
            cur = cur.next

        if not cur:
            return
        elif cur == self.head:
            self.head = self.head.next
        else:
            prev.next = cur.next
            del cur

    def __repr__(self):
        if not self.head:
            return 'Empty'

        length = 0
        cur = self.head
        arr = []

        while cur:
            length += 1
            arr.append(cur.val)
            cur = cur.next

        return str(arr) + ' is length ' + str(length)


sll = SLL()
sll.append(0)
sll.append(1)
sll.append(2)
sll.prepend(3)
sll.delete(3)
print(sll)
