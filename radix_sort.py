A = [170, 45, 75, 90, 802, 24, 2, 66]
print(len(A))


def radix_sort(A):
    max_val = max(A)
    place_val = 1

    while (max_val // place_val) > 0:
        A = count_sort(A, place_val)
        place_val *= 10

    return A


def count_sort(A, place_val):
    counts = [0 for i in range(10)]
    output = [0 for i in range(len(A))]

    for num in A:
        digit = (num // place_val) % 10
        counts[digit] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for i in range(len(counts)):
        counts[i] -= 1

    for num in A:
        digit = (num // place_val) % 10
        output[counts[digit]] = num
        counts[digit] -= 1

    # print(output)
    return output


print(radix_sort(A))
