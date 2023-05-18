# LIFO: last itme we insert is the first itme we take out

class Stack:

    def __init__(self):
        self.stack = []

    # insert item into the stack // O(1)
    def push(self, data):
        self.stack.append(data)

    # remove and return the last item we have insert (LIFO) // O(1)
    def pop(self):

        if self.stack_size() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    # peek: it returns the last itme without removing it // O(1)
    def peek(self):
        return self.stack[-1]
    
    # has O(1) running time
    def is_empty(self):
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)
    
if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(F"Size : {stack.stack_size()}")
    print(F"Popped item: {stack.pop()}") 

    print(F"Size : {stack.stack_size()}")
    print(F"Peek item: {stack.peek()}") 

    print(F"Size : {stack.stack_size()}")
