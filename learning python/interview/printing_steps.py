#My approach
# def steps(num):
#     for i in range(1, num+1):
#         space = "-" * (num-i)
#         print(("#" * i)+space)

#solution from tutor

# # def steps(num):
#     for row in range(num):
#         space = ""
#         for column in range(num):
#             if column <= row:
#                 print("#", end="")
#             else:
#                 space+="-"  
#         print(space)


#recursion practice
# def recursion(num):
#     if num == 0:
#         return
#     print(num)
#     return recursion(num-1)


steps(3)