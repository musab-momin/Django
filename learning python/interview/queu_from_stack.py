#create a functionality of queu using two stacks

class Stack:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self, value):
        self.first_stack.append(value)
    
    def remove(self):
        while len(self.first_stack) > 0:
            self.second_stack.append(self.first_stack.pop(-1))
        
        value_should_be_return = self.second_stack.pop(-1)
        
        while len(self.second_stack) > 0:
            self.first_stack.append(self.second_stack.pop(-1))
        
        return value_should_be_return
    
    def print(self):
        print(self.first_stack)

que = Stack()
que.push('Green')
que.push('Blue')
que.push('Red')

que.print()

removed = que.remove()
print(removed)

que.print()