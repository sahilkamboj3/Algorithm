import numpy as np

# arr = [3, 4, 2, 1, 5, 4, 6, 7]
# arr = [5, 4, 3, 2, 1]
arr = np.random.randint(low=1, high=1000, size=1000)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(arr)
print(arr)
