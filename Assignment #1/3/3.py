import heapq as hq #imports HeapQueue

fruit = {} #creates a dictionary

class Line: #creates a class for Line
    def __init__(self, value, length):
        self.value = value #value of Line
        self.length = length #length of Line

    def __lt__(self, other):
        return self.length < other.length #compares the length of one line and another
    
def sortbyLengthLines(originalFile, reversedFile): #creates a definition for sorting the length of the lines
   new_list = [] #creates a list
   t_list = [] #creates a temp list
   heap = [] #creates a heap
   hq.heapify(heap) #heapifys the heap
   for i in range(len(originalFile)): #creates a loop in range of the length of the original file
       u = Line(originalFile[i], len(originalFile[i])) #creates a Line with attached value and length
       t_list.append(u) #appends a Line to temp list
   for i in range(len(originalFile)): #creates a loop in range of the length of the original file
      hq.heappush(heap, t_list[i]) #pushes each element of the temp list into the heap
   for i in range(len(originalFile)): #creates a loop in range of the length of the original file
       j = str(hq.heappop(heap).value) #pops the smallest element out of the heap and turns it into a string
       ini.write(j) #writes the smallest element out of the heap onto the destination file

def removeDuplication(originalFile, destinationFile): #creates a definition for comparing file
    while True: #creates a while loop that exists until the end of the original file
        count = 0 #creates an object that holds the counter
        line = file.readline() #reads a single line from the original file
        fruit.update({line: count}) #updates the dictionary with the line of the original file and the count
        count += 1 #updates the count
        if not line: #if there is no line on the original file
            break #break loop
    new_list = list(fruit.keys()) #creates a new list with all the values of the dictionary
    return new_list #returns list of all the values of the dictionary
    
ini = open('sortbylength.txt', 'w', encoding='utf-8-sig') #opens the destination file
file = open('log.txt', 'r', encoding='utf-8-sig') #opens the original file

nodups = removeDuplication(file, ini) #calls the remove duplication definition

sortbyLengthLines(nodups, ini) #calls the sort by length of lines definition

file.close() #closes the original file
ini.close() #closes the destination file
