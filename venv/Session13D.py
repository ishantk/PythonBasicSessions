# User-Defined Exception
class BankingException(Exception):
    pass

class Banking:

    def __init__(self):
        self.balance = 10000
        self.minBalance = 3000
        self.attempts = 0

    def withdraw(self, amt):
        self.balance = self.balance - amt

        if self.balance <= self.minBalance:
            self.attempts = self.attempts+1
            self.balance = self.balance + amt
            print("Withdraw Failure !! Balance is ", self.balance)
        else:
            print("Withdraw Success !! Balance is ",self.balance)

        if self.attempts == 3:
            raise BankingException
            #raise ArithmeticError

print("==Banking Started==")

bRef = Banking()

for i in range(1,101):
    bRef.withdraw(3000)

print("==Banking Finished==")