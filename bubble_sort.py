import numpy as np

"""
In bubble sort, we want to 'bubble' the highest numbers to the very end of the array until we get a sorted array.
[5, 4, 3, 2, 1] -> [4, 5, 3, 2, 1] -> [4, 3, 5, 2, 1] -> [4, 3, 2, 5, 1] -> [4, 3, 2, 1, 5]
[4, 3, 2, 1, 5] -> [3, 4, 2, 1, 5] -> [3, 2, 4, 1, 5] -> [3, 2, 1, 4, 5]
[3, 2, 1, 4, 5] ... -> [2, 1, 3, 4, 5]
[2, 1, 3, 4, 5] -> [1, 2, 3, 4, 5]
"""


def bubble_sort(A):
    end = 1
    while end != len(A):
        for i in range(len(A) - end):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
        end += 1


A = np.random.randint(low=0, high=50, size=15)
print(A)
bubble_sort(A)
print(A)
