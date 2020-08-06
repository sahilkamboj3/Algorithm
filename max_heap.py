import numpy as np


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.i = 1

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def add(self, num):
        self.heap.append(num)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, idx):
        if idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx] < self.heap[idx]:
                self.swap(parent_idx, idx)
                self.heapify_up(parent_idx)

    def fill_heap(self, arr):
        for num in arr:
            self.add(num)

    def extract_max(self):
        if self.i < len(self.heap):
            self.swap(0, len(self.heap) - self.i)
            self.heapify_down(0)
            self.i += 1

    def heapify_down(self, idx):
        left_child = (2 * idx) + 1
        right_child = left_child + 1
        largest_idx = None

        if left_child < len(self.heap) - self.i and self.heap[left_child] > self.heap[idx]:
            largest_idx = left_child
        if right_child < len(self.heap) - self.i and self.heap[right_child] > self.heap[left_child]:
            largest_idx = right_child

        if largest_idx:
            self.swap(largest_idx, idx)
            self.heapify_down(largest_idx)

    def sort(self):
        for i in range(len(self.heap) - 1):
            self.extract_max()

    def print_heap(self):
        print(str(self.heap))


A = np.random.randint(low=0, high=50, size=15)

mh = MaxHeap()

mh.fill_heap(A)
mh.print_heap()

mh.sort()
mh.print_heap()
