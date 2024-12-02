# Encapsulation = Wrapping data and function into a single unit(object).

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance    
                    

acc1 = Account(10000,15268)
acc1.debit(2000)
acc1.credit(500)
acc1.credit(600)
acc1.debit(900)