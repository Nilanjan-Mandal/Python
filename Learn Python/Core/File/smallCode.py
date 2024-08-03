import os
os.chdir('/Users/nilanjan/Documents/IT/Language/python/Learn Python/Core/File')
print(os.getcwd())

with open('demo.txt', 'r') as readFile: 
    for line in readFile: 
        if line.startswith('Answer') is True:
            with open('Answer.txt', 'a') as writeFile: 
                writeFile.write(line)



                