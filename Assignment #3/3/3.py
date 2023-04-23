import SLLReverse

SLL = SLLReverse.SLLQueue()
empty = SLLReverse.SLLQueue()

for i in range(10):
    SLL.add(f'{i}')

print(f'Full list: {SLL}')
print(f'Empty List: {empty}')
empty.reverse()
SLL.reverse()
print(f'Full list Reversed: {SLL}')
print(f'Empty List Reversed: {empty}')

#the big O notation should be O(n) because it has to go through the whole list
