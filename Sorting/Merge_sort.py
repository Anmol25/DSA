def merge(arr1,arr2):
    merged = [0] * (len(arr1) + len(arr2))
    i, j, k = 0,0,0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged[k] = arr1[i]
            k +=1
            i +=1
        else:
            merged[k] = arr2[j]
            k +=1
            j +=1

    while i < len(arr1):
        merged[k] = arr1[i]
        k +=1
        i +=1

    while j < len(arr2):
        merged[k] = arr2[j]
        k +=1
        j +=1

    return merged



def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    arr1 = mergeSort(arr[:mid])
    arr2 = mergeSort(arr[mid:])

    return merge(arr1,arr2)


array = [9,8,7,6,5,4,3,2,1]

array = mergeSort(array)

print(array)