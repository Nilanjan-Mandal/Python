# Basic Tuple
tup = ("python", "is good")
print(tup)

# Create Tuple with the use of List
Tuple_z = ([1, 2, 3], ["a", "b", "c"])
print(Tuple_z)

# Repitation
print("Tuple with repetition: ")
Tuple4 = ("Nilanjan",) * 3
print(Tuple4)

print("\nTuple with nested tuples: ")
Tuple5 = (1, 2, 3, 4, 5)
Tuple6 = ("a", "b", "c", "d", "e")
Tuple7 = (Tuple5, Tuple6)
print(Tuple7)


Tuple1 = (
    1,
    45,
    87,
    90,
    34,
    23,
    5,
)
Tuple2 = ("a", "r", "y", "j", "p")

w = len(Tuple1)
x = sorted(Tuple2)
y = max(Tuple1)
z = min(Tuple1)
v = sum(Tuple1)
avg = v / w

# Concatination
Tuple_con = Tuple2 + Tuple1
print(Tuple_con)


print(w)
print(x)
print(y)
print(z)
print(v)
print(avg)


# Slicing
Tuple_slice = "Nilanjan is a very genious guy!"
print("This will print the value form 4th to 9th Index!")
print(Tuple_slice[4:10])

print(Tuple1[0:-1])
