class BankAccount():
    def __init__(self, balance, interest_rate = 2/100):
        self.interest_rate = interest_rate
        self.balance = balance

# method to deposit money
    def deposite (self, amount):
        self.balance += amount
        return self

# mehod to withdraw money
    def withdraw(self, amount):
        if self.balance < amount:
            print(self.balance)
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5+ amount   # balance will be in negative
            return self
        elif self.balance >= amount:
            self.balance -= amount   
            return self
    
# method to display account balance 
    def display_account_info(self): 
        return f"{self.balance}"
    
# methond to yield_interst
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate 
            return self
    
    @classmethod
    def print_all_accounts(cls):
            for account in cls.accounts:
                account.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        
    #creates checking account for user 
    def create_checking(self, balance): 
        self.checking = BankAccount(balance, 2/100) # variable set to a Bankaccount class

    # creates saving account
    def create_savings(self, balance):
        self.saving = BankAccount(balance, 3/100) #variable set to a Bankaccount class

    # display user balance of both savings and checking account
    def display_user_balance(self):
        print(f"User: {self.name}, savings balance: {self.saving.display_account_info()} | checking balance: {self.checking.display_account_info()}")
        return self
        

Amee= User("Amee") # User" class is assigened to object "Amee"

Amee.create_checking(1000)     # creating a checking account with starting balance $1000
Amee.checking.withdraw(100)     # withdraw 100 from checking

Amee.create_savings(3000)  #creating a checking account with starting balance $1000
Amee.saving.yield_interest() # savings yeid interst using "BankAccont" class method

Amee.display_user_balance()  # OUTPUT: User: Amee, savings: 3090.0 | checking: 900