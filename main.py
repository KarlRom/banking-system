from use_cases import AccountService
from infrastructure import AccountRepository
from domain import Account

def main():
    repo = AccountRepository()  # Create repository
    service = AccountService(repo)  # Pass repository to service

    #Creates new account
    account = service.create_account(101, "John Doe", "john@example.com", "1234567890", "123-456-789")
    print(f"Created account: {account.account_number} with balance {account.get_balance()}")

    #Make transactions
    service.make_transaction(account.account_id, 500, 'deposit')
    service.make_transaction(account.account_id, 200, 'withdraw')

    statement = service.generate_account_statement(account.account_id)
    print("\n" + statement)

if __name__ == "__main__":
    main()
