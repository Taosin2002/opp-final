from abc import ABC,abstractmethod
import datetime
class User(ABC):
    acounts = []
    account_number = {}
    total_balance = 0
    total_loans = 0
    isLoan = False
    def __init__(self,name,email,address,password,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.account_type = account_type
        self.balance = 0
        self.loans = 2
        self.transaction = []
        self.acount_numbers = f"2023-{len(self.name)}-{len(self.email)}-{len(self.address)}"
        self.acounts.append(self)
        self.account_number[self.name]= self
        
    def deposite(self,amount):
        if amount >= 0 :
            self.balance+=amount
            User.total_balance+= amount
            history = f"{amount} has been deposited in your account at {datetime.datetime.now()}"
            self.transaction.append(history)
            print("Deposite successful")
        else:
            print("||   Invalid Amount  ||")

    def withdraw(self,amount):
        if amount >= 0 and amount<= self.balance :
            self.balance -= amount
            User.total_balance -=amount
            history = f"{amount} has been withdraw in your account at {datetime.datetime.now()}"
            self.transaction.append(history)
            print(f"Withdraw successful of amount {amount}")
        else:
            print("||  Withdrawal amount exceeded  ||")

    def Loan(self,amount):
        if self.loans != 0 and User.isLoan == False:
            if User.total_balance!= 0:
                if amount>=0 and amount <= User.total_balance :
                    self.balance+=amount
                    User.total_loans+=amount
                    print("\nLoan has successfully added to your account\n")
                    history = f"{amount} has been Loan in your account at {datetime.datetime.now()}"
                    self.loans-=1
                    self.transaction.append(history)
                else:
                    print("This amount can not added to your balance")
                    print("***** Please enter amount under 50000$ !*******\n")
            else:
                print("\n\n------|    BANKRUPT     |-----\n\n")
        else:
            print("******  You can't take Loans  ******")

    def changeInfo(self,type):
        if type == 'name':
            name = input("Enter your New Username : ")
            self.name = name
            print(f"\nName is succefully change to {self.name}\n")
        if type == 'name':
            password = input("Enter your New password : ")
            self.password = password
            print("\npassword has changed!!\n")
    
    def Transection(self):
        for trans in self.transaction:
            print(trans)

    @abstractmethod
    def showInfo(self):
        pass

    def chech_balance(self):
        print(f"\n Your balance is {self.balance} \n")

    def transfer_money(self,account,amount):
        if account in User.account_number:
            deposite_account = User.account_number[account]
            self.withdraw(amount)
            deposite_account.deposite(amount)
            history = f"{amount}$ has been transfer from {self.name} to {account}"
            print(f"\n----- {amount}$ has been transfer from {self.name} to {account}-----\n")
            self.transaction.append(history)
        else:
            print("Account does not exist")
class Savings_account(User):
    def __init__(self, name, email, address,password) -> None:
        super().__init__(name, email, address,password,"savings")
        self.interest_rate = 7

    def showInfo(self):
        print("\n--------INFO----------")
        print(f"Username : {self.name}")
        print(f"Usermail : {self.email}")
        print(f"User Address : {self.address}")
        print(f"User Acount Number : {self.acount_numbers}")
        print("Account type : Savings ")
        print("--------------------------")

    def apply_interest(self):
        interest = self.balance * (self.interest_rate/100)
        print(f"\n Applied Interest of {interest}\n")
        self.deposite(interest)

class Current_Acount(User):
    def __init__(self, name, email, address,password) -> None:
        super().__init__(name, email, address,password,"Current")
        
    
    def showInfo(self):
        print("\n--------INFO----------")
        print(f"Username : {self.name}")
        print(f"Usermail : {self.email}")
        print(f"User Address : {self.address}")
        print(f"User Acount Number : {self.acount_numbers}")
        print("Account type : Current ")
        print("--------------------------")

