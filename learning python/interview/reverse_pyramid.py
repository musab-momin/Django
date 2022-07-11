def print_pyramid(num):
    row = num
    col = row*2-1

    start = 0 
    end = col-1

    for i in range(row):
        for j in range(col):
            if j >= start and j<=end:
                print('#', end='')
            else:
                print(' ', end='')
        start += 1
        end -= 1
        print()


test = 10
print_pyramid(test)