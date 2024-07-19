# Detarmine the Grade of a Student
def grade_determination(score):
        if score >= 90:
                return 'A'
        elif score >= 80 and score < 90:
                return 'B'
        elif score >= 70 and score < 80:
                return 'C'   
        else:
                return 'Not Upto the Mark' 
        

number = int(input("Please share your marks: "))

print("The grade of your son is {0}".format(grade_determination(number)))

# Find the factorial Number

def get_Factorial(N):
        if N == 1 or N == 0:
                return 1
        elif N < 0:
                return 0
        else:
                fact = 1
                while N > 0:
                        fact = fact * N
                        N = N - 1
                return fact


Factorial = int(input("Please enter the Number your want to get the factorial: "))

print("Facctorial of the {0} is {1}".format(Factorial,get_Factorial(Factorial)))

