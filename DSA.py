################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------
class SinglyLinkedListNode:
    """
    | This is a class which stores information about Node of a SinglyLinkedList.
    | This contains the following functions:
    | def __init__(self, data)
    | def __str__(self)

    :param self: Here self is the object in which given data is stored
    :type self: SinglyLinkedListNode
    :param data: Information stored in node
    :type data: optional
    """
    def __init__(self, data):
        """Constructor

        :Example:

        >>> from DSA import SinglyLinkedListNode
        >>> L = SinglyLinkedListNode(1)
        """
        self.data = data
        self.next = None
    
    
    def __str__(self):
        """
        | Returns the data stored in a string form 

        :param self: Here self is the object in which given data is stored
        :type self: SinglyLinkedListNode
        :return: str(self.data)
        :rtype: str
        :Example:

        >>> from DSA import SinglyLinkedListNode
        >>> Node = SinglyLinkedListNode("Hi")
        >>> print(Node.__str__())
        Hi
        """
        return str(self.data)

class SinglyLinkedList:
    """
    | This is a class which stores information about Singly Linked List.
    | This contains the following functions:
    | def __init__(self)
    | def insert(self, data)
    | def find(self, data)
    | def deleteVal(self, data)
    | def printer(self, sep = ', ') 
    | def reverse(self)    

    :param self: Here self is the object in which given data is stored
    :type self: SinglyLinkedList
    """   
    def __init__(self):
        """Constructor

        :Example:

        >>> from DSA import SinglyLinkedList
        >>> L = SinglyLinkedList()
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """
        | Insert data into Singly Linked List

        :param self: Here self is the object in which given data is stored
        :type self: SinglyLinkedList
        :param data: Information stored in node
        :type data: optional
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> L = SinglyLinkedList()
        >>> L.insert(2)
        >>> L.insert(1)
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    
    def find(self, data):
        """
        | Searches for data in Singly Linked List

        :param self: Here self is the object in which given data is stored
        :type self: SinglyLinkedList
        :param data: Information stored in node
        :type data: optional
        :return: Node at which data is stored
        :rtype: SinglyLinkedListNode 
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> L = SinglyLinkedList()
        >>> L.insert(2)
        >>> L.insert(1)
        >>> A = L.find(1)
        >>> print(A.__str__())
        2
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """
        | Delete vals    

        :param self: Here self is the object in which given data is stored
        :type self: SinglyLinkedList
        :param data: Information stored in node
        :type data: optional
        :return: True
        :return: False
        :rtype: bool 
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> L = SinglyLinkedList()
        >>> L.insert(2)
        >>> L.insert(1)
        >>> L.deleteVal(1)
        True
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next.next = prevPos.next
        return True
    
    def printer(self, sep = ', '):
        """
        | prints Singly Linked List 

        :param self: Here self is the object in which given data is stored
        :type self: SinglyLinkedList
        :param sep: Separator, defaults to ', '
        :type sep: str
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> L = SinglyLinkedList()
        >>> L.insert(2)
        >>> L.insert(1)
        >>> L.printer()
        [2, 1]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """
        | Reverse the Singly Linked List  

        :param self: Here self is the object in which given data is stored
        :type self: SinglyLinkedList
        :Example:

        >>> from DSA import SinglyLinkedList
        >>> L = SinglyLinkedList()
        >>> L.insert(2)
        >>> L.insert(1)
        >>> L.reverse()
        >>> L.printer()
        [1, 2]
        """ 
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    """
    Merges two Singly Linked Lists

    :param list1: List to be merged 
    :type list1: SinglyLinkedList
    :param list2: List to be merged
    :type list2: SinglyLinkedList    
    :return: merged 
    :rtype: SinglyLinkedList
    :Example:

    >>> from DSA import SinglyLinkedList
    >>> from DSA import merge
    >>> L = SinglyLinkedList()
    >>> L.insert(2)
    >>> L2 = SinglyLinkedList()
    >>> L2.insert(2)
    >>> L.insert(1)
    >>> L.reverse()
    >>> L2 = merge(L,L2)
    >>> L2.printer()
    [1, 2, 2]
    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """
    | This is a class which stores information about Node of a Doubly Linked List.
    | This contains the following functions:
    | def __init__(self, data)
    | def __str__(self)    

    :param self: Here self is the object in which given data is stored
    :type self: DoublyLinkedListNode
    :param data: Information stored in node
    :type data: optional     
    """
    def __init__(self, data):
        """Constructor

        :Example:

        >>> from DSA import DoublyLinkedListNode
        >>> L = DoublyLinkedListNode(1)
        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """Returns the data stored in a string form  

        :param self: Here self is the object in which given data is stored
        :type self: DoublyLinkedListNode
        :return: str(self.data)
        :rtype: str 
        :Example:

        >>> from DSA import DoublyLinkedListNode
        >>> L = DoublyLinkedListNode("Hi")
        >>> print(L.__str__())
        Hi
        """ 
        return str(self.data) 

class DoublyLinkedList:
    """
    | This is a class which stores information about Node of a Doubly Linked List
    | def __init__(self)
    | def insert(self, data)
    | def printer(self, sep = ', ')
    | def reverse(self)

    :param self: Here self is the object in which given data is stored
    :type self: DoublyLinkedList        
    """
    def __init__(self):
        """Constructor

        :Example:

        >>> from DSA import DoublyLinkedList
        >>> L = DoublyLinkedList()
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """
        | Inserting into doubly linked list 

        :param self: Here self is the object in which given data is stored
        :type self: DoublyLinkedList
        :param data: Information stored in node
        :type data: optional   
        :Example:

        >>> from DSA import DoublyLinkedList
        >>> L = DoublyLinkedList()
        >>> L.insert(1) 
        >>> L.insert(2)    
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """
        | Prints the Doubly Linked List  

        :param self: Here self is the object in which given data is stored
        :type self: DoublyLinkedList
        :param sep: Separator, defaults to ', '
        :type sep: str
        :Example:

        >>> from DSA import DoublyLinkedList
        >>> L = DoublyLinkedList()
        >>> L.insert(2)
        >>> L.printer()
        [2]
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """
        | Reverses the dounbly linked list

        :param self: Here self is the object in which given data is stored
        :type self: DoublyLinkedList
        :Example: 

        >>> from DSA import DoublyLinkedList
        >>> L = DoublyLinkedList()
        >>> L.insert(1) 
        >>> L.insert(2)
        >>> L.reverse()
        >>> L.printer()
        [2, 1]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev

