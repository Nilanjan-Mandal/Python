import os
print("Print the Current Directory \n")
print(os.getcwd())
print("Change the Directory")
os.chdir('/Users/nilanjan/Documents/IT/Language/python/Learn Python/Core/File/')
print("Print the Current Directory -- ")
print(os.getcwd())

# Let's get into operations : 
with open('demo.txt', 'r') as readFile:
           #print(readFile.read())
           print(readFile.readlines())
        # for line in readFile: 
        #         print(line, end= '')

print("Let's write something : \n")
with open('TEST.txt', 'a') as writeFile:
        writeFile.write("\n APPEND!")




