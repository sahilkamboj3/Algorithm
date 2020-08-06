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

    def extract_min(self):
        pass

    def heapify_down(self, idx):
        pass
