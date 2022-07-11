test = "reversethisthing"
ans = ''

#solution 2
#for i in range(len(test)-1, -1, -1):
#    ans = ans + test[i]


#solution 1
for i in test:
    ans = i + ans


print(test[::-1])
print(ans)
