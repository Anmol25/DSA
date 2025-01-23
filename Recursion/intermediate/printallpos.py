def printpos(arr, size, i, x):
    if size == i:
        return
    
    if arr[i] == x:
        print(i, end= " ")

    # print rest
    printpos(arr,size,i+1,x)

arr = [1,34,3,1,33,22,1]

printpos(arr,7,0,1)
print("")