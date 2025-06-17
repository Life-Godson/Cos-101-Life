: class Account:
    def _init_(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.display_balance()
: class CurrentAccount("account"):
    # Inherits deposit method from Account
    pass
: class SavingsAccount("account"):
    # Inherits deposit method from Account
    pass
