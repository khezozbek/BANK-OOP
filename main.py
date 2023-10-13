from registration import register_account
from money_transfer import transfer_funds

# Register accounts
account1 = register_account("123456789", "John Doe", 100.0)
account2 = register_account("987654321", "Jane Smith", 50.0)

transfer_funds(account1, account2, 75.0)

# Get account balances
account1.get_balance()
account2.get_balance()
