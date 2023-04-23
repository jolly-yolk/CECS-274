import numpy as np


class DLList:
    class Node:
        def __init__(self, x) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def absorb(self, u):
        for i in range(u.n, 0, -1):
            self.add_before(self.get_node(self.n), u.get(u.n - i))
            u.remove(u.n - i)
            

    def check_size(self):
        i = 0
        for i in range(self.n):
            i += 1
        i += 1
        if i != self.n:
            return 'Elements and Nodes are Unequal'
        else:
            pass
        
   
    def get_node(self, i):
        if (i < self.n/2):
            p = self.dummy.next
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n - i):
                p = p.prev
        return p
        
    def get(self, i):
        return self.get_node(i).x

    def set(self, i, x):
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
            
    def add(self, i, x):
        self.add_before(self.get_node(i), x)

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
    
    def remove(self, i):
        self._remove(self.get_node(i))

    def size(self):
        return self.n

    def append(self, x)  :
        self.add(self.n, x)

    def is_Palindrome(self):
        k = 0
        b = 1
        if self.n == 0:
            return self
        for i in range(self.n // 2):
            y = self.get_node(0 + k) # beginning
            x = self.get_node(self.n - b) # end
            a = x.x #store end value
            x.x = y.x #make end value beginning value
            y.x = a # make beginning value stored end value
            k += 1 #increment to change index of beginning and end value
            b += 1
            if x.x == y.x:
                continue
            else:
                return False
        return True

    def reverse(self):
        k = 0
        b = 1
        if self.n == 0:
            return self
        for i in range(self.n // 2):
            y = self.get_node(0 + k) # beginning
            x = self.get_node(self.n - b) # end
            a = x.x #store end value
            x.x = y.x #make end value beginning value
            y.x = a # make beginning value stored end value
            k += 1 #increment to change index of beginning and end value
            b += 1

         
    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input: 
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            raise "Not implemented. Please use the references next and prev"
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

