def bubble(arr):
    for i in range(len(arr)):
        for j in range((len(arr)-i-1)):
            if arr[j] > arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp

    print(arr)

bubble([84, 24, 0, 65, 43])