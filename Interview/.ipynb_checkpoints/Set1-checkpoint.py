print ("Hello World!")
num1 = input("Please enter the number: ")
num2 = input("Please enter the number: ")

# Perform arithmatic operations
print("The entered number is: {0}, {1} ".format(num1,num2))
addition = int(num2) + int(num1)
print("Addition of {0} & {1} number is: {2}".format(num1,num2,addition))

# Print a Calander
import calendar

# ask of month and year
year = int(input("Please Enter the year Number: "))
month = int(input("Please Enter the month Number: "))

print(calendar.month(year, month))

# Print 1 to N Natural Number
N = int(input("Please enter the number: "))

i = 1
while i <= N:
    print(i)
    i += 1

N1 = int(input("Please enter the number: "))

for i in range(1, N1 + 1):
    print(i)

