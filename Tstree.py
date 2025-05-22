class Tstree:

    def __init__(self):
        self._root = None

    def insert(self, string):
        if self._root is None:
            self._root = Tstree(string)
        else:
            self._root._insert(string)