# Object Oriented Programming (oop) checkpoint
class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposite(self, deposite_amount):
        self.account_balance += deposite_amount
        return f"You have just deposited {deposite_amount} and your new balance is {round(self.account_balance, 2)}"

    def withdrew(self, withdrew_amount):
        if self.account_balance > withdrew_amount:
            self.account_balance -= withdrew_amount
            return f"You've withdrawn {withdrew_amount} and your new balance is {self.account_balance}"
        else:
            return f"Insufficient Funds"

    def check_balance(self):
        return f"Your current Balance is {self.account_balance}"

    def __str__(self):
        return f"Account name: {self.account_holder}\n Account: {self.account_number}\n Account Balance: {self.account_balance}"



acct001 = Account(account_number="0011", account_balance=10000.00, account_holder="John")
acct002 = Account(account_number="0012", account_balance=20000.00, account_holder="Peter")
acct003 = Account(account_number="0013", account_balance=5000.00, account_holder="James")


print(acct001.deposite(100), "\n")

print(acct001.deposite(200), "\n")

print(acct002.withdrew(500), "\n\n", acct002.account_balance)