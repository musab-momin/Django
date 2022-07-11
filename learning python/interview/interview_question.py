# arr = [1, 2, 3]
# arr_two = [4, 5, 6]
# lst = []

# for i in range(len(arr)):
#     lst.append(arr[i] + arr_two[i])

# print(lst)



# arr = [12, 43, 2, 100, 54, 5, 68]

# first = arr[0]
# second = arr[0]

# for i in arr:
#     if i > first:
#         second = first 
#         first = i
#     if i < first and i > second:
#         second = i

# print(first, second)
# arr.sort()
# print(arr)


#write a python program to print duplicates
# lst = ['hello', 20, 74, 20, 32, 19, 32]
# freq = {}

# for i in lst:
#     if i in freq.keys():
#         freq[i] = freq[i] + 1
#     else:
#         freq[i] = 1


# for key in freq.keys():
#     if freq[key] > 1:
#         print(key)


#what is the difference between is operator and '==' in python?

#is operator is used for reference comperision or address comperision
# == is use for content comperision


#a = 12
#b = 12

#print( a == b ) #output True
#print( a is b ) #output True


#lst = [1, 43, 5, 56]
#lst_two = [1, 43, 5, 56]

#print( lst is lst_two ) #output False
#print( lst == lst_two ) #output True

#lst_three = lst
#print( lst is lst_three ) #output True



#explain about ternary operator or conditional operator

#a = 6
#b = 7
#c = 4

#max = a if a > b and a > c else b if b > a and b > c else c
#print(max)

#explain mutability and imutability in python

#lst = [1, 2, 3, 4]
#print('before modification', lst)
#lst[1] = 7777
#print('after modification', lst)


#tup = (1, 2, 3, 4)
#print('before modification', tup)
#tup[1] = 7777 #TypeError tuple object does not support item assignment


 



















