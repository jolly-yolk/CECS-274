import BinaryTree
import ArrayQueue

class BinarySearchTree:

    def __init__(self, nil = None):
        super().__init__()
        self.n = 0
        self.nil = nil
        self.r = self.nil

    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x, v):
        u = BinaryTree.BinaryTree.Node(x, v)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x): #Node, x = object
        w = self.r
        prev = None
        while (w != None):
            prev = w
            if (x < w.x):
                w = w.left
            elif (x > w.x):
                w = w.right
            else:
                return w
        return prev
        
    def add_child(self, p, u): #bool, u = Node, p = Node
        if (p == None):
            self.r = u #inserting into empty tree
        else:
            if (u.x < p.x):
                p.left = u
            elif (u.x > p.x):
                p.right = u
            else:
                return False #u.x is already in the tree
            u.parent = p
        self.n += 1
        return True

    def funcX(self, x):

        w = self.r

        p = self.nil

        while w is not self.nil: 

            p = w

            if x < w.x:

                w = w.left

            elif x > w.x:

                w = w.right

            else:

                return w

        return p

    def find_eq(self, x): #object, x = object
        w = self.r
        while (w != None):
            if x < w.x:
                w = w.left
            elif (x > w.x):
                w = w.right
            else:
                return w.x
        return None
    
    def find(self, x): #object, x = objects
        w = self.r
        z = None
        while (w != None):
            if (w != None):
                z = w
                w = w.left
            elif (x > w.x):
                w = s.right
            else:
                return w.x
        if (z == None):
            return None
        return z.x
        
    def add(self, key, value): #bool, value = object, key = object
       p = self.find_last(key)
       return self.add_child(p, self.new_node(key, value))
        
    def add_node(self, u): #bool, u = Node
        pass
    
    def splice(self, u): #u = Node
        if (u.left != None):
            s = u.left
        else:
            s = u.right
        if (u == self.r):
            self.r = s
            p = None
        else:
            p = u.parent
            if (p.left == u):
                p.left = s
            else:
                p.right = s
        if (s != None):
            s.parent = p
        self.n -= 1

    def remove_node(self, u): #u = Node
        if (u.left == None) or (u.right == None):
            self.splice(u)
        else:
            w = u.right
            while (w.left != None):
                w = w.left
            u.x = w.x
            self.splice(w)

    def remove(self, x): #bool, x = object
        pass
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)
            
    def in_order(self) :       
        if self.r is not self.nil:
            self.__in_order(self.r)

    def pre_order(self) :       
        if self.r is not self.nil:
            self.__pre_order(self.r)

    def pos_order(self) :       
        if self.r is not self.nil:
            self.__pos_order(self.r)

    def __in_order(self, u) : #u = Node      
        if u.left is not self.nil:
            self.__in_order(u.left)
        print(f"{u.x}: {u.v}")     
        if u.right is not self.nil:
            self.__in_order(u.right)

    def __pre_order(self, u) :  #u = Node
        print(f"{u.x}: {u.v}")     
        if u.left is not self.nil:
            self.__pre_order(u.left)
        if u.right is not self.nil:
            self.__pre_order(u.right)

    def __pos_order(self, u) :  #u = Node
        if u.left is not self.nil:
            self.__pos_order(u.left)
        if u.right is not self.nil:
            self.__pos_order(u.right)
        print(f"{u.x}: {u.v}")
        
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w


    def get_ie(self, x):
        l = ArrayQueue.ArrayQueue()
        u = self.r
        
        if (u.x == x): #if the root is equal to the x
            l.add(u.x) #adds root
            u = u.left #goes to node left of the root
            while (u != None): #this functions adds all the nodes under u
                l.add(u.x)
                if (u.right == u.left != None):
                    u = self.next_node(u)
                if (u.right == u.left == None):
                    break
                
        elif (u.x > x): #if the root is greater than the x
            u = u.left #goes to the node left of u
            while (u != None):
                if (u.x > x): #finds a node less than or equal to x
                    u = u.left   
                if (u.x <= x): #once it finds a node less than or equal to x
                    l.add(u.x) #adds u
                    u = u.left #goes to the left
                    while (u != None): #this functions adds all the nodes under u
                        l.add(u.x)
                        if (u.right == u.left != None):
                            u = self.next_node(u)
                        if (u.right == u.left == None):
                            break

        elif (u.x < x): #the x is greater than the root
            l.add(u.x) #adds the root
            u = u.left #goes to the left of the root and ands all the nodes
            while (u != None):
                l.add(u.x)
                if (u.right == u.left != None):
                    u = self.next_node(u)
                if (u.right == u.left == None):
                    break
            u = self.r.right #goes to the right of the root
            while (u != None):
                if (u.x < x): #if u is less than x it adds u and all the nodes under u
                    if (u.x not in l):
                        l.add(u.x) 
                    o = u
                    u = u.left
                    while (u != None):
                        l.add(u.x)
                        if (u.right == u.left != None):
                            u = self.next_node(u)
                        if (u.right == u.left == None):
                            break
                    u = o.right #goes to the right of the first node in the loop
                    if (u != None):
                        if (u.x >= x):
                            if (u.x == x): #if a node is equal to x it is added
                                l.add(u.x)
                        u = u.left #goes to the node to the left and adds all the childern
                        while (u != None):
                            if (u.x not in l):
                                l.add(u.x)
                            if (u.right == u.left != None):
                                u = self.next_node(u)
                            if (u.right == u.left == None):
                                break
        
        return l
            
                
'''     
q = BinarySearchTree()
q.add(3, "third")
q.add(2, "second")
q.add(1, "first")
print(q.find(2.5))
q.remove_node(q.r)
print(q.find(3))
q.add(3, "third")
q.add(5, "fifth")
q.add(4, "fourth")
print(q.find_eq(3.4))
print(q.find(3.4))
print("In order")
q.in_order()
print("Pre order")
q.pre_order()
print("Pos order")
q.pos_order()
print()
print("Numbers less than or equal to 1:")
print()
print(q.get_ie(1))

print()
print("Numbers less than or equal to 2:")
print()
print(q.get_ie(2))

print()
print("Numbers less than or equal to 5:")
print()
print(q.get_ie(5))
'''
