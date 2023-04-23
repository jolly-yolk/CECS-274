fruit={} #creates a dictionary

def removeDuplication(originalFile, destinationFile): #creates a definition to remove duplications in the original file
    while True: #creates a loop that persists until the end of the original file
        count = 0 #creates a counter object
        line = file.readline() #reads a single line on the original file
        fruit.update({line: count}) #updates the dictionary with the vale of the line that is currently being read and the currnet count
        count += 1 #updates the counter
        if not line: #if we meet the end of the original file
            break #break the loop
    new_list = list(fruit.keys()) #creates a list with the values of the dictionary
    for i in range(len(new_list)): #creates a loop with the range of the length of the dictionary list
        ini.writelines(new_list[i]) #writes the list of the dictionary values onto the destination file
    
ini = open('noduplication.txt', 'w', encoding='utf-8-sig') #opens the destination file
file = open('log.txt', 'r', encoding='utf-8-sig') #opens the original file

removeDuplication(file, ini) #calls the definition to remove duplication

file.close() #closes the original file
ini.close() #closes the destination file


