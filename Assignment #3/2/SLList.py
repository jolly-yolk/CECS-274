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
    

    def add_index(self, i, x):
        u = SLLQueue.Node(x)
        w = self.head
        if self.n == 0:
            return None
        if i == self.n - 1:
            self.add(x)
        else:
            self.tail.next = SLLQueue.Node(self.tail.x)
            self.tail = self.tail.next
            w = self.get(i)
            for k in range(i, self.n - 1):
                w.next.next.x = w.next.x
            w.next.x = w.x
            w.x = u.x
        self.n += 1
        
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
    
    def remove_index(self, i):
        if self.n == 0:
            return None
        if (i == self.n - 1):
            u = self.get(i - 1)
            self.tail = u
            self.tail.next = None
        else:
            u = self.get(i)
            for i in range(i, self.n - 1):
                u.x = u.next.x
                u = u.next
            u = self.get(self.n - 2)
            self.tail = u
            self.tail.next = None   
        self.n -= 1

    def set(self, i, x):
        u = self.get(i)
        u.x = x

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
