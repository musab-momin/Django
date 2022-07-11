class Stack:
    def __init__(self):
        self.stack = []

    def push(self, entry):
        self.stack.append(entry)
    
    def pop(self):
        self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def print(self):
        print(self.stack)


stack_obj = Stack()

stack_obj.push(20)
stack_obj.push(30)
stack_obj.push(40)


stack_obj.print()

stack_obj.pop()

stack_obj.print()
peeked = stack_obj.peek()
print(peeked)