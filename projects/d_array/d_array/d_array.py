import ctypes 

class DynamicArray():
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self._A  = self.make_array(self.capacity)
        
    def get_item(self, k):
        if not 0 <= k < self.n:
            print("Index Error")
        return self._A[k]
    
    def _len(self):
        return self.n
    
    def _append(self, obj):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        self._A[self.n] = obj
        self.n += 1
        
    def resize(self, c):
        B = self.make_array( c)
        for i in range(self.n):
            B[i] = self._A[i]
        self._A = B
        self.capacity = c
        
    def make_array(self, c):
        return (c * ctypes.py_object)()