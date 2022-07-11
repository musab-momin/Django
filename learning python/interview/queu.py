class Queu:
    def __init__(self):
        self.que = []
    
    def add(self, inp):
        self.que.append(inp)
    
    def remove(self):
        return self.que.pop(0)

    def peek(self):
        return self.que[0]

    def wieve(self, source_one, source_two):
        combination = []

        flag = False
        while(flag==False):
            first = source_one.pop(0)
            second = source_two.pop(0)
            combination.append(first)
            combination.append(second)
            if(len(source_one) ==  0):             
                flag = True
                for i in source_two:
                    combination.append(i)
            if(len(source_two) == 0):
                flag = True
                for i in source_one:
                    combination.append(i)
        return combination
            
    def print(self):
        print(self.que)



obj = Queu()
obj.add(34)
obj.add(45)
obj.add(68)

combined_lst = obj.wieve([1, 2, 3], ['hi'])
print(combined_lst)

# tmp = obj.peek()
# print(tmp)

# re = obj.remove()
# tmp = obj.remove()
# print(re, tmp)

#obj.print()
