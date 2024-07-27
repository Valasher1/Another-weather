# OOP = Object Oriented Programming

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self, amountRecieved):
        self.balance = self.balance + amountRecieved
        print(f"\n 'DEPOSIT COMPLETE'. ${amountRecieved}")
        self.getBalance()

    def viableTransaction(self, amountWithdrawn):
        if self.balance >= amountWithdrawn:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amountWithdrawn):
        try:
            self.viableTransaction(amountWithdrawn)
            self.balance = self.balance - amountWithdrawn
            print("\n 'WITHDRAW COMPLETE'.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")


    def transfer(self, amountTransfered, account):
        try:
            print("\n**********\n\nBegining Transfer...🚀")
            self.viableTransaction(amountTransfered)
            self.withdraw(amountTransfered)
            account.deposit(amountTransfered)
            print("\n 'TRANSFER COMPLETE!' ✅✅✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted!. ❌❌❌ {error}")

class InterestReward(BankAccount):
    def deposit(self,amountRecieved):
        self.balance = self.balance + (amountRecieved * 1.05)
        print(f"\n 'DEPOSIT COMPLETE'. ${amountRecieved}")
        self.getBalance()

class SavingsAcct(InterestReward):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amountWithdrawn):
        try:
            self.viableTransaction(amountWithdrawn + self.fee)
            self.balance = self.balance - (amountWithdrawn + self.fee)
            print("\n 'WITHDRAW COMPLETE'.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
 
         

