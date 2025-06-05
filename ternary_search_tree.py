class TstreeNode:
    """
    Node class for Ternary Search Tree (TST)
    Ecah node holds a single character and other attributes:
    - _lt: left subtree for characters less than current character
    - _eq: middle subtree for th enext character in the string
    - _gt: right subtree for characters greater than current character
    """

    def __init__(self, string):
        """
        Initialize a node with the given character
        :param string: single character stored at this node
        """
        self._string = string
        self._terminates = False  # True if character at this node marks the end of a string
        self._lt, self._eq, self._gt = None, None, None # Left, Equal, and Greater child nodes
   
    def _insert(self, string):
        """
        Insert a string into the Ternary Search
        """
        if string == '':
            self._terminates = True
            return

        first_char = string[0]
        remaining_char = string[1:]

        if self._string == first_char:
            if remaining_char == '':
                self._terminates = True
                return
            if self._eq is None:
                self._eq = TstreeNode(remaining_char[0])
                self._eq._insert(remaining_char)
            else:
                self._eq._insert(remaining_char)
        elif first_char > self._string:
            if self._gt is None:
                self._gt = TstreeNode(first_char)
                self._gt._insert(string)
            else:
                self._gt._insert(string)
        elif first_char < self._string:
            if self._lt is None:
                self._lt = TstreeNode(first_char)
                self._lt._insert(string)
            else:
                self._lt._insert(string)
                
    def _search(self, string, check_prefix = False):
        """
        Search for a string or prefix 
        :param string: string to search
        :param check_prefix: if True, return True if prefix found; else, require exact match
        :return: True if string or prefix found, False otherwise
        """
        if string == '':
            return string == ''
        
        first_char = string[0]
        remaining_char = string[1:]
        
        if first_char == self._string:
            if self._eq == None and remaining_char == '':
                return True
            elif self._eq == None and remaining_char != '':
                return False
            elif (not self._eq == None) and remaining_char == '':
                if self._terminates:
                    return True
                if check_prefix:
                    return True
                else:
                    return False
            else:
                if self._eq:
                    pass
                elif self._gt:
                    pass
                elif self._lt:
                    pass
                return self._eq._search(remaining_char, check_prefix)
        elif first_char > self._string:
            if self._gt == None:
                return False
            else:
                return self._gt._search(string, check_prefix)
        elif first_char < self._string:
            if self._lt == None:
                return False
            else:
                return self._lt._search(string, check_prefix)

    def __str__(self, tab_length = 2):
        """
        String representation of the Ternary Search Tree.
        """
        string = ("     " + " " * tab_length) + "char: " + self._string + ", Terminates: " + str(self._terminates)
        if self._lt:
            string += "\n_lt:" + self._lt.__str__(tab_length + 2)
        if self._eq:    
            string += "\n_eq:" + self._eq.__str__(tab_length + 2)
        if self._gt:
            string += "\n_gt:" + self._gt.__str__(tab_length + 2)
        return string

    def all_strings(self, current_string=''):
        """
        Return a list of all stored in the Ternery Search Tree.
        """
        string = current_string + self._string
        strings = []
        if self._terminates:
            strings.append(string)
        if self._lt:
            strings += self._lt.all_strings(current_string)
        if self._eq:
            strings += self._eq.all_strings(string)
        if self._gt:
            strings += self._gt.all_strings(current_string)
        return strings

    def __len__(self):
        """
        Return the total number of strings stored in the Ternary Search Tree
        """
        length = 1 if self._terminates else 0
        if self._lt:
            length += self._lt.__len__()
        if self._eq:
            length += self._eq.__len__()
        if self._gt:
            length += self._gt.__len__()
        return length      


class TernarySearchTree:

    def __init__(self):
        self._root = None

    def insert(self, string):
        if string == '':
         if self._root._string == '':
            return
        
            old_root = self._root
            new_root = TstreeNode('')
            new_root._gt = old_root
            new_root._terminates = True
            self._root = new_root
            return
        
        if self._root == None:
            self._root = TstreeNode(string[0])
        self._root._insert(string)
        
    def search(self, string, check_prefix = True):
        print(string.upper())
        return self._root._search(string, check_prefix)
    
    def __str__(self):
        if self._root == None:
            return ""

        string = "terminates: "+str(self._root._terminates) + "\n"

        if self._root._string == '':
            if self._root._gt == None:
                return string
            else:
                return string + self._root._gt.__str__()
        return string + self._root.__str__()
        
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        if self._root is None:
            return 0
        if self._root._string == '':
            if self._root._gt == None:
                return 0
            else:
                return 1 + len(self._root._gt)
        else:
            return len(self._root)
        
        
    def all_strings(self):
        if self._root is None:
            return[]
        if self._root._string == '':
            if self._root._gt == None:
                return ['']
            else:
                return[''] + self._root._gt.all_strings()
        return self._root.all_strings()
            