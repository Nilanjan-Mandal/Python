arr = [1,2,3,4,5,6,7,8,9,10]
list = ["Hey", "Subodh", "Bidisha", 12, 78]
tuple =(12,"Hey", "Subodh", "Bidisha", 10, 78)
dict = {"Samsung" : 100, "Apple": 200, "Lava": 205}

#Array Operations
print("Let's work with Array")
print(arr)

#List Operations
print("Let's work with List")
print(list)
#Append
list.append(65)
print("After the Append of 65 \n", list)
number = int(input("Enter the number to append : "))
list.append(number)
print("After the Append of the {0} \n {1}\n".format(number,list))
#Reverse Order : 
print(list[::-1])
#Insert an element in nth Position
number = input("Please enter the elementyou want to insert : \n")
list.insert(2,number)
print("After the insertion of {0} newly created list is {1}:".format(number,list))
#Slicing
print(list[0:2])
#Extend a list
list.extend([7,8])
#Removing elements
list.remove("Hey")
del list[2:5]
#length a list
print(len(list))
print(list)
list3 = list1 + list2
print(list3)


#Tuple Operations
print("Let's work with Tuple")
print(tuple)

#Dictionary Operations
print("Let's work with Dictionary")
print(dict)

