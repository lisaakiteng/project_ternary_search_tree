class TstreeNode:

    def __init__(self, string):
        self._string = string
        self.terminates = False
        self._lt, self._eq, self._gt = None, None, None
        
   
    def _insert(self, string):
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

    def __str__(self, tab_length=2):
            string = ("     " + " " * tab_length) + "char: " + self._string + ", Terminates: " + str(self._terminates)
            if self._lt:
                string += "\n_lt:" + self._lt.__str__(tab_length + 2)
            if self._eq:    
                string += "\n_eq:" + self._eq.__str__(tab_length + 2)
            if self._gt:
                string += "\n_gt:" + self._gt.__str__(tab_length + 2)
            return string

    def __len__(self):
            if self._terminates:
                return 1
            length = 0
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
           
            