class Employee():
    college = "AEC" # Class Attribute

    def __init__(self, name, marks) -> None:
        self.name = name # Object Attribute > Class Attribute
        self.marks = marks
    def hello(self):
        print("Welcome to {}".format(self.college))
    
    def getmarks(self):
        return self.marks
    
e1 = Employee("Neel", 90)
print(e1.name)
print(e1.college)
e1.hello()
print(e1.getmarks())