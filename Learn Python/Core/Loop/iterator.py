'''Iterable - Object, which can provide iterator
Iteration 
Iterator - In Python, an iterable is an object that can be iterated over, meaning that you can traverse through all its elements one by one
Generator'''

nums = [7,8,9,5]
it = iter(nums)
print(it)
# print(it.__next__())
# print(it.__next__())
print(next(it))
print(next(it))



list1 = list(range(1,10))

