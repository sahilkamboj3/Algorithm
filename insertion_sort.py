import numpy as np

# arr = [3, 4, 2, 1, 5, 4, 6, 7]
# arr = [5, 4, 3, 2, 1]
arr = np.random.randint(low=1, high=100, size=100)


def insert_sort(arr):
    for i in range(len(arr)):
        while arr[i] < arr[i - 1] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


print(arr)
insert_sort(arr)
print(arr)
