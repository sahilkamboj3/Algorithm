import numpy as np

"""
In insertion sort, we start at index 1 and move our way down the array. In doing so, at each index, we keep moving the number to the beginning of the array, or as far as we get, comparing that number with the previous index. If the number on the right is smaller, we swap the two numbers.
"""


def insertion_sort(A):
    for i in range(len(A) - 1):
        j = i + 1
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1


A = np.random.randint(low=0, high=50, size=10000)
print(A)
insertion_sort(A)
print(A)
