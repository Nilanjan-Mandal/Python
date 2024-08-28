# Special Type of Function that allows you to create an iterable sequence of values. 

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

# Create a generator object
gen = square_generator(5)
print(gen)
print(next(gen))
print(next(gen))

def num_generator(m):
    for i in range(m+1):
        yield i

gen1 = num_generator(23)
print(gen1)
print(next(gen1))
print(next(gen1))
print(next(gen1))

# gen = num_generator()
# for j in gen:
#     print(j)
