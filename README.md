# Data-Structures
This repository contains various data structures such as Linked lists, queues and many more implemented in Python language.

### Linked Lists - 
They are composed of nodes and references pointing from one node to the other. The last will always point to a Null. A linked list can be single (reference to next node only) or double (references to both previous and next nodes). They are used in the implementation of some of the abstract data types like stacks and queues. 

### Stacks and Queues - 
These are abstract data types which can be implemented either with arrays or linked lists. 
Stack has a LIFO(Last In First Out) structure and supports operations like push(), pop() and peek().
Queue has a FIFO(First In First Out) structutre and supports operations like enqueue(), dequeue() and peek().

### Binary Search Trees(BST) - 
Arrays and linked lists have their own time complexities for various operations. BST's have a logarithmic time complexity, O(logN) for most of the operations and are a bit fast compared to arrays and linked lists. BST's have nodes that contain data and are interconnected via edges. Each node exactly contains two child nodes and all the nodes are accessed through root nodes.The time complexity of BST operations depends on the height of the tree. To achieve the logarithmic time complexity, a tree must be balanced. 

### AVL Trees - 
These are balanced binary trees and always have logarithmic time complexity. To maintain the balanced state of the tree, the tree is checked regularly after every operations and if it is unbalanced, rotations are made to make it balanced again.

