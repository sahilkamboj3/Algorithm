arr = [6, 5, 4, 3, 2, 1]
"""
          0
    1           5
  3   4        2
"""


class MaxHeap():
    def __init__(self):
        self.heap = []

    def add(self, num):
        self.heap.append(num)
        self.float_up(len(self.heap) - 1)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i],

    def float_up(self, idx):
        if idx == 0:
            return

        parent_idx = (idx - 1) // 2
        if self.heap[idx] > self.heap[parent_idx]:
            self.swap(parent_idx, idx)
            self.float_up(parent_idx)

    def bubble_down(self, idx):
        left_child = (2 * idx) + 1
        right_child = left_child + 1
        largest_idx = None

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[idx]:
            largest_idx = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[left_child]:
            largest_idx = right_child

        if largest_idx:
            self.swap(largest_idx, idx)
            self.bubble_down(largest_idx)

    def print_heap(self):
        print(str(self.heap))

    def extract_max(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        elif len(self.heap) > 1:
            self.swap(0, len(self.heap) - 1)
            node = self.heap.pop()
            self.bubble_down(0)
            return node
        else:
            return 'list is empty'


mh = MaxHeap()

for i in range(11):
    mh.add(i + 1)

for i in range(12):
    print(mh.extract_max())
