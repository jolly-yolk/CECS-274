class Stack: #creates a class for stack
    def __init__(self):
        self.elements = [] #creates a stack of elements

    def push(self, data):
        self.elements.append(data) #appends the object data into the stack

    def pop(self):
        return self.elements.pop() #pops the last element in the stack


def reverse(originalFile, destinationFile): #creates a definition to reverse the original file
    stack = Stack() #creates a stack
    reverse = [] #creates a list
    for i in range(len(originalFile)): #creates a for loop in the range of the length of the original file
        stack.push(originalFile[i]) #push into the stack original file[i]
    for i in range(len(originalFile)): #creates a for loop in the range of the length of the original file
        reverse.append(stack.pop()) #appends to the reverse list the current element being popped from the stack
    for i in range(len(reverse)): #creates a for loop in the range of the length of the reverse list
        destinationFile.writelines(f'{reverse[i]}\n') #writes the elements of the reverse list onto the destination file

i = open('reversedinput-1.txt', 'w') #opens the destiantion file
i.close() #closes the destination file (this is to clear the destination file so that if the program rusn multiple times it doesnt duplicate)

file = open('input-1.txt') #opens the original file
Input1 = file.readlines() #creates a list with the elements being the contents of the original file

for i in range(len(Input1)): #creates a for loop with the range in length of the list of the elements of the original file
    Input1[i] = Input1[i].replace('\n', '') #clears the \n naturally occuring on the original file

destinationFile = open('reversedinput-1.txt', 'a') #opens the destination file
   
reverse(Input1, destinationFile) #calls the definition to reverse the original file

file.close()
destinationFile.close() #closes the destiantion file