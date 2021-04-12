class User:
    def __init__(self, name):
        self.name = name
        self.balance = 10000
    
    def make_deposit(self,amount):
        if amount <= 0:
            print('The amount must be greater than zero')
        else:    
            self.balance += amount
        return self
    def make_withdrawal(self, amount):
        if amount > self.balance:
            print('You have no money enough')
        else:
            self.balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name} has ${self.balance}")
    def transfer_money(self, amount, user):
        self.balance -= amount
        user.balance += amount
        print(f"Transfer process ${amount} successfully to {user.name}")
        return self
user1 = User(name='Mohammed')
user2 = User(name='Faisal')
user3 = User(name="khaled")
user1.display_user_balance()
user1.make_deposit(0)
user1.transfer_money(300, user2)
user2.display_user_balance()

    
        