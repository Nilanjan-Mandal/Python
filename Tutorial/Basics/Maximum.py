num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

Maximum_No = find_max(num1, num2)

print("Please find the maximum number from your input: {0}".format(Maximum_No))