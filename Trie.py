# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """
    | This is a class which stores information about Trie
    | def __init__(self)
    | def find(self, root, c)
    | def insert(self, s)
    | def checkPrefix(self, s)
    | def countPrefix(self, s)

    :param self: Here self is the object in which given data is stored
    :type self: Trie 
    """
    def __init__(self):
        """Constructor

        :Example:

        >>> from Trie import Trie
        >>> L = Trie()
        """
        self.T = {}
    
    def find(self, root, c):
        """
        | To find a character in trie 

        :param self: Here self is the object in which given data is stored
        :type self: Trie
        :param root: Root of trie 
        :type root: set 
        :param c: Node of trie
        :type c: optional
        :Example:

        >>> from Trie import Trie
        >>> L = Trie()
        >>> L.insert({1})
        >>> L.insert({2})
        >>> L.insert({3})
        >>> print(L.find(L.T,3))
        True
        """
        return (c in root)
    
    def insert(self, s):
        """
        | Insert S in into trie 

        :param self: Here self is the object in which given data is stored
        :type self: Trie 
        :param s: set to insert
        :type s: set
        :Example:

        >>> from Trie import Trie
        >>> L = Trie()
        >>> L.insert({1})
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """
        | checks whether prefix is present in s or not

        :param self: Here self is the object in which given data is stored
        :type self: Trie
        :param s: prefix set
        :type s: set
        :Example:

        >>> from Trie import Trie
        >>> L = Trie()
        >>> L.insert({1})
        >>> L.insert({2})
        >>> L.insert({3}) 
        >>> print(L.checkPrefix({4}))
        False
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """
        | Counts no of occurences

        :param self: Here self is the object in which given data is stored
        :type self: Trie
        :param s: prefix set
        :type s: set 
        :Example:

        >>> from Trie import Trie
        >>> L = Trie()
        >>> L.insert({1})
        >>> L.insert({2})
        >>> L.insert({3})
        >>> L.insert({3})
        >>> print(L.countPrefix({3}))
        2
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0        