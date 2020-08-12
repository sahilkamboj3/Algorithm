A = [5, 4, 3, 2, 1]


def quick_sort(A):
    _quick_sort(A, 0, len(A) - 1)


def _quick_sort(A, start, end):
    if len(A) > 1:
        quick_sort_iter(A, start, end)
        mid = (start + end) // 2

        quick_sort_iter(A, start, mid)
        quick_sort_iter(A, mid + 1, end)


def quick_sort_iter(A, start, end):
    mid = (start + end) // 2
    pivot = A[mid]

    A[mid], A[end] = A[end], A[mid]
    left_pointer = 0
    right_pointer = end - 1

    while left_pointer < right_pointer:
        while left_pointer < right_pointer and A[left_pointer] <= pivot:
            left_pointer += 1
        while left_pointer < right_pointer and A[right_pointer] >= pivot:
            right_pointer -= 1

        if left_pointer < right_pointer:
            A[left_pointer], A[right_pointer] = A[right_pointer], A[left_pointer]

    A[left_pointer - 1], A[end] = A[end], A[left_pointer - 1]


print(A)
quick_sort(A)
print(A)
# 0 3 6 9 10 11 - 8
