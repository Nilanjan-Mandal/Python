# Break -> This will exit from the current iteration
# Continue -> This will skip the current condition
# Pass -> 

numbers = list(range(1,101))
# print(numbers)

print("Let's Print the Odd Numbers")
for i in numbers:
    if i % 2 == 0:
        continue
    print(i)

print("Print numbers till 40")
for i in numbers:
    if i == 41:
        break
    print(i)
