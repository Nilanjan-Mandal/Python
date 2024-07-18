# Create a File, If the file does not exist
# f1 = open("File1.txt", "x")

# Create a File if the file exist
f1 = open("File1.txt", "r+")
f1.write("Python Lecture!")
print(f1.read())

# Read The content
# data = f1.read()
# print(data)

# This will move the position of the file pointer!
f1.seek(0)
# This will tell the cursor position
print(f1.tell())

f1.close()
