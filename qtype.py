
class Queue():

    def __init__(self):      
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def Enq(self, item):          # Enqueue operation
        self.queue.append(item)

    def Deq(self):                # Dequeue operation
        data = self.queue[0]      # 0 will be the index of the first element inserted and Copy the value to a variable
        del self.queue[0]         # delete the actual value from the array(list)
        return data               # returns the data (variable)

    def peek(self):
        return self.queue[0]

    def QSize(self):
        return len(self.queue)


myq = Queue()

myq.Enq(10)
myq.Enq(20)
myq.Enq(30)
myq.Enq(40)
myq.Enq(50)
myq.Enq(100)

print(myq.QSize())

print(myq.Deq())     # returns the data and also deletes from the queue
print(myq.Deq())

print(myq.peek())    # Only returns the data

print(myq.QSize())
