def count_sort(A):
    output = [0 for i in range(max(A))]
    counts = [0 for i in range(max(A))]

    for num in A:
        counts[num - 1] += 1

    for i in range(len(A) - 1):
        counts[i + 1] = counts[i + 1] + counts[i]

    print(counts)


A = [4, 5, 2, 3, 1]
count_sort(A)
