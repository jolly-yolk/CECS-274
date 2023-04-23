import numpy as np

class SLLQueue:
    class Node:
        def __init__(self, x):
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
        
    def add(self, x) :
        u = SLLQueue.Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True
    
    def check_size(self):
        i = 0
        for i in range(self.n):
            i += 1
        if i != self.n:
            return 'Elements and Nodes are Unequal'
        else:
            pass

    def get(self, i):
        u = self.head
        for k in range(0, i):
            u = u.next
        return u

    def remove(self):
        if self.n == 0:
            return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        return x
    
    def reverse(self):
        k = 0
        b = 1
        if self.n == 0:
            return self
        for i in range(self.n // 2):
            y = self.get(0 + k) # beginning
            x = self.get(self.n - b) # end
            a = x.x #store end value
            x.x = y.x #make end value beginning value
            y.x = a # make beginning value stored end value
            k += 1 #increment to change index of beginning and end value
            b += 1
            
            
            
    def size(self):
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
