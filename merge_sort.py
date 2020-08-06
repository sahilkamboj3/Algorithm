import numpy as np

"""
The idea in merge sort is to keep splitting the array until we have n 1-number arrays, essentially, and use two pointers to put sort them in the final array.
"""


def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2

        L = A[mid:]
        R = A[:mid]

        merge_sort(L)
        merge_sort(R)
        sort_arrs(L, R, A)


def sort_arrs(L, R, A):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


A = np.random.randint(low=0, high=50, size=15).tolist()
print(A)
merge_sort(A)
print(A)
