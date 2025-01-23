def isPresent(arr, size, num):
    if size == 0:
        return False
    
    if arr[0] == num:
        return True
    
    return isPresent(arr[1:], size - 1 ,num)

arr = [1,2,3,4]

print(isPresent(arr, 4, 8))
