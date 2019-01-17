class Node():

    def __init__(self, character):
        self.character = character
        self.leftNode = None
        self.rightNode = None
        self.middleNode = None
        self.value = 0


class TST():

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.putItem(self.root, key, value, 0)

    def putItem(self, node, key, value, index):

        c = key[index]

        if node == None:
            node = Node(c)

        if c < node.character:
            node.leftNode = self.putItem(node.leftNode, key, value, index)   # No index increment because we consider the same charcter
        elif c > node.character:
            node.rightNode = self.putItem(node.rightNode, key, value, index) # No index increment because we consider the same charcter
        elif index < len(key) - 1:                                           # index starts from 0 thats why "-1". To check we are not at the end of the key
            node.middleNode = self.putItem(node.middleNode, key, value, index+1) # Increment index because the next character has to be inserted under the previous one
        else:
            node.value = value                                               # we are at the end of the key (after last character), so insert value.

        return node

    def get(self, key):
        node = self.getItem(self.root, key, 0)

        if node == None:
            return -1

        return node.value
    
    def getItem(self, node, key, index):
        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.getItem(node.leftNode, key, index)
        elif c > node.character:
            return self.getItem(node.rightNode, key, index)
        elif index < len(key) - 1:
            return self.getItem(node.middleNode, key, index+1)
        else:
            return node

if __name__ == "__main__":

    tst = TST()

    tst.put("apple", 100)
    tst.put("orange", 200)

    print(tst.get("apple"))
        
    
