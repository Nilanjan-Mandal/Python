# A Python program generally has two scope, Local & Global

# Global Variable
number = input("Please give a number: ")
# print(number)

def variable():
    global number
    number = 10
    print(number)

variable()
print(number)
