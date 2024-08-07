class Car: 
    color = 'Black'

    def __init__(self, type) -> None:
        self.type = type

    @staticmethod
    def start():
        print("Started")

    @staticmethod
    def stop():
        print("Stopped")

class Toyota(Car):
    def __init__(self, name, type) -> None:
        super().__init__(type)
        self.name = name

car1 = Toyota("Prius", "Electric")
print(car1.type)  # Output: Electric

