'''List comprehension offers one-liner syntax to create a new list based on the values of the existing list. 
You can use a `for loop` to replicate the same thing, but it will require you to write multiple lines, and sometimes it can get complex'''

my_list = list(range(1,20))
print(my_list[::-1])
my_list.pop()
print("Entire List : ")
print(my_list)
print(len(my_list))