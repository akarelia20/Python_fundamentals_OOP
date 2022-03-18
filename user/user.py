class User:
    def __init__(self,name,user_balance ):
        self.name = name
        self.user_balance = user_balance

    def make_deposit(self, amount): 
        self.user_balance += amount

    def make_withdrawal(self, amount):
        self.user_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.user_balance}")
        
    def transfer_money(self, other_user, amount):
        self.user_balance -= amount
        other_user.user_balance += amount


Megan = User("Megan Hill", 300) # Megan has 300
David = User("David python", 100) # David has 100
Charlie= User("Charlie Thompson", 300) #Charlie has 300

Megan.make_deposit(100) 
Megan.make_deposit(50)
Megan.make_deposit(100)
Megan.make_withdrawal(250)
Megan.display_user_balance() # Output: User:Megan Hill, Balance: 300

David.make_deposit(50) 
David.make_deposit(200)
David.make_withdrawal(100)
David.make_withdrawal(100)
David.display_user_balance() # Output: User: David python, Balance: 150

Charlie.make_deposit(200)
Charlie.make_withdrawal(100)
Charlie.make_withdrawal(100)
Charlie.make_withdrawal(100)
Charlie.display_user_balance() # Output: User: Charlie Thompson, Balance: 200

Megan.transfer_money(Charlie, 100) # Megan transfers 100 to charlie

Megan.display_user_balance() # Output: User: Megan Hill, Balance: 200
Charlie.display_user_balance() # Output: User: Charlie Thompson, Balance: 300