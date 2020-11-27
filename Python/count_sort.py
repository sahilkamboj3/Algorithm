import numpy as np


def count_sort(A):
    k = max(A)
    counts = [0 for i in range(k + 1)]  # [0, 1, 1, 1, 1, 1]

    for num in A:
        counts[num] += 1

    output = []

    for i, count in enumerate(counts):
        while count > 0:
            output.append(i)
            count -= 1

    return output


A = np.random.randint(low=0, high=50, size=15)
sorted_arr = count_sort(A)

print(A)
print(sorted_arr)
