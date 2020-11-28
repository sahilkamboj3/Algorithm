class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def add(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = node

    def delete(self, val):
        if not self.head:
            return

        prev = None
        cur = self.head

        while cur and cur.val != val:
            prev = cur
            cur = cur.next

        if cur == self.head:
            self.head = self.head.next
            return

        if not cur:
            return

        prev.next = cur.next
        del cur

    def __str__(self):
        cur = self.head
        string = "[ "

        while cur:
            string += str(cur.val) + " "
            cur = cur.next

        string += "]"

        return string


range_ = 4
sll = SLL()

for i in range(range_):
    sll.add(i)

print(sll)

# sll.delete(3)
# print(sll)

# sll.delete(0)
# print(sll)

for i in range(range_):
    sll.delete(i)

print(sll)
