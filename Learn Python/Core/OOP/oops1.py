class bag_factory():
    brand = 'wildcraft'
bag1 = bag_factory()
print(bag1)
print(bag1.brand)

# Constructor or __init__ function
# Classes has a function is called constructor or __init__. This will invoke when # we create an object. we may edit the __init__ function
class student():
    # Default Constructor
    def __init__(self) -> None:
        pass
    # Parameterized Constructor    
    def __init__(self, name, marks) -> None:
        print("Adding new student in database.... ")
        self.name = name
        self.marks = marks

s1 = student("Nilanjan", 97)
print(s1.name)
s2 = student("Mahesh", 88)
print(s2.name)
print(s2.marks)


