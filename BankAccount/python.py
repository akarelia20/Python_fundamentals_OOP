class BankAccount():
    #empty list to store the instances/obj of the "BankAccount class"
    accounts = []
    def __init__(self, interest_rate, balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self) #appends/adds the each objects of this calss to "account" list

    # deposit method adds the amount to the total the balance
    def deposite (self, amount):
        self.balance += amount
        return self

    """
    decreases the account balance by the given amount if there are sufficient funds; 
    if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    """
    def withdraw(self, amount):
        if self.balance < amount:
            print(self.balance)
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5+ amount
            return self
        elif self.balance >= amount:
            self.balance -= amount
            return self

    # prints the account balance
    def display_account_info(self): 
        print(f"Balance: ${self.balance}")
        return self
    
    #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate 
            return self
    
    # loops through "acccount" list which containes all the objects of this class and print them.
    @classmethod
    def print_all_accounts(cls):
            for account in cls.accounts:
                account.display_account_info()
            


Amee_joint_saving = BankAccount(2/100,1000) 
Maria_checking = BankAccount(1/100,3000)

Amee_joint_saving.deposite(100).deposite(100).deposite(100).withdraw(300).yield_interest().display_account_info()

Maria_checking.deposite(500).deposite(500).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

BankAccount.print_all_accounts()

"""
output:
Balance: $1020.0
Balance: $2020.0
Balance: $1020.0
Balance: $2020.0
""" 