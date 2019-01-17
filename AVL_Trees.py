
class Node():

    def __init__(self, data):

        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL():

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)          # send the root node

    def insertNode(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild)) + 1

        return self.settleViolations(data, node)             # to check for AVL Violations. We are passing the root node

    def settleViolations(self, data, node):                  # node is the root node

        balance = self.calcBalance(node)

        # case 1: doubly left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Doubly left heavy situation....")
            return self.rotateRight(node)
            # we always perform the rotation on the root node in the main tree or sub-trees.
            # Thats why we have to check for the AVL properties after each INSERTION

        # case 2: doubly right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print("Doubly right heavy situation....")
            return self.rotateLeft(node)

        # case 3: left-right heavy situation
        if balance > 1 and data > node.leftChild.data:
            print("Left-Right heavy situation....")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # case 4: right-left heavy situation
        if balance < -1 and data < node.rightChild.data:
            print("Right-Left heavy situation....")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node
    
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)
            
    def removeNode(self,data,node):

        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)  # why initialised to leftchild is because at the end either the left or the right child will be removed
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node....")
                del node
                return None

            if not node.leftChild:                                  # No left child- only a single right child
                print("Removing a node with a single right child.....")
                tempNode = node.rightChild
                del node
                return tempNode                                     # exit from function and return the new node in the previous node's position
            elif not node.rightChild:
                print("Removing a node with a single left child.....")
                tempNode = node.leftChild
                del node
                return tempNode                                     # exit from function and return the new node in the previous node's position

            print("Removing a node with two children.....")
            tempNode = self.getPredecessor(node.leftChild)          # the node we want to remove has a predecessor in its left tree, the right sub-tree will be larger than the current node
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild) # we want to remove the temNode data because it is already swapped( we want it to be recursive because it can fall into any of the previous cases

        node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1
        
        balance = self.calcBalance(node)

        # case 1: doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            print("Doubly left heavy situation....")
            return self.rotateRight(node)
            
        # case 2: doubly right heavy situation
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            print("Doubly right heavy situation....")
            return self.rotateLeft(node)

        # case 3: left-right heavy situation
        if balance > 1 and self.calcHeight(node.leftChild) < 0:
            print("Left-Right heavy situation....")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # case 4: right-left heavy situation
        if balance < -1 and self.calcHeight(node.rightChild) > 0:
            print("Right-Left heavy situation....")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node                                                  # returning the main root node

    def getPredecessor(self,node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
    
    def traverse(self):

        if self.root:
            self.traverseInorder(self.root)
            
    def traverseInorder(self, node):

         if node.leftChild:
             self.traverseInorder(node.leftChild)

         print("%s" % node.data)

         if node.rightChild:
             self.traverseInorder(node.rightChild)
             
    def calcHeight(self, node):

        if not node:
            return -1
        
        return node.height
    

    # If this method returns >1, it means it is a left heavy situation --> RIGHT ROTATION
    # If this method returns <-1, it means it is a right heavy situation --> LEFT ROTATION
    def calcBalance(self, node):

        if not node:
            return 0

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
 
    def rotateRight(self, node):

        print("Roatating to the right on node" , node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1
        tempLeftChild.height =  max( self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild) ) + 1

        return tempLeftChild                                    # the new node in the previous node's position

    def rotateLeft(self, node):

        print("Roatating to the left on node" , node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1
        tempRightChild.height =  max( self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild) ) + 1

        return tempRightChild                                   # the new node in the previous node's position
    
    

avl = AVL()

avl.insert(9)
avl.insert(6)
avl.insert(10)
avl.insert(3)
avl.insert(8)
avl.insert(5)

avl.remove(6)
avl.traverse()
