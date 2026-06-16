arr = [7, 12, 9, 11, 3]

for i in range(len(arr)-1) :
    for j in range(len(arr) - i - 1) :
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print(arr)

#improved bubble sort algo 

arr2  = [7, 3, 9, 12, 11]

swapped = False

for i in range(len(arr2)-1) :
    for j in range(len(arr2) - i - 1) :
        if arr2[j] > arr2[j+1] :
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
            swapped = True
            
    if not swapped :
        break    
        
print(arr)

        