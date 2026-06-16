arr = [ 7, 12, 9, 11, 3]

for j in range(len(arr) - 1) :
    
    index = j
    
    for i in range(j+1, len(arr)) :
        if arr[i] < arr[index] :
            index = i
    
    arr[j] , arr[index] = arr[index], arr[j]
print(arr)


#using function.
def selectionsort(arr):

    for j in range(len(arr) - 1):

        index = j

        for i in range(j + 1, len(arr)):
            if arr[i] < arr[index]:
                index = i

        arr[j], arr[index] = arr[index], arr[j]

    return arr


print(selectionsort([7, 12, 9, 11, 3]))
    