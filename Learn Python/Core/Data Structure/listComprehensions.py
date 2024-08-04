#List Comprehension --> Construct a list from another list. 
fruit = ['apple', 'Banana', 'strawberries']
for f in fruit:
    print(f)
print()
#List Comprehensions -- 
[print(f) for f in fruit]

car = ['BMW', 'BUGATY', 'FORCE', 'TATA', 'SKODA']
# car_lower = []
# for c in car:
#     c = c.lower()  # Call the lower() method
#     car_lower.append(c)

# car = car_lower
# print(car)
#List Comprehensions -- 
car = [c.lower() for c in car]
print(car)


bits = [True, False, False, True, False, True, True, True]
new_bits = []

# for b in bits:
#     if b == True:
#         new_bits.append(1)
#     else:
#         new_bits.append(0)
# bits = new_bits
# print(bits)

# List Comprehension 
super_bits = [1 if b == True else 0 for b in bits]
print()
print(super_bits)