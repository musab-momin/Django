#generate fibonaci series till given Nth number

#iterative approach
# def fib(num):
#     arr = [0, 1]

#     for i in range(1, num+1):
#         tmp = arr[i] + arr[i-1]
#         arr.append(tmp)

#     print(arr)
#     return arr[num]

# ans = fib(15)
# print(ans)


# def fib(num):
#     if num < 2:
#         return num
#     return fib(num - 1) + fib(num - 2)

# def memo(num):
#     record = {}
#     if num in record.keys():
#         return record[num]
#     value = fib(num)
#     record[num] = value
#     return value

# ans = memo(15)
# print( ans )

