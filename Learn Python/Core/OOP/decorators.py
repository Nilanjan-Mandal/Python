class Student: 
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks

    def getaverage(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
        print("Hi {},\nyour average score is {}".format(self.name, sum/3))

s1 = Student("Nilanjan", [99, 88, 96])
s1.getaverage()
