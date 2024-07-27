from bank_account import *

Sam = BankAccount(1000, "Sam")
Praise = BankAccount(2000, "Praise")

Sam.getBalance()
Praise.getBalance()

Sam.deposit(500)
Praise.deposit(300)

Sam.withdraw(10000)
Sam.withdraw(25)

Sam.transfer(15000, Praise)
Sam.transfer(200, Praise)

Princess = InterestReward(2000, "Princess")
Princess.getBalance()
Princess.deposit(100)
Princess.transfer(50, Praise)

Val = SavingsAcct(1000, "Val")
Val.getBalance()
Val.deposit(100)
Val.transfer(10, Praise)
