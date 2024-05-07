class Student:
    # default constructor
    def __init__(self):
        pass
    # parametarized  constructor
    name = "Neel"
    Job = "Engineer"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new person to database ...")    


s1 = Student("Karan", 90)
print(s1.name, s1.marks)