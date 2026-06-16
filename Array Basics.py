# Swap first and last:

arr = [11, 22, 33]
temp = arr[0]
arr[0] = arr[2]
arr[2] = temp
for i in range(3):
    print(arr[i], end=" ")


# Create an algorithm to find the lowest value in a array.

my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

#  Input and Print Integer and String Array
arr = []
for i in range(5):
    arr.append(int(input()))

for num in arr:
    print(num)

print(arr[-1])

name = []
for i in range(5):
    name.append(input())

for string in name:
    print(string)
 
    
# 2D Array Input and Print with Indices
arr1 = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    arr1.append(row)

for i in range(3):
    for j in range(3):
        print(i, j, end=" ")
        print(arr1[i][j], end=" ")
    print()
    
    
# Check if Array is Sorted

arr = [1, 2, 3, 4, 5]
is_sorted = False

for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        is_sorted = True
        break

if is_sorted:
    print("Sorted")
    
# Largest Element

arr = [3, -2, 7, -1, 0, 5, -4]
largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest:", largest)

# Second Largest Element

arr = [3, -2, 7, -1, 0, 5, -4]
largest = arr[0]
second_largest = float('-inf')

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Second Largest:", second_largest)

# Third Largest Element

arr = [3, -2, 7, -1, 0, 5, -4]
largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')

for i in range(len(arr)):
    if arr[i] > largest:
        third_largest = second_largest
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        third_largest = second_largest
        second_largest = arr[i]
    elif arr[i] > third_largest and arr[i] != largest and arr[i] != second_largest:
        third_largest = arr[i]

print("Third Largest:", third_largest)