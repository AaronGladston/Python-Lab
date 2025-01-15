class AtmSystem:
    def __init__(self,name,acc_no,acc_type):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = 0
    
    def accountDetails(self):
        return f"Name of account holder: {self.name}\nAccount Number: {self.acc_no}\nType of Account: {self.acc_type}\nBalance : Rs.{self.balance}\n"
    
    def check_balance(self):
        return f"The remaining balance in the account is Rs.{self.balance}\n"
    
    def deposit(self):
        deposit = int(input("Enter the amount to be deposited: "))
        self.balance += deposit
        print(f"Rs.{deposit} has been successfully deposited.\n")
    
    def withdraw(self):
        withdraw = int(input("Enter the amount to be withdrawn: "))
        if(withdraw<=self.balance):
            self.balance -= withdraw
            print(f"Rs.{withdraw} has been successfully withdrawn.\n")
        else:
            print(f"Insufficient balance for withdrawal.\n")
        
    def receipt(self):
        print("Transaction details:\n")
        print(self.accountDetails())
        print(self.check_balance())
        print("Thank you for using the ATM Services.\n")
    
if __name__== '__main__':
    start = 0
    account1 = None
    while start == 0:
        print("ATM System:\n1.Account creation\n2.Check Account Details\n3.Check Balance\n4.Deposit Amount\n5.Withdraw Amount\n6.Exit with transaction receipt")
        choice = int(input("Enter your choice:"))
        if choice==1:
            name = input("Enter the name of the account holder: ")
            acc_no = int(input("Enter the account number: "))
            acc_type = input("Enter the account type: ")
            account1 = AtmSystem(name,acc_no,acc_type) 
        elif choice==2:
            if account1:
                print(account1.accountDetails())
            else:
                print("No account found.Please create an account first.\n")
        elif choice==3:
            if account1:
                print(account1.check_balance())
            else:
                print("No account found.Please create an account first.\n")
        elif choice==4:
            if account1:
                account1.deposit()
            else:
                print("No account found.Please create an account first.\n")
        elif choice==5:
            if account1:    
                account1.withdraw()
            else:
                print("No account found.Please create an account first.\n")
        elif choice==6:
            if account1:
                account1.receipt()
                start = 1
            else:
                print("No account found.Please create an account first.\n")
        else:
            print("Enter a valid choice.\n")
        if start==0:
            start = int(input("Do you want to continue(0 for Yes or 1 for No)?"))       