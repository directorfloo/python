class Account:
    def __init__(self, name, balance, number=8104676967):
        self.name = name
        self.balance = balance
        self.number = number

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        if amount < 499:
            raise Exception('Balance must be at least 499')
        elif amount < self.balance:
            raise Exception('New balance cannot be less than current balance')
        self.balance = amount

    def get_number(self):
        return self.number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise Exception('Deposit must be positive')

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
        else:
            raise Exception('Insufficient balance')
