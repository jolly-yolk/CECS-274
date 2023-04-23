import SLLDeQueue

SLL1 = SLLDeQueue.SLLQueue()

SLL1.add('a')
SLL1.add('b')
SLL1.add('c')
SLL1.add('d')
SLL1.add('e')
SLL1.add('f')

print('Most than 1 Node')
print(SLL1)
print(f'Second to Last Variable: {SLL1.second_last()}')

SLL2 = SLLDeQueue.SLLQueue()
SLL2.add('a')

print()
print('At Most 1 Node')
print(SLL2)
print(f'Second to Last Variable: {SLL2.second_last()}')

SLL3 = SLLDeQueue.SLLQueue()

print()
print('No Nodes')
print(SLL3)
print(f'Second to Last Variable: {SLL3.second_last()}')

'''
The run time for the code will be O(n - 1) because there is a loop that will run
#until the last element of the list which would be n - 1.'''
