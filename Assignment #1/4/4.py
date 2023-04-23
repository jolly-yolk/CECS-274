import numpy as np #imports Numpy Array
import heapq as hq #imports HeapQueue

class List():  #creates a class for Lists
    def __init__(self):
        self.nump = np.array([]) #creates a numpy array
        
    def add(self, x):
        self.nump = np.append(self.nump, x) #appends object x to numpy array
        
    def remove(self, i):
        self.nump = np.delete(self.nump, [i]) #removes object at position i
        
    def set(self, i, x):
        self.nump = np.insert(self.nump, i, x) #sets an object x at position i
        
    def get(self, i):
        return self.nump[i] #returns the value at position i
        
    
class USet: #creates a class for USet
    def __init__(self):
        self.numpie = np.array([]) #creates a numpy array

    def add(self, x):
        if x not in self.numpie: #if object does not exist in numpy array
            self.numpie = np.append(self.numpie, x) #appends object x to numpy array
            return True #returns True if object appended
        else: #if object exists in numpy array
            return False #returns False if object was not appened
    def remove(self, x):
        if x in self.numpie: #if object exists in numpy array
            self.numpie = np.delete(self.numpie, [x]) #removes object x from numpy array
        else: #if object does not exist in numpy array
            return x #return object if object not in numpy array
    def find(self, x):
        if x not in self.numpie: #if object not in numpy array
            return x #return object if not in numpy array
    
class SSet: #creates a class for SSet
    def __init__(self):
        self.numpy = np.array([]) #creates a numpy array
        
    def add(self, x):
        if x not in self.numpy: #if object not in numpy array
            self.numpy = np.append(self.numpy, x) #append object if not in numpy array
            self.numpy.sort() #sorts the numpy array so that the Sort Set is Sorted in order
            return True #if object appened return True
        else: #if object in numpy array
            return False #returns False if object in numpy array
        
    def remove(self, x):
        if x in self.numpy: #if object in numpy array
            self.numpy = np.delete(self.numpy, [x]) #removes object from numpy array
        else: #if object not in numpy array
            return x #returns object if not in numpy array

    def size(self):
        return len(self.numpy) #returns the size of the numpy array
        
    def find(self, x):
        t_list = [] #creates a temp list
        hq.heapify(t_list) #heapifys list
        for i in range(len(self.numpy)): #creates a for loop going through the numpy array
                if self.numpy[i] >= x: #if object numpy array[i] is greater than or equal to object x
                    hq.heappush(t_list, self.numpy[i]) #push numpy array[i] into temp list
        if x not in self.numpy: #object x not in numpy array
             return hq.heappop(t_list) #returns the smallest number that is greater than object x
                    
        
#The tests that prove the above classes work run the program to see them properly
#List Test
print('The List Tests:')
print('Initial Numpy Array')
my_list = List()
print(my_list.nump)
print()
print('Add:')
my_list.add(5)
my_list.add(5)
my_list.add(5)
my_list.add(5)
print(my_list.nump)
print()
print('Remove:')
my_list.remove(0)
print(my_list.nump)
print()
print('Set:')
my_list.set(0, 3)
print(my_list.nump)
print(my_list.get(0))
print(my_list.get(3))
print()

#USet Test
print('The USet Test:')
print('Initial Numpy Array')
my_uset = USet()
print(my_uset.numpie)
print()
print('Add:')
my_uset.add(5)
my_uset.add(5)
my_uset.add(3)
my_uset.add(5)
my_uset.add(2)
my_uset.add(3)
print(my_uset.numpie)
print()
print('Remove:')
my_uset.remove(2)
print(my_uset.numpie)
print(my_uset.remove(4))
print()
print('Find:')
print(my_uset.find(3))
print(my_uset.find(6))
print()

#SSet Test
print('The SSet Test:')
print('Initial Numpy Array')
my_sset = SSet()
print(my_sset.numpy)
print()
print('Add:')
for i in range(0, 10):
    my_sset.add(i)
print(my_sset.numpy)
print()
print('Remove:')
my_sset.remove(6)
print(my_sset.numpy)
print()
print('Size:')
print(my_sset.size())
print()
print('Find:')
print(my_sset.find(5))
print(my_sset.find(6))
print()