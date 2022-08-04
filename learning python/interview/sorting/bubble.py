from sqlalchemy import true

# time complexity is n^2 and space complexity is O(n)
# iterare through the array and compare the first element of arr with rest of other repeat this process for 
# every element.


def bubble_sort(arr):
    n = len(arr)
    while(true):
        swap = False
        for i in range(n-1):
           if(arr[i+1] < arr[i]):
               tmp = arr[i]
               arr[i] = arr[i+1]
               arr[i+1] = tmp
               swap = True
        
        if not swap:
            break;
    
    return arr


arr = [7, 2, 9, 10, 5, 8, 32, 1]
print(bubble_sort(arr))