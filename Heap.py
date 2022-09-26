class Heap:
    """
    | This is a conceptual class representation of a Heap. 
    | First it has a constructor. It contains some essential functions
    | like parent, left, right, insert, min, Heapify, deleteMin.
    | This contains following function:
    | def _init_(self, cap)
    | def parent(self, i)
    | def left(self, i)
    | def right(self, i)
    | def insert(self, val)
    | def min(self)
    | def Heapify(self, root)
    | def deleteMin(self)     
    """
    def __init__(self, cap):
        """
        | Constructor defined

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :param cap: This parameter to store in heap
        :type cap: optional 
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)                   
        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """
        | Returns the parent of i in the heap

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :param i: Parameter provided while calling
        :type i:  int
        :return: a value int((i-1)/2)
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)
        >>> L.insert(3)
        >>> L.insert(2)
        >>> L.insert(1)
        >>> print(L.parent(3))
        1
        """
        return (i - 1)//2
    
    def left(self, i):
        """
        | Returns the left of i in the heap

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :param i: Parameter provided while calling
        :type i:  int
        :return: a value 2*i + 1
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)
        >>> L.insert(3)
        >>> L.insert(2)
        >>> L.insert(1)
        >>> print(L.left(3))
        7
        """
        return (2 * i) + 1
    
    def right(self, i):
        """
        | Returns the right of i in the heap

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :param i: Parameter provided while calling
        :type i:  int
        :return: a value 2*(i+1)
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)
        >>> L.insert(3)
        >>> L.insert(2)
        >>> L.insert(1)
        >>> print(L.right(3))
        8
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """
        | Inserts val into heap

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :param i: Parameter provided while calling
        :type i:  int
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)
        >>> L.insert(3)
        >>> L.insert(2)
        >>> L.insert(1)
        >>> print(L.H)
        [1, 3, 2]
        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """
        | Returns the min of heap in the heap

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :return: a value self.H[0] or -1
        :rtype: int
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)
        >>> L.insert(3)
        >>> L.insert(2)
        >>> L.insert(1)
        >>> print(L.min())
        1
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """
        | Creates heapify

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :param root: Used to call left, right
        :type root: int
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)
        >>> L.insert(3)
        >>> L.insert(2)
        >>> L.insert(1)
        >>> print(L.Heapify(1))
        None
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """
        | Used do deleteMin in the heap

        :param self: Here self means implement storing the provided information into heap created
        :type self: Heap
        :Example:

        >>> from Heap import Heap
        >>> L = Heap(10)
        >>> L.insert(3)
        >>> L.insert(2)
        >>> L.insert(1)
        >>> L.deleteMin()
        >>> print(L.H)
        [2, 3, 2]
        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.Heapify(0)