from domain import Account, Customer
from infrastructure import AccountRepository

class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer_id, name, email, phone_number, account_number):
        customer = Customer(customer_id, name, email, phone_number)
        account = Account(len(self.account_repository.accounts) + 1, customer_id, account_number, 0.0)
        self.account_repository.save_account(account)
        return account

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")
    
    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        statement = f"Account Statement for Account {account.account_number}:\n"
        statement += "\n".join(account.transactions) if account.transactions else "No transactions found."
        return statement
