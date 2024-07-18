# Homegeneous, UnSorted group of elements. Define -- 
numbers = [1,2,3,4,5,6,7,8]
number = [1,2,3,4]
cars = ["Ford", "Volvo", "BMW"]
list = ["100","2.8","Sameer","Bidisha","Bigdata","I am the owner"]
tuple = ("Sameer", "Arjun", 100)


print ("The first car is {0}".format(cars[0]))
print ("The first number is {0}".format(numbers[6]))
print(list)
print(tuple)


print ("3rd Item of an Array {0}".format(numbers[2]))
print ("0th Item of an Array {0}".format(numbers[0]))
print ("last Item of an Array {0}".format(numbers[-1]))


def sum_arr(number):
    sum = 0 
    for i in number:
        sum = sum + i
        return sum

print("Addition: {0}".format(sum_arr(number)))
