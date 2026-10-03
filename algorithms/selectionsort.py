def selectionsort(arr:list[int]):

    for i in range(0,len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
    return arr

arr1 = [23,1,5,25,96,12]
print(selectionsort(arr1))