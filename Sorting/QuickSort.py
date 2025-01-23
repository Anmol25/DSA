def partition(arr, s, e):
    i = s
    pivot = arr[e]
    for j in range(s, e):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[e] = arr[e], arr[i]
    return i


def quickSort(arr, s, e):
    if (s >= e):
        return

    p = partition(arr, s, e)
    quickSort(arr, s, p-1)
    quickSort(arr, p+1, e)


array = [1000, 4, 90, 80, 20, 40, -2]

print(array)

quickSort(array, 0, len(array)-1)

print(array)
