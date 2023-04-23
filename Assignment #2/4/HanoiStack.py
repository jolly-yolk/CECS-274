import numpy as np


class ArrayStack:
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemthods should be implemented. 
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple, 
        s = ArrayStack()
        print(s)
        print(len(s))
    '''
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n):
        return np.zeros(n, object)
    
    def resize(self):
        '''
            Resize the array
        '''
        b = self.new_array(max(0, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i):
        return self.a[i]
    
    def set(self, i, x):
        y = self.a[i]
        self.a[i] = x
        return y
    
    def add(self, i, x) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if self.n == len(self.a):
            self.resize()
        
        for j in range(i+1, self.n + 1):
                self.a[j] = self.a[j - 1]

        self.a[i] = x
        self.n += 1
                      

    def remove(self, i):
        '''
            remove element i and shift all j > i one 
            position to the left
        '''
        if (self.n * 3) < len(self.a):
            self.resize()
        x = self.a[i]

        for j in range(i, self.n - 2):
                self.a[j] = self.a[j+1]       
        self.n -= 1
        return x
        

    def push(self, x) :
        self.add(self.n, x)
    
    def pop(self):
        return self.remove(self.n-1)
        

    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n
        
    def __str__(self):
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
'''
stack = ArrayStack()
print(stack.a)
stack.add(0, 'f')
print(stack.a)
stack.add(0, 'e')
print(stack.a)
stack.add(0, 'b')
print(stack.a)
stack.add(1, 'c')
print(stack.a)
stack.add(2, 'g')
print(stack.a)
stack.remove(3)
print(stack.a)
stack.remove(1)
print(stack.a)
stack.remove(0)
print(stack.a)
stack.push('h')
print(stack.a)
stack.pop()
print(stack.a)
stack.pop()
print(stack.a)
print(f'{stack.a} len(a) = {len(stack.a)} n = {stack.n}')
'''

