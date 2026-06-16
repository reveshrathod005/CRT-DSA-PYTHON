# Linear Search, Count Occurrences and Max Consecutive Ones


def max_consecutive_ones(arr):
    current_count = 0
    max_count = 0
    for j in range(len(arr)):
        if arr[j] == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return current_count


def count_linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count = i
    return count


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

target = int(input())

max_ = max_consecutive_ones(arr)
print(max_)