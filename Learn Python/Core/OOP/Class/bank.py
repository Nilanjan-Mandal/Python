class Account:
    def __init__(self, bal, account_no) -> None:
        self.bal = bal
        self.account_no = account_no
    
    #Debit Method
    def debit(self, ammount):
        self.bal = self.bal - ammount
        print("Rs. {} has debited from your account {}: ".format(ammount, self.account_no))
        print("Total Balace is,  {}".format(self.get_bal()))
    #Credit Method
    def credit(self, ammount):
        self.bal = self.bal + ammount
        print("Rs. {} has credited to your account {}: ".format(ammount, self.account_no))
        print("Total Balace is,  {}".format(self.get_bal()))
    #Print the balance
    def get_bal(self):
        return self.bal

acc1 = Account(10000, 3245678909)
print("The balance of {} is = {}".format(acc1.account_no, acc1.bal))
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
