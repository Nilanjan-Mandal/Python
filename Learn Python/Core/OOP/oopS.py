# Class : This is the blue print of the object we are going to create!
# Object : This is the real time object

class Student:
    name = "Karan"

s1 = Student()
print(s1)
print(s1.name)
s2 = Student()
print(s2.name)

# Make a Car Factory -- 
class garage: 
        color = 'Blue'
        brand = 'BMW'
car1 = garage()
print(car1.color)


# Constructor 
# All classes have the function __init__()  which will invoke when the class is initiated. 

# Class -- 
class bag_factory: 
      def __init__(self) -> None:
            print("Creating new bags")
      brand = 'wildcraft'
            
# Object -- 
bag1 = bag_factory()
print(bag1)