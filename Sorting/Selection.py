array = [1000,4,90,80,20,40,-2]

# Selection sort
for i in range(len(array)):
    min_idx = i
    for j in range(min_idx + 1,len(array)):
        if array[min_idx] > array[j]:
            # swap
            array[min_idx] , array[j] = array[j], array[min_idx]

print(array)