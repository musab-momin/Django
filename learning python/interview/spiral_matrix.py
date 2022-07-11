#write a function that accecpt an integer N. and return NxN matrix


#my solution

# def make_spiral(n):
#     result = []
#     counter = 1
#     start_row = 0
#     end_row = n-1
#     start_col = 0
#     end_col = n-1

#     while start_col <= end_col and start_row <= end_row:
#         result.append([])
#         for col in range(start_col, end_col+1):
#             print(result)

#     print(result)

#tutor solutions
def make_spiral(n):
    result = []
    #append n sub arrays in result
    for i in range(n):
        tmp =[]
        for j in range(n):
            tmp.append(0)
        result.append(tmp)
    #print(result)

    #creating variable to have record of matrix
    counter = 1
    start_row = 0
    end_row = n-1
    start_col = 0
    end_col = n-1

    #all the comments are writen by considering n = 3 and only for first while iteration
    while start_col <= end_col and start_row <= end_row:
        #this line will fill top row of our result  
        for i in range(start_col, end_col+1):
            result[start_row][i] = counter
            counter += 1
        #output after this for loop will be this [[1, 2, 3], 
        # [], 
        # []]
        start_row += 1
        #this line will fill right(last) col of our result  
        for i in range(start_row, end_row+1):
            result[i][end_col] = counter
            counter += 1
        #output after this for loop will be this [
        # [1, 2, 3], 
        # [, , 4], 
        # [, , 5]]
        
        end_col -= 1
        
        #this line will fill bottom two col of our result
        for i in range(end_col, start_col-1, -1):
            result[end_row][i] = counter
            counter += 1
        
        #output after this for loop will be this [
        # [1, 2, 3], 
        # [, , 4], 
        # [7, 6, 5]]
        
        end_row -= 1
        
        #this line will fill left col of our result
        for i in range(end_row, start_row-1, -1):
            result[i][start_col] = counter
            counter += 1
        
        #output after this for loop will be this [
        # [1, 2, 3], 
        # [8, , 4], 
        # [7, 6, 5]]
        start_col += 1

    print(result)

    
make_spiral(5)