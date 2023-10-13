from bank_account import BankAccount

def transfer_funds(sender, recipient, amount):
    if not sender.is_blocked:
        if sender.balance >= amount:
            sender.withdraw(amount)
            recipient.deposit(amount)
            print(f"Funds transferred successfully from {sender.account_number} to {recipient.account_number}.")
        else:
            print("Insufficient funds for transfer.")
    else:
        print("Sender account is blocked. Transfer not allowed.")
