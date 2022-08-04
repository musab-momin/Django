def selection_sort(arr):
    n = len(arr)
    sorted_arr = []
    
    while(len(sorted_arr) != n):
        mini = find_minimum(arr)
        arr.remove(mini)
        sorted_arr.append(mini)
        
    return sorted_arr



def find_minimum(arr):
    mini = arr[0]
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
    return mini




arr =  [ 10, 14, 28, 11, 7, 16, 30, 50, 25 ]
print(selection_sort(arr))