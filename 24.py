class Bank_Account:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def getdeposit(self,depo_amount):
        return self.balance = self.balance + self.amount

    def getwithdraw(self,with_amount):
        return self.balance = self.balance - self.amount

    def getbalance(self):
        return self.balance        

account1=(acc_no,name,acc_type,balance)
acc_no = int(input("Enter the account the account number:"))
name = input("Enter the name of the account holder:")
acc_type = input("Enter the account type:")
balance = int(input("Enter the balance of the account:"))
