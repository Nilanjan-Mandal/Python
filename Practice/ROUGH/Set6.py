# Read the File
f = open("/Users/nilanjan/Documents/IT/Language/python/Interview/Set1.py", "r")      
print(f.read())
print(f.read(5))
print(f.readline())
f.close()

# Write the File
# a -> Apend
# w -> Overwrite
f1 = open("/Users/nilanjan/Documents/IT/Language/python/Interview/hash.py", "a")      
f1.write("Adding More Contents!")
f1.close()

f1 = open("/Users/nilanjan/Documents/IT/Language/python/Interview/hash.py", "r")      
print(f1.read())
f1.close()
