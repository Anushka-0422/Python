class Account:

    def __init__(self, name, no, bal):
        self.acc_name = name
        self.acc_no = no
        self.bal = bal

        print("Account Holder Name:", self.acc_name)
        print("Account No:", self.acc_no)
        print("Account Available Balance:", self.bal)

    def deposit(self, amt):
        self.bal += amt
        print("Amount Successfully Added! New Balance:", self.bal)

    def withdraw(self, amtw):
        if amtw > self.bal:
            print("Insufficient balance! Available:", self.bal)
        else:
            self.bal -= amtw
            print("Successfully Deducted! New Balance:", self.bal)

    def balance(self):
        print("Available Balance:", self.bal)


# Creating an object with initial balance of 2000
obj = Account("John", 12345, 2000)

# Performing operations
obj.deposit(1000)   # Balance - 3000
obj.withdraw(1500)  # Balance - 1500
obj.balance()
