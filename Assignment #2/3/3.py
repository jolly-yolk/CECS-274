import RotatingArrayList

arraylist = RotatingArrayList.ArrayList()

for i in range(0, 10):
    arraylist.append(i)
print('Initial list:')
print(arraylist)
print()
print('Rotating 2:')
arraylist.rotate(2)
print(arraylist)
print()
print('Rotating 3:')
arraylist.rotate(3)
print(arraylist)

#the Big O Notation is O(n + m) because we use 2 for loops to rotate the list.

