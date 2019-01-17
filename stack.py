
class Stack():

    def __init__(self):
        self.stack = []

    def IsEmpty(self):
        return self.stack == []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        data = self.stack[-1]        # -1 will be the index of the top of the stack
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def StackSize(self):
        return len(self.stack)



mystack = Stack()

mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.push(50)
mystack.push(100)

print("The stack size is",mystack.StackSize())

print(mystack.peek())  # Returns the item in the top of the stack
print(mystack.pop())   # Returns the item from the top of the stack and also deletes it
print(mystack.pop())

print("The stack size is",mystack.StackSize())
