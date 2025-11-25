class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Returns True if successful, False otherwise."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance}")
