from nodes import LLNode as Node


class DLL:
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
        new_node.prev = cur

    def prepend(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
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
            self.head.next.prev = None
            self.head = self.head.next
        elif not cur.next:
            prev.next = cur.next
        else:
            prev.next = cur.next
            cur.next.prev = cur.prev
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


dll = DLL()
dll.append(0)
dll.append(1)
dll.append(2)
dll.prepend(3)
dll.delete(2)
dll.delete(1)
dll.delete(3)
dll.delete(0)
print(dll)