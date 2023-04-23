import BinaryTree

tree = BinaryTree.BinaryTree()
tree.r = tree.Node('Node 1')
r = tree.r
r.v = '1'

r.insert_left()
r.left.x = 'Node 2'
r.left.v = '2'

r.insert_right()
r.right.x = 'Node 3'
r.right.v = '3'

r.left.insert_left()
r.left.left.x = 'Node 4'
r.left.left.v = '4'

r.left.insert_right()
r.left.right.x = 'Node 5'
r.left.right.v = '5'

r.right.insert_left()
r.right.left.x = 'Node 6'
r.right.left.v = '6'

r.right.insert_right()
r.right.right.x = 'Node 7'
r.right.right.v = '7'

print(f'Is the tree balanced?:')
print()
if (tree.is_balanced() == True):
    print('Is Balanced')
else:
    print(tree.is_balanced())
    print('Is Not Balanced')
    
print()
print(f'After inserting an element on the left of the tree is it still balanced?:')
print()
r.left.left.insert_left()
r.left.left.left.x = 'Node 8'
r.left.left.left.v = '8'

if (tree.is_balanced() == True):
    print('Is Balanced')
else:
    print('Is Not Balanced')
    
print()
print(f'After inserting an element on the left of the tree again is it still balanced?:')
print()
r.left.left.left.insert_left()
r.left.left.left.left.x = 'Node 16'
r.left.left.left.left.v = '16'

if (tree.is_balanced() == True):
    print('Is Balanced')
else:
    print('Is Not Balanced')

