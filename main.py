class Account:

    # constructor
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # string representation
    def __repr__(self):
        return f'Account owner:{self.owner}\nAccount balance: {self.balance}$'

    def deposit(self, money=0):  # deposit function
        self.money = money
        return 'deposit accepted'

    def withdraw(self, draw):    # withdraw function
        self.draw = draw
        if self.draw <= self.balance:
            print('Withdraw Accepted')
        else:
            print('Funds unavailable!!!')


# testing
Rachel_account = Account('Rachel Mulumba <=> savings account\n______________________________',                       10000)
print(Rachel_account)
# making deposit
print(Rachel_account.deposit(200))
# making withdraw amount that is available
print(Rachel_account.withdraw(500))
# making withdraw amount that is not available
print(Rachel_account.withdraw(20000))
