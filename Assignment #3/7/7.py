import DLLMinStack

minstack = DLLMinStack.DLList()

minstack.add(0, 'a')
minstack.add(1, 'b')
minstack.add(2, 'c')
print(f'Minestack: {minstack}')
print()

minstack.push('d')

print(f'Push Element in Minstack: {minstack}')
print()

minstack.pop()

print(f'Pop Element in Minstack: {minstack}')
print()

print(f'Size of Minstack: {minstack.size() + 1}') #add 1 to include dummy
print()

print(f'Minimum Value in the Minstack: {minstack.min()}')


