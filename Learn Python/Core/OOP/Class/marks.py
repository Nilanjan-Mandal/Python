# This is important for dynamically changing the attributes. 
class Student:
    def __init__(self, phy,chem, math) -> None:
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def calc_percentage(self):
        return (self.phy + self.chem + self.math)/3
s1 = Student(98,78,65)
print(s1.math)
s1.math = 10
print(s1.calc_percentage)