import BinarySearchTree
q = BinarySearchTree.BinarySearchTree()
q.add(7, '7')
q.add(5, '5')
q.add(20, '20')
q.add(4, '4')
q.add(6, '6')
q.add(19, '19')
q.add(25, '25')
q.add(35, '35')
q.add(15, '15')
q.add(2, '2')
print(q.r.left.x)
q.remove(q.remove(q.r.left))
print(q.r.left.x)
