#
#
#
#
#

class savings:
    balance = 0;
    def __init__(self, amount):
        print("Savings acoount created")
        self.balance = float(amount)

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        print("You have deposited", amount)
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance <= amount:
            print("Not enough balance")
        else:
            print("You have withdrawn", amount)
            self.balance -= amount


#
#main
#

myAcc = savings(500)
print("My initial balance is", myAcc.getBalance())
myAcc.deposit(200)
print("My new balance is", myAcc.getBalance())
myAcc.withdrawal(600)
print("My balance after withdrawal is", myAcc.getBalance())
