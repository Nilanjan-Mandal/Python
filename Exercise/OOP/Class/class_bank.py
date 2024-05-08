class Account:
    # Create the parameterized constructor
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    #debit method
    def debit(self, ammount):
        self.balance = self.balance - ammount
        print ("Rs.", ammount, "was debited from your account", self.account)
        print ("Total balance is : ", self.get_bal())
         
    #credit method
    def credit(self, ammount):
        self.balance = self.balance + ammount
        print ("Rs.", ammount, "was credited to your account", self.account)
        print ("Total balance is : ", self.get_bal())

    #total balance
    def get_bal(self):
        return self.balance

# Objects
acc1 = Account("A234", 10000)
acc2 = Account("B254", 14000)
acc3 = Account("C214", 19000)

#Debit Ops
acc1.debit(1000)

#Credit Ops
acc1.credit(200)


# Print the details
print("The account number is: ", acc1.account)
print("The balance is ", acc1.balance)