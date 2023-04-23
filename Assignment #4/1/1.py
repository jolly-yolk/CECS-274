import BinaryTree

tree = BinaryTree.BinaryTree()
tree.r = tree.Node('Node 1')
r = tree.r
r.v = 'a'

r.insert_right()
r.right.x = 'Node 3'
r.right.v = 'c'

r.insert_left()
r.left.x = 'Node 2'
r.left.v = 'b'

r.right.insert_right()
r.right.right.x = 'Node 7'
r.right.right.v = 'g'

r.right.insert_left()
r.right.left.x = 'Node 6'
r.right.left.v = 'f'

r.left.insert_right()
r.left.right.x = 'Node 5'
r.left.right.v = 'e'

r.left.insert_left()
r.left.left.x = 'Node 4'
r.left.left.v = 'd'

print(f'Height of node left of root: {tree._height(r.left)}')
print(f'Height of node left of root: {tree.height2(r.left)}')
print()
print(f'Height of root: {tree.height()}')
print(f'Height of root: {tree.height2(r)}')
print()
print(f'Height of node left of the left of the root: {tree._height(r.left.left)}')
print(f'Height of node left of the left of the root: {tree.height2(r.left.left)}')
print()
print(f'Height of node left of the right of the root: {tree._height(r.right.left)}')
print(f'Height of node left of the right of the root: {tree.height2(r.right.left)}')
print()

r.right.right.insert_right()
r.right.right.right.x = 'Node 15'
r.right.right.right.v = 'g'

print('Inserted element right to the right of the right of the root')
print()
print(f'Height of root: {tree.height()}')
print(f'Height of root: {tree.height2(r)}')
print()
print(f'Height of the right of the right of the root: {tree._height(r.right.right)}')
print(f'Height of the right of the right of the root: {tree.height2(r.right.right)}')
print()

r.left.right.insert_left()
r.left.right.left.x = 'Node 10'
r.left.right.left.v = 'u'

print('Inserted element left to the right of the left of the root')
print()
print(f'Height of root: {tree.height()}')
print(f'Height of root: {tree.height2(r)}')
print()
print(f'Height of the right of the left of the root: {tree._height(r.left.right)}')
print(f'Height of the right of the left of the root: {tree.height2(r.left.right)}')

'''
the function height2 will run in O(n) time because it must look at all the number of childern to determine the height of the node (u) relative to the lowest child.
'''
