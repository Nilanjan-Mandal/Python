# Special Type of Function that allows you to create an iterable sequence of values. 
# Gen Function -> Gen Object

# def square_generator(n):
#     result = []
#     for i in range(1, n + 1):
#         yield result.append(i * i)
#     print(result)
# # Create a generator object
# gen = square_generator(5)

# # Iterate over the generator
# for square in gen:
#     print(square)


def num_generator():
    for i in range(100):
        yield i

gen = num_generator()
for j in gen:
    print(j)
