import numpy as np

"""
Concept: Starting from index 0, find the minimum in in the array from that index to the end and place that at the current index we're iterating on.
Time Complexity: O(n^2)
Space Complexity: 
"""


def select_sort(A):
    for i in range(len(A) - 1):
        j = i + 1
        min_ = i

        while j < len(A):
            if A[j] < A[min_]:
                min_ = j
            j += 1

        A[i], A[min_] = A[min_], A[i]


A = np.random.randint(100, size=5)
print(A)
select_sort(A)
print(A)
