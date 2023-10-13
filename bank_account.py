class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.is_blocked = False

    def deposit(self, amount):
        if not self.is_blocked:
            self.balance += amount
            print(f"Deposited {amount} into the account. New balance: {self.balance}")
            if self.balance <= -0.01:
                self.is_blocked = True
                print("Account blocked due to negative balance.")
        else:
            print("Account is blocked. Deposit not allowed.")

    def withdraw(self, amount):
        if not self.is_blocked:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from the account. New balance: {self.balance}")
                if self.balance <= -0.01:
                    self.is_blocked = True
                    print("Account blocked due to negative balance.")
            else:
                print("Insufficient funds!")
        else:
            print("Account is blocked. Withdrawal not allowed.")

    def get_balance(self):
        print(f"Account balance: {self.balance}")

    def is_account_blocked(self):
        return self.is_blocked
