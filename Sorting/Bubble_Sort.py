array = [1000,4,90,80,20,40,-2]

# Bubble sort
for j in range(len(array)-1):
    for i in range(len(array)-1):
        pt_1 = i
        pt_2 = i + 1
        
        if array[pt_1] > array[pt_2]:
            array[pt_1] , array[pt_2] = array[pt_2], array[pt_1]

print(array)