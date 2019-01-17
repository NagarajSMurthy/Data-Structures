
class Node():

    def __init__(self,data):

        self.data = data
        self.nextNode = None
       


class linkedlist():

    def __init__(self):

        self.head = None
        self.size = 0
        self.dataList = []

    def insertNode(self,data):                  # O(1) time complexity

        self.size = self.size+1
        self.dataList.append(data)
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def Size(self):                             # This method has O(1) time complexity
        #print(self.size)
        return self.size

    def Size2(self):                            # This method has O(N) time complexity

        actualNode = self.head
        size = 0

        while actualNode is not None:
            size = size+1
            actualNode = actualNode.nextNode
        #print("The size of the list is " + str(size))
        return size

    def insertEnd(self,data):                   # O(N) time complexity

        self.size = self.size+1                 # Update the size
        newNode = Node(data)                    # Instantiate and create the node
        actualNode = self.head

        while actualNode.nextNode is not None:  # To locate the end Node
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode           # Place the node in the linkedlist

    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:           # points to the null

            print("%d\n" % actualNode.data)
            actualNode = actualNode.nextNode

    def removeNode(self,data):

        if self.head == None:                   # To check if the list is empty
            return                              # exit, if empty
        if data not in self.dataList:
            print('Data not in the linked list')
        self.size = self.size + 1               # Update the size

        currentNode = self.head 
        previousNode = None
        try:
            
            while currentNode.data != data:
    
                previousNode = currentNode  
                currentNode = currentNode.nextNode
    
            if previousNode == None:                # If the root node has to be removed
                self.head = currentNode.nextNode
    
            else:
                previousNode.nextNode = currentNode.nextNode
        except AttributeError:
            pass
            
            
Mylist = linkedlist()

Mylist.insertNode(10)
Mylist.insertNode(35)
Mylist.insertNode(67)
Mylist.insertNode(89)
Mylist.insertNode(341)



#Mylist.Size()  # O(1)
#Mylist.Size2() # O(N)
print(Mylist.Size())  # O(1)
print(Mylist.Size2()) # O(N)
print("The size of the list is " + str(Mylist.Size2()))

Mylist.insertEnd(671)
print("The size of the list is " + str(Mylist.Size2()))

Mylist.traverseList()

Mylist.removeNode(20)
print("The size of the list is " + str(Mylist.Size2()))

Mylist.traverseList()        
        
