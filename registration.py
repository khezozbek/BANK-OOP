from bank_account import BankAccount
def register_account(account_number, account_holder, initial_balance):
    account = BankAccount(account_number, account_holder, initial_balance)
    return account
