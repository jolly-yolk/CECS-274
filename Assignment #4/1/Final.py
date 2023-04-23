import BinaryTree

tree = BinaryTree.BinaryTree()
tree.r = tree.Node('Node 1')
r = tree.r
r.v = '2'

r.insert_right()
r.right.x = 'Node 3'
r.right.v = '4'

r.insert_left()
r.left.x = 'Node 2'
r.left.v = '1'

r.right.insert_right()
r.right.right.x = 'Node 7'
r.right.right.v = '5'

r.right.insert_left()
r.right.left.x = 'Node 6'
r.right.left.v = '3'

'''
print('In Order')
tree.in_order()
print()
print('Post')
tree.pos_order()
'''

print(tree.funcX(r.right.right.right).v)
