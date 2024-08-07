class Student:
    def __init__(self, id, passcode, ) -> None:
        self.id = id
        self.__passcode = passcode #Private Attributes

s1 = Student(12, 'abce')
print(s1.passcode)


