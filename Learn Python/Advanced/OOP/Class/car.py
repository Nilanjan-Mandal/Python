class Car:
    def __init__(self) -> None:
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started!")

car1 = Car()
car1.start()