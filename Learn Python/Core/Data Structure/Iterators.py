'''
Iterable - Object, which can provide iterator
Iteration 
Iterator - In Python, an iterable is an object that can be iterated over, meaning that you can traverse through all its elements one by one
Generator
'''

def num_gen(n):
    for i in range(n):
        yield i

ob1 = num_gen(1000000)
print(ob1)
print(next(ob1))
print(next(ob1))
print(next(ob1))

# for i in num_gen(1000):
#      print(i)

