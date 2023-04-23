import DLLCheckSize
import SLLCheckSize

sll = SLLCheckSize.SLLQueue()
dll = DLLCheckSize.DLList()

for i in range(10):
    sll.add(f'{i}')

for i in range(10):
    dll.add(i, f'{i}')
    
print(f'SLL: {sll}')
print()
print(f'DLL: {dll}')
print()
print(f'SLL: {sll.check_size()}') #since linked lists are dynamic the size of
                                  #the list and number of elements will always
                                  #be equal.
print()
print(f'DLL: {dll.check_size()}') #elements and nodes will never be equal
                                  #because there is always 1 more node then
                                  #there is an element therefore nodes > elements
                                  # by only 1 node.

#Big O Notation will be O(n) because it must iterate through the linked list
#in order to count the nodes and elements.
