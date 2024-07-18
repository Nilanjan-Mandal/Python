num1 = int(input("Kindly enter the number: "))

def fatorial(f):
    if f == 0 or f == 1:
        return 1
    elif f < 0:
        return 0
    else:
        fact = 1
        while (f > 1):
            fact = fact * f
            f = f -1
        return fact
    
Factorial = fatorial(num1)
print("Factorial of {0} is {1}".format(num1,Factorial))


        