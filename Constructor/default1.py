class Account :
    def __init__(self):
        self.accNo = int(input("Enter your a/c no. : "))
        self.accName = (input("Enter your a/c name : "))
        self.balance = float(input("Enter your balance : "))

    def display(self):
        print("Account No. :", self.accNo)
        print("Account Name:", self.accName)
        print("Balance :", self.balance)

    def deposit(self,amount):
        self.balance += amount
        print("deposited Amount :  ",self.balance)

    def withdraw(self,amount):
        if amount >self.balance:
            print("Insufficient Balance..!!",self.balance)
        else:
            self.balance-=amount
            print("Amount Withdraw Successfully : ",self.balance)

    def checkbalamnce(self):
        print("Current Balance : ",self.balance)

a=Account()
a.display()
a.deposit(1000)
a.withdraw(500)
a.checkbalamnce()