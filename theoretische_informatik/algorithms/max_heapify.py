A = [3, 1, 4, 1, 5, 9, 2, 6, 5]
m = len(A)
i = 0


def max_heap(A, m):
    for i in range((m // 2) - 1, -1, -1):
        max_heap_correct(A, m - 1, i)

def max_heap_correct(A, m, i):
    print(A)
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= m and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= m and A[r] > A[largest]:
        largest = r

    if largest != i:
        print(f"Swapping {A[i]} and {A[largest]}")
        A[i], A[largest] = A[largest], A[i]
        max_heap_correct(A, m, largest)

print(A)  # Output the original array
max_heap(A, m)
print(A)  # Output the modified array
