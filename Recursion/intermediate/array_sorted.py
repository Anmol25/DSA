def sorted(arr, n):
    if n == 0 or n == 1:
        return True
    
    if arr[0] > arr [1]:
        return False
    
    return sorted(arr[1:],n-1)

array = [20,2,3,4,5,6]

print(sorted(array, 6))