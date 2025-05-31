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


                
                
    def _search(self, string):




class TernarySearchTree:

    def __init__(self):
        self._root = None

    def insert(self, string):
           
            