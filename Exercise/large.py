print ("Let's Find the largest number among two number - ")

a = float(input("Please type the first number : "))
b = float(input ("Please type the second number : "))

largest = 0

if a > b:
    largest = a

else:
    largest = b


print ("The largest Number is among two numbers is  ", largest)


print ("PLease find the largest numbers among three numbers - ")
# Find the Largest number among three numbers
c = float(input("Please type the first number : "))
d = float(input ("Please type the second number : "))
e = float(input ("Please type the third number : "))

largest_3 = 0

if (c >= d) and (c >= e):
    largest_3 = c
elif (d >= e) and (d >= c):
    largest_3 = d
else:
    largest = e


print ("The largest Number is among three numbers is  ", largest)


print ("Let's Find the largest number among 4 number")

f = float(input("Please type the first number : "))
g = float(input ("Please type the second number : "))
h = float(input ("Please type the third number : "))
i = float(input ("Please type the third number : "))          

large_4 = max(f,g,h,i)    
print ("The largest Number is among four numbers is  ", large_4)

print ("Let's Find the largest number among N number")

j = int(input("Please type the max number"))
