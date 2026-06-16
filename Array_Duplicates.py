# Remove Duplicates from Array

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    is_duplicate = False
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            is_duplicate = True
            break
    if not is_duplicate:
        print(arr[i], "")
        

