#1 Import
import re
text = 'ABC 123 XYZ 456 @&! 100'

#2 Create the pattern
pattern = re.compile(r'\d\d\d') #Raw string, and match the pattern for three digit

#3 Search the pattern in the particular text 
matches = pattern.search(text)
matches1 = pattern.finditer(text) #This will search for pattern in the etire string

#4 Print
print(matches)

for match in matches1:
    print(match.group())

