import RandomQueue
import random

def RandomRemove(queue):
    i = random.randrange(queue.n)
    print(f'Remove Index: {i} -> {queue.a[i]}')
    queue.remove(i)
    

queue = RandomQueue.ArrayQueue()
queue.add('a')
queue.add('b')
queue.add('c')
queue.add('d')
print('Initial Queue')
print(queue)
print()
print('First Random Removal')
RandomRemove(queue)
print(queue)
print()
print('Second Random Removal')
RandomRemove(queue)
print(queue)
print()
print('Third Random Removal')
RandomRemove(queue)
print(queue)
print()
print('Fourth Random Removal')
RandomRemove(queue)
print(queue)


    
