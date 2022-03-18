class User:
    def __init__(self, name , user_balance):
        self.name = name
        self.user_balance = user_balance

    def make_deposit(self, amount): 
        self.user_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.user_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.user_balance}")
        return self
        
    def transfer_money(self, other_user, amount):
        self.user_balance -= amount
        other_user.user_balance += amount
        return self

# assigning User class to instances/objects and passing required conditions such as name and balance.
Megan = User("Megan Hill", 300) 
David = User("David python", 100) 
Charlie= User("Charlie Thompson", 300)

#chaining mathod displayed below
# Output: User:Megan Hill, Balance: 300
Megan.make_deposit(100).make_deposit(50).make_deposit(100).make_withdrawal(250).display_user_balance() 

# Output: User: David python, Balance: 150
David.make_deposit(50).make_deposit(200).make_withdrawal(100).make_withdrawal(100).display_user_balance() 

# Output: User: Charlie Thompson, Balance: 200
Charlie.make_deposit(200).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# Megan transfers 100 to charlie using class method 
# Output: User: Megan Hill, Balance: 200
Megan.transfer_money(Charlie, 100).display_user_balance() 

# After receiving 100 from Megan , 
# Output: User: Charlie Thompson, Balance: 300
Charlie.display_user_balance() 

