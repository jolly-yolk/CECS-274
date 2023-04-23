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


    def remove(self):
        if self.n == 0:
            return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        return x

    def size(self):
        return self.n

    def second_last(self):
        if (self.head == self.tail) or (self.head.x == None):
            return None
        x = self.head.x
        u = self.head
        t = True
        while t == True:
            if u == self.tail:
                break
            else:
                x = u.x
                u = u.next
        return x

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
