#This code uses the basic principles of object- oriented programming.
#Includes polymorphism, encapsulation, inheritance, abstraction

class Bank:
    accounts = 0
    @classmethod
    def __init__(self, username, password):
        self.username = username
        self.password = password
        Bank.accounts += 1

    def __del__(self):
        del self
        Bank.accounts-=1

    def __str__(self):
        return "You are logged in as {}".format(self.username)

    __repr__= __str__

class Customer(Bank):
    def __init__(self, username, password, balance):
        Bank.__init__(self, username, password)
        self.balance = balance

    def withdraw(self, amount):
        if amount> self.balance:
            print("You do not have enough!")
        else:
            self.balance-= amount
            print("Withdrawing {} dollars".format(amount))
            return self.balance

    def deposit(self, amount):
        self.balance+= amount
        print("Depositing {} dollars".format(amount))
        return self.balance

    def current_balance(self):
        return self.balance

class Manager(Bank):
    def __init__(self, username, password):
        Bank.__init__(self, username, password)

class BankTeller(Bank):
    def __init__(self, username, password):
        Bank.__init__(self, username, password)


