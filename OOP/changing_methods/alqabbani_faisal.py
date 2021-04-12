class User:
    def __init__(self, name):
        self.name = name
        self.balance = 10000
    # deposit method
    def make_deposit(self,amount):
        if amount <= 0:
            print('The amount must be greater than zero')
        else:    
            self.balance += amount
        return self
    #withdrwa method
    def make_withdrawal(self, amount):
        if amount > self.balance:
            print('You have no money enough')
        else:
            self.balance -= amount
        return self
    #display user balance
    def display_user_balance(self):
        print(f"{self.name} has ${self.balance}")
        return self
    #transfer money to another user
    def transfer_money(self, amount, user):
        self.balance -= amount
        user.balance += amount
        print(f"Transfer process ${amount} successfully to {user.name}")
        return self
# first instance from object
user1 = User(name='Mohammed')
user2 = User(name='Faisal')
user3 = User(name="khaled")
user1.display_user_balance().make_deposit(400).make_withdrawal(300).display_user_balance()

    
        