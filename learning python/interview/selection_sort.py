def selection(arr):
    for i in range(len(arr)):
        index_of_lowest = i
        for j in range(i+1, len(arr)):
            if arr[index_of_lowest] > arr[j]:
                index_of_lowest = j
        if arr[i] != arr[index_of_lowest]:
            tmp = arr[i]
            arr[i] = arr[index_of_lowest]
            arr[index_of_lowest] = tmp

    print(arr)


selection([84, 24, 0, 65, 43, -1])