class Employee():
    name = "ABC.org" # Class Attribute

    def __init__(self, name) -> None:
        self.name = name # Object Attribute > Class Attribute
    
e1 = Employee("Neel")
print(e1.name)