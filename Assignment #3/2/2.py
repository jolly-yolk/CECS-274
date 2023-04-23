import SLList

SLList = SLList.SLLQueue()
SLList.add('a')
SLList.add('b')
SLList.add('c')
SLList.add('d')

print('Original List: ')
print(SLList)


#Get
i = 2
x = SLList.get(i)
print()

print(f'Get at index ({i}): {x.x}')


#Set
i = 3
SLList.set(i, 'g')
print()

print('New List that has been set: ')
print(SLList)

#Add Index
i = 2
SLList.add_index(i, 'g')
print()

print('New List that has been indexed: ')
print(SLList)


#Remove Index
SLList.remove_index(4)
SLList.remove_index(0)
SLList.remove_index(0)
print()

print('New list with a removed elements: ')
print(SLList)
