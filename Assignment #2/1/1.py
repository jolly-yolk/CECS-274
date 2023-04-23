import ArrayStack
       
def add_all(i, c):
    stack = ArrayStack.ArrayStack()
    for k in range(0, i):
        stack.push(a[k])   
    for k in range(len(c)):
        stack.push(c[k])
    for k in range(i, len(c)):
        stack.push(a[k])
    return stack
            
a = ArrayStack.ArrayStack()
a.push('a')
a.push('b')
a.push('c')
a.push('d')
print(f'Before: {a}')
c = ['1', '2', '3', '4']
'''
print()
print('Inserting Stack')
print(c)
print()
print('Inserting at index 0')
print(add_all(0, c))
print()
print('Inserting at index 1')
print(add_all(1, c))
print()
print('Inserting at index 2')
print(add_all(2, c))
print()
print('Inserting at index 3')
print(add_all(3, c))
print()
print('Inserting at index 4')
print(add_all(4, c))


calling add(i, x) repeatedly is wrong because the Big O Notation comes out to
being O(m+n) m and n being the number of times it would take to push each element in
both of the lists together.
'''
a.add(2, 'e')
print(f'After: {a}')

