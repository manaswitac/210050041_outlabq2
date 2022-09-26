# -------------------------- Binary Search Tree ------------------------------

class BSTNode:
    """
    | This is a class which stores information about Node of a Binary Search Tree.
    | This contains the following functions:
    | def __init__(self, info)
    | def __str__(self)    

    :param self: Here self is the object in which given data is stored
    :type self: DoublyLinkedList
    :param info: Data to be stored in self 
    :type info: optional 
    """
    def __init__(self, info):
        """Constructor

        :Example:

        >>> from BST import BSTNode
        >>> L = BSTNode(1) 
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """
        | Returns the data stored in a string form 

        :param self: Here self is the object in which given data is stored
        :type self: SinglyLinkedListNode
        :return: str(self.data)
        :rtype: str 
        :Example:

        >>> from BST import BSTNode
        >>> L = BSTNode("Hi") 
        >>> print(L.__str__())
        Hi
        """
        return str(self.info)

class BinarySearchTree:
    """
    | This is a class which stores information about Node of a Binary Search Tree
    | This contains the following functions:
    | def __init__(self)
    | def insert(self, val)
    | def traverse(self, order)
    | def height(self, root)

    :param self: Here self is the object in which given data is stored
    :type self: BinarySearchTree 
    """
    def __init__(self):
        """Constructor

        :Example:

        >>> from BST import BinarySearchTree
        >>> L = BinarySearchTree()
        """
        self.root = None
    
    def insert(self, val):
        """
        | Inserting into BST   

        :param self: Here self is the object in which given data is stored
        :type self: BinarySearchTree
        :param val: Data to be stored in node
        :type val: optional
        :Example:

        >>> from BST import BinarySearchTree
        >>> L = BinarySearchTree()
        >>> L.insert(1)
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """
        | Traversing through each node of BST  
        | This contains following functions:
        | def preOrder(root)
        | def inOrder(root)
        | def postOrder(root)

        :param self: Here self is the object in which given data is stored
        :type self: BinarySearchTree
        :param order: oreder of traverse
        :type order: str
        :Example:

        >>> from BST import BinarySearchTree
        >>> L = BinarySearchTree()
        >>> L.insert(2)
        >>> L.insert(1)
        >>> L.insert(3)
        >>> L.traverse('PRE')
        2 1 3 
        """
        
        def preOrder(root):
            """
            | Preorder traversal

            :param root: root of tree
            :type root: node
            """
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
              
        def inOrder(root):
            """
            | inorder traversal

            :param root: root of tree
            :type root: node
            """  
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
               
        def postOrder(root):
            """
            | Postorder traversal

            :param root: root of tree
            :type root: node
            """ 
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        """
        | To calculate height of tree

        :param self: Here self is the object in which given data is stored
        :type self: BinarySearchTree
        :param root: root of tree
        :type root: node 
        :return: height
        :rtype: int 
        :Example:

        >>> from BST import BinarySearchTree
        >>> L = BinarySearchTree()
        >>> L.insert(1)
        >>> L.insert(2)
        >>> L.insert(3)
        >>> print(L.height(L.root))
        2
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))
