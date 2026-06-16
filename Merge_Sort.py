# Merge Sort

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    left = []
    right = []

    for i in range(n1):
        left.append(arr[l + i])
    for j in range(n2):
        right.append(arr[mid + 1 + j])

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1

    while i < n1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = right[j]
        k += 1
        j += 1


def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def display_array(arr):
    for i in arr:
        print(i, end=" ")
    print()


arr = [4, 1, 3, 5, 2]
n = len(arr)

print("Array before sorting")
display_array(arr)

merge_sort(arr, 0, n - 1)

print("Array after sorting")
display_array(arr)