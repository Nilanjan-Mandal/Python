g = [2, 8, 90, 78, 45, 60, 10, 20, 5, 62]

print("Print the list in sequence : ")
print(g)

print("Print Reverse order : ")
s = g[::-1]
print(s)

lst = list("Hey! How are you")
print(lst)

x = [12, 14, 17, 9, 86, 47, 76, 36, 24, 36, 88, 20, 5, 10, 100]
letter = ["a", "g", "j", "p", "o", "n"]

# Length
print(len(x))
# Max Value
print(max(x))
# Minimum Value
print(min(x))
# Sum
print(sum(x))
# Average
print(sum(x) / len(x))
# Concatinate
concatinate = x + letter
print(concatinate)
# Appending
letter.append("m")
print(letter)
# Removal
letter.remove("m")
print(letter)
# Insert
letter.insert(1, "m")
print(letter)
