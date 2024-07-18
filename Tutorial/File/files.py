# File I/O -> (Input/Output)
# We have to open a file before doing any kind of operations in the file. 

# mode by default is 'read'. r/w

# -> Let's Open the file
f = open("demo.txt", "r") 

# -> Let's Read the file
data = f.read(5)
# That will only read first 5 characters
print(data)
print(type(data))

# -> Let's Close the file
f.close()



