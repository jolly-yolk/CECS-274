import HanoiStack #imports stack skeleton

disks = int(input('Please input the number of disks you would like(3 to 8): ')) #asks user to insert number of disks

#validates whether there are too many or too few disks. If true then it asks to reenter disk number.
while (disks < 3) or (8 < disks):
    if (disks < 3):
        print()
        print('Not enough disks man...')
        print()
    else:
        print()
        print('That\'s too many disks!')
        print()
    disks = int(input('Please input the number of disks you would like(3 to 8): '))

#provides minimum number of moves you can use for each number of disks
if disks == 3:
    mini = 7
if disks == 4:
    mini = 15 
if disks == 5:
    mini = 31
if disks == 6:
    mini = 63
if disks == 7:
    mini = 127
if disks == 8:
    mini = 255
    
valid = False #creates a bool variable named valid

#prints rods and asks user to select a starting rod
print('''
     l) Left Rod
     m) Middle Rod
     r) Right Rod
    ''')
start = input('Please select which rod you would like to start (l, m, or r): ')

print()

#asks user to select a ending rod
end = input('Please select which rod you would like to end (l, m, or r): ')

#validates the starting and ending rod selection
if (start == 'l' or start == 'm' or start == 'r') and (end == 'l' or end == 'm' or end == 'r') and (start != end):
    valid = True

# if selection is invalid the user is asked to reenter values until it is valid   
while valid != True:
    print()
    print('Invalid Selection')
    print()
    valid = False
    start = input('Please select which rod you would like to start (l, m, or r): ')
    print()
    end = input('Please select which rod you would like to end (l, m, or r): ')
    if (start == 'l' or start == 'm' or start == 'r') and (end == 'l' or end == 'm' or end == 'r') and (start != end):
        valid = True

#creates 4 stacks (3 for the rods and 1 for the validating stack)       
left = HanoiStack.ArrayStack()
middle = HanoiStack.ArrayStack()
right = HanoiStack.ArrayStack()
winner = HanoiStack.ArrayStack()

win = False #creates a bool variable that indicates whether or not the player has won

#fills two of the four stacks (the starting rod and validating stack)
if start == 'l':
    for i in range(disks, 0, -1):
        left.push(i)
if start == 'm':
    for i in range(disks, 0, -1):
        middle.push(i)
if start == 'r':
    for i in range(disks, 0, -1):
        right.push(i)
        
for i in range(disks, 0, -1):
    winner.push(i)

moves = 0 #variable that records number of moves used

#creates a loop that functions as the "meat and potatoes" of the game
while win != True:
    #validates whether or not the player has won and if they shoudl break the loop
    if end == 'l':
        if left.n == winner.n:
            break
    elif end == 'm':
        if middle.n == winner.n:
            break
    elif end == 'r':
        if right.n == winner.n:
            break

    invalid = False #creates a bool variable that validates if the move is invalid

    #prints the rods, the number of moves you've done, and the minimum number of moves you can do
    print()
    print(f'Left: {left}')
    print(f'Middle: {middle}')
    print(f'Right: {right}')
    print(f'Moves: {moves}')
    print(f'Minimum Moves: {mini}')
    print()

    move = input('Please select what rod you would like to move(l, m, or r): ') #asks user to input the rod they wish to move

    valid = False #sets the valid bool to False if it wasn't already

    #Validates whether the move is valid
    if (move == 'l' or move == 'm' or move == 'r'):
        valid = True
    if move == 'l' and left.n == 0:
        valid = False
    elif move == 'm' and middle.n == 0:
        valid = False
    elif move == 'r' and right.n == 0:
        valid = False

    #if the move is invalid then the user is asked to resumbmit the move variable until it is valid
    while valid != True:
        print()
        print('Invalid Selection')
        print()

        valid = False

        move = input('Please select what rod you would like to move(l, m, or r): ')

        print()

        if (move == 'l' or move == 'm' or move == 'r'):
            valid = True
        if move == 'l' and left.n == 0:
            valid = False
        elif move == 'm' and middle.n == 0:
            valid = False
        elif move == 'r' and right.n == 0:
            valid = False
               
    add = input('Please select what rod you would like to add to (l, m, or r): ') #asks user to input the rod they wish to add to

    valid = False #sets valid to False if it wasn't already
    
    #validates whether the rod they wish to move to is avaliable
    if (add == 'l' or add == 'm' or add == 'r') and (add != move):
        valid = True
    if (add == 'l' and left.n == disks):
        valid = False
    elif (add == 'm' and middle.n == disks):
        valid = False
    elif (add == 'r' and right.n == disks):
        valid = False

    #if they cannot move to the rod they have selected then they are asked to resubmit until they select a valid rod
    while valid != True:
        print()
        print('Invalid Selection')
        print()

        valid = False

        add = input('Please select what rod you would like to add to (l, m, or r): ')
        print()

        if (add == 'l' or add == 'm' or add == 'r') and (add != move):
            valid = True
        
    #the following if statements cover the various possibilities for player selections in terms of moving and adding       
    if move == 'l' and add == 'r':
        #if the adding stack is empty then just push whatever is popped from the moving rod and the loop continues
        if right.n == 0:
            right.push(left.pop())

        # if the adding stack is not empty then validate whether or not the moving rod has a larger number on top
        else:

             x = right.get(right.n - 1)
             y = left.get(left.n - 1)

             #if the top of the moving rod is bigger than the top of the adding rod then push the moving variable to the adding rod and the loop continues
             if x > y:
                right.push(left.pop())

             #if the top of the noving rod is smaller than the top of the adding rod then the move is invalid and the loop continues
             else:
                print()
                print('Invalid Selection')
                invalid = True
                print()
            
    if move == 'l' and add == 'm':
        if middle.n == 0:
            middle.push(left.pop())

        else:

            x = middle.get(middle.n - 1)
            y = left.get(left.n - 1)

            if x > y:
                middle.push(left.pop())

            else:
                print()
                print('Invalid Selection')
                invalid = True
                print()
                
            
    if move == 'm' and add == 'l':
        if left.n == 0:
            left.push(middle.pop())

        else:
            x = left.get(left.n - 1)
            y = middle.get(middle.n - 1)

            if x > y:
                left.push(middle.pop())

            else:
                print()
                print('Invalid Selection')
                invalid = True
                print()
    
    if move == 'm' and add == 'r':
        if right.n == 0:
            right.push(middle.pop())

        else:
            x = right.get(right.n - 1)
            y = middle.get(middle.n - 1)
            
            if x > y:
                right.push(middle.pop())

            else:
                print()
                print('Invalid Selection')
                invalid = True
                print()
            
    if move == 'r' and add == 'l':
        if left.n == 0:
            left.push(right.pop())

        else:
            x = left.get(left.n - 1)
            y = right.get(right.n - 1)

            if x > y:
                left.push(right.pop())

            else:
                print()
                print('Invalid Selection')
                invalid = True
                print()
            
    if move == 'r' and add == 'm':
        if middle.n == 0:
            middle.push(right.pop())

        else:
            x = middle.get(middle.n - 1)
            y = right.get(right.n - 1)

            if x > y:
                middle.push(right.pop())
            else:
                print()
                print('Invalid Selection')
                invalid = True
                print()
    
    #if the current move is invalid it does not count to the number of moves used
    if invalid == False:
        moves += 1
#once the player has won the resulting rods, number of moves, minimum number of moves possible, and a congratulation message is shown :)
print()
print(f'Left: {left}')
print(f'Middle: {middle}')
print(f'Right: {right}')
print(f'Moves: {moves}')
print(f'Minimum Moves: {mini}')
print()
print('Congratulations you have won!')
print()
#program ends
            
    
    
        
        
    





