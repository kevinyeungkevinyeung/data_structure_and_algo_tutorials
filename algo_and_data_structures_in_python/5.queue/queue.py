
# FIFO first item we insert is the first one we take out
class Queue:

    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []
    
    # O(1) constant running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time. How to solve this problem? Doubly linked list
    def dequeue(self):
        if self.queue_size() != 0:
    
            data = self.queue[0]
            del self.queue[0]
            
            return data

    # O(1) constant running time
    def peek(self):
        return self.queue[0]
    
    # O(1) constant running time
    def queue_size(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(F"Size : {queue.queue_size()}")
print(F"Popped item: {queue.dequeue()}") 

print(F"Size : {queue.queue_size()}")
print(F"Peek item: {queue.peek()}") 

print(F"Size : {queue.queue_size()}")