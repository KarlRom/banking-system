from domain import Account, Customer

class AccountService:
    def __init__(self):
        self.accounts = {}
        self.customers = {}

    def create_account(self, customer_id, name, email, phone_number, account_number):
        customer = Customer(customer_id, name, email, phone_number)
        account = Account(len(self.accounts) + 1, customer_id, account_number, 0.0)
        self.customers[customer_id] = customer
        self.accounts[account.account_id] = account
        return account

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found")

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")
    
    def generate_account_statement(self, account_id):
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found")
        return f"Account {account.account_number} has a balance of {account.get_balance()}."