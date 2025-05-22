class TstreeNode:

    def __init__(self, string):
        self._string = string
        self._lt, self._eq, self._gt = None, None, None

        
   
    def _insert(self, string):
        if string == self._string:
            if self._eq is None:
                self._eq = TstreeNode(string)
            else:
                self._eq._insert(string)
        elif string < self._string:
            if self._lt is None:
                self._lt = TstreeNode(string)
            else:
                self._lt._insert(string)
        elif string > self._string:
            if self._gt is None:
                self._gt = TstreeNode(string)
            else:
                self._gt._insert(string)