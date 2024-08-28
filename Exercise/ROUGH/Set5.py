#Upper, Lower, Concatinate
a = input("Please enter your text here: ")
str1 = input("Enter the string \n")
str2 = input("Enter the string \n")
concat = str1 + str2

print(a.upper())
print ("\n lower \n")
print(a.lower())
print("\n Concate \n")
print(concat)


# Find the occurance of a chracter in a string 
text = input("Please write the text \n")
char = input("Write the character for which you want to find the occurance : ")
print("Length is: {}".format(len(text)))

count = 0 
for i in range(len(text)):
    if text[i] == char:
        count = count + 1

print("\n Occurance is: {}".format(count))


# Total Number of words, vowel, consenent
text = input("Please write the text \n")

print("Length is: {}".format(len(text)))

count = 0 
for i in range(len(text)):
    if text[i] == " " or text[i] == " \n ":
        count = count + 1

print("\n Word is: {}".format(count))


# Python program to Replace Blank Space with Hyphen in a String

str2 = text.replace(' ', '_')
print("Original String :  ", text)
print("Modified String :  ", str2)
print("\n Reverse String \n")
print(text[::-1])