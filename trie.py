class Node:
    def __init__(self, val):
        self.children = {}
        self.val = val


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        cur = self.root

        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]

    def find(self, string):
        cur = self.root

        for char in string:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return len(cur.children) == 0


trie = Trie()

trie.insert('sahil')
trie.insert('say')
trie.insert('sapp')
trie.insert('sape')

# print(trie.root.children)
