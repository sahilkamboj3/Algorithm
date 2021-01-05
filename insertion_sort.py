import numpy as np

"""
Concept: Started from index 1, loop through and compare each number to its predecessor. If the predecessor is greater, swap the values, else move on to the next index.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def insert_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1


A = np.random.randint(100, size=(10))
print(A)
insert_sort(A)
print(A)
