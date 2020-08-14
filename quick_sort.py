import numpy as np

A = np.random.randint(low=0, high=100, size=15)


def quick_sort(A):
    _quick_sort(A, 0, len(A) - 1)


def _quick_sort(A, low, high):
    if low < high:
        split = partition(A, low, high)
        _quick_sort(A, low, split - 1)
        _quick_sort(A, split + 1, high)


def partition(A, low, high):
    i = low - 1
    pivot = A[high]

    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[high] = A[high], A[i + 1]

    return i + 1


print(A)
quick_sort(A)
print(A)
