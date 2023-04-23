import DLLMerge

dll1 = DLLMerge.DLList()
dll2 = DLLMerge.DLList()

dll1.add(0, 'a')
dll1.add(1, 'b')
dll1.add(2, 'c')
print(f'DLL1: {dll1}')
print()

dll2.add(0, 'd')
dll2.add(1, 'e')
dll2.add(2, 'f')
print(f'DLL2: {dll2}')
print()

dll1.absorb(dll2)

print(f'DLL1(Absorbed): {dll1}')
print()

print(f'DLL2(Absorbed): {dll2}')
print()

#the big o notation would be O(n) where n is the number of elements in DLList 2
#which you have to move and delete while DLList 1 elements doesn't do anything
