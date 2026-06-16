# Insertion Sort


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

a = [8, 3, 6, 5, 4, 2]
insertion_sort(a)
for i in a:
    print(i, end=" ")