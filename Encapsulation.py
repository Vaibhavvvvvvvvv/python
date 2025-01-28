class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):  # Fix the parameter name
        self.__balance += amount  # Correctly add the amount

    def get_balance(self):
        return self.__balance  # Return the private balance securely

# Create an account object
account = BankAccount("Vaibhav", 1000)
account.deposit(500)  # Deposit 500 into the account
print(account.get_balance())  # Output: 1500
