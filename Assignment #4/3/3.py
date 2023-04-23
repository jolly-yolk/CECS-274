import BinarySearchTree
q = BinarySearchTree.BinarySearchTree()
q.add(3, "third")
q.add(2, "second")
q.add(1, "first")
q.remove_node(q.r)
q.add(3, "third")
q.add(5, "fifth")
q.add(4, "fourth")

print(q.funcX(6).x)

'''
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
