print(type(1))
print(1 + 2)
print([1,2,3] + [4,5,6])
print("apna" + "college")


class Complex:
    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img
    def show_number(self):
        print(self.real, "i+", self.img, "j")
    
    #Dunder Function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.show_number()

num2 = Complex(4,9)
num2.show_number()
# num3 = num1.add(num2)
# num3.show_number()
num3 = num1+num2
print(num3.show_number())
