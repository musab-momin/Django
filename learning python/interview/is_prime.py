#Take a input of int number and find out whether the number is prime number or not
#A number is prime if it is only divisible by 1 and it self


#solution: we iterate from 2 to n-1 and between these number if n is divisible by any number it means it is not a prime number if it is not
#divisible by any number it means it is a prime number but there is problem with our solution bcoz it is not so effient let's 
#make it effieient. We are going to iterate through from 2 to square root why lets take a example.

#if the n = 36 it is has following divisor 
# 1 2 3 6 9 12 18 36

#If we divide them into two groups one group is from 1 to square root of n and other is rest of them. If we notice they are equal means
#both the groups has same amount of number which is 4. by that we understand if we don't find the divisor till square root it means we 
#don't find divisor above the square root. So we have to loop from 2 to square root.  

import math


def find_is_prime(n):
    if n < 2:
        return False

    limit = int(math.sqrt(n))

    for i in range(2, limit+1):
        if n % i == 0:
            return False
    
    return True


inp = int(input('>'))
print(find_is_prime(inp))