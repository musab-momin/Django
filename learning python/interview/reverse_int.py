#my approach

def reverse_int(num):
    result = ""
    for i in str(num):
        if i != "-" and i != '0':
            result = i + result
    
    result = int(result)
    if num > 0:
        print(result)
    else:
        print(result*-1)


test = -4500
reverse_int(test)