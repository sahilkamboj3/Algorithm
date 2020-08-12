import numpy as np


def selection_sort(A):
    for i in range(len(A) - 1):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


A = np.random.randint(low=0, high=50, size=15)
print(A)
selection_sort(A)
print(A)
