def alloccur(arr, size, x, i):
    if size == i:
        return 0
    
    ans = 0
    if arr[i] == x:
        ans = 1

    return ans + alloccur(arr,size,x,i+1)

arr = [1,2,3,1,4,8,1]

print(alloccur(arr, 7, 1, 0))