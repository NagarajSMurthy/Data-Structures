
class Node():

    def __init__(self,data):
        self.data = data
        self.leftChild = None                       # left node
        self.rightChild = None                      # right node

class BinarySearchTree():

    def __init__(self):
        self.rootNode = None

    def insert(self,data):
        if self.rootNode is None:
            self.rootNode = Node(data)              # Instantiate
        else:
            self.insertNode(data,self.rootNode)     # All the data are accessed through ROOT NODE
    # O(logN) time complexity (if the tree is balanced otherwise O(N)time complexity
    def insertNode(self,data,node):                 # node is an object
        if data < node.data:                        # data is less then the root node, so go left
            if node.leftChild:                      # if node.leftChild is not equal to none
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:                     # if node.rightChild is not equal to none
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)

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

            if not node.leftChild:   # No left child- only a single right child
                print("Removing a node with a single right child.....")
                tempNode = node.rightChild
                del node
                return tempNode # exit from function
            elif not node.rightChild:
                print("Removing a node with a single left child.....")
                tempNode = node.leftChild
                del node
                return tempNode # exit from function

            print("Removing a node with two children.....")
            tempNode = self.getPredecessor(node.leftChild) # the node we want to remove has a predecessor in its left tree, the right sub-tree will be larger than the current node
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild) # we want to remove the temNode data because it is already swapped( we want it to be recursive because it can fall into any of the previous cases
        return node

    def remove(self,data):
        if self.rootNode:
            self.rootNode = self.removeNode(data, self.rootNode)
            
    def getPredecessor(self,node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
    
    def getMin(self):
        if self.rootNode:
            node = self.rootNode
            while node.leftChild is not None:
                node = node.leftChild

        return node.data

    def getMax(self):
        if self.rootNode:
            node = self.rootNode
            while node.rightChild is not None:
                node = node.rightChild

        return node.data

    def traverse(self):    # traversing always takes O(N) time complexity
        if self.rootNode:
            #print("j")
            self.traverseInOrder(self.rootNode)

    def traverseInOrder(self,node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
            
        print("%s" %node.data)
        
        if node.rightChild:
            self.traverseInOrder(node.rightChild)
            

bst = BinarySearchTree()

bst.insert(32)
bst.insert(10)
bst.insert(55)
bst.insert(79)
bst.insert(19)
bst.insert(1)
bst.insert(16)
bst.insert(23)

#print(bst.getMin())
bst.traverse()

bst.remove(32)
bst.traverse()


            
