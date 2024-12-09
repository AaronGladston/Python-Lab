class Bank_Account:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def getDeposit(self):
        depo_amount = int(input("Enter the amount to be deposited into the account:"))
        self.balance = self.balance + depo_amount
        return print("The updated balance of the account is:",self.balance)

    def getWithdraw(self):
        with_amount = int(input("Enter the amount to be withdrawn from the account:"))
        self.balance = self.balance - with_amount
        return print("The updated balance of the account is:",self.balance)

    def getBalance(self):
        return print("The current balance of the account is:",self.balance)

acc_no = int(input("Enter your account number:"))
name = input("Enter the name of the account holder:")
acc_type = input("Enter the type of the account:")
balance = int(input("Enter the balance of the account:"))
account1 = Bank_Account(acc_no,name,acc_type,balance)
account1.getDeposit()
account1.getWithdraw()
account1.getBalance()


