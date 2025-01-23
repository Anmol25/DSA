array = [1000,4,90,80,20,40,-2]

def binary_search(array, item):
    s = 0
    e = len(array) - 1
    
    while(s<=e):
        mid = int((s+e)/2)
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            e = mid - 1
        else:
            s = mid + 1
    return -1


print(binary_search(array, 80))