import numpy as np


class MinHeap:
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
            parent = (idx - 1) // 2

            if self.heap[parent] > self.heap[idx]:
                self.swap(parent, idx)
                self.heapify_up(parent)

    def build_heap(self, nums):
        for num in nums:
            self.add(num)

    def extract_min(self):
        if self.i < len(self.heap):
            self.swap(0, len(self.heap) - self.i)
            self.heapify_down(0)
            self.i += 1

    def heapify_down(self, idx):
        left_child = (2 * idx) + 1
        right_child = left_child + 1
        largest_child = None

        if left_child < len(self.heap) - self.i and self.heap[left_child] < self.heap[idx]:
            largest_child = left_child

        if right_child < len(self.heap) - self.i and self.heap[right_child] < self.heap[left_child]:
            largest_child = right_child

        if largest_child:
            self.swap(largest_child, idx)
            self.heapify_down(largest_child)

    def sort_heap(self):
        while self.i < len(self.heap):
            self.extract_min()
        self.heap.reverse()

    def print_heap(self):
        print(str(self.heap))


mh = MinHeap()

A = np.random.randint(low=0, high=50, size=15).tolist()

mh.build_heap(A)
mh.sort_heap()

mh.print_heap()
