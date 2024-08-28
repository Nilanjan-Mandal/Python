# Class & Objects

class Bankaccount():
    defaultAccNumber = 1
    
    def __init__(self, name, balance = 0) -> None: # Constructor-> Every object
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber