# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

---------------

# This program adds two numbers

num1 = input("Please type the first number")
num2 = input("Please type the second number")

print ("The Type of number is: ", type(num2))

# As Python treats them as a string, we must convert those to nos. 
num1 = float(num1)
num2 = float(num2)

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Function
def sub(a,b): 
    return a-b

sub_of_two_nos = sub(num2,num1)
print("The subtraction of {0} and {1} is {2}".format(num2,num1,sub_of_two_nos))

