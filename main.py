from use_cases import AccountService

def main():
    service = AccountService()

    #Creates new account
    account = service.create_account(1, "John Doe", "john@example.com", "1234567890", "123-456-789")
    print(f"Created account: {account.account_number} with balance {account.get_balance()}")

    #Make transactions
    service.make_transaction(account.account_id, 500, 'deposit')
    print(service.generate_account_statement(account.account_id))

    service.make_transaction(account.account_id, 200, 'withdraw')
    print(service.generate_account_statement(account.account_id))

if __name__ == "__main__":
    main()