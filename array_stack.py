class ArrayStack:

    def __init__(self):
        self._data = []

    def length(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        self._data.pop()
