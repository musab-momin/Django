def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    center = len(arr) // 2
    left = arr[0:center]
    right = arr[center:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    sorted_arr =[]
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    
    while len(left) > 0:
        sorted_arr.append(left.pop(0))
    
    while len(right) > 0:
        sorted_arr.append(right.pop(0))

    return sorted_arr


sorted_arr = mergeSort([-30, 22, 0, 97])
print(sorted_arr)