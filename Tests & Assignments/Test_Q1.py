from dataclasses import dataclass

@dataclass
class Bank:
    """
    Bank class to represent a bank of transactions involving people.
    """
    accounts: dict = None
    account_number: int = 0

    def __post_init__(self):
        if self.accounts is None:
            self.accounts = {}

    def create_account(self, customer_name: str, initial_balance: int):
        """
        Creates a new account using information provided.
        :param customer_name: Customer name for the account.
        :param initial_balance: Initial balance for the account under that name.
        :return: Account number associated with the account.
        """
        self.account_number += 1
        self.accounts[self.account_number] = {'customer_name': customer_name, 'balance': initial_balance, 'history': []}
        return self.account_number

    def deposit(self, account_number: int, amount: int):
        """
        Deposits a new amount into the account with the given amount.
        :param account_number: Account number for the account to be deposited into.
        :param amount: Account number for the account to be deposited into.
        :return: None
        """
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.accounts[account_number]['history'].append(f"Deposit: +{amount}")
        else:
            print("Account not found.")

    def withdraw(self, account_number: int, amount: int):
        """
        Withdraws a ammount from the account with the given amount.
        :param account_number: Account number for the account to be deposited into.
        :param amount: Amount of money to be withdrawn from the account.
        :return: None
        """
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                self.accounts[account_number]['history'].append(f"Withdraw: -{amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def get_balance(self, account_number: int) -> int:
        """
        Returns the balance of an account.
        :param account_number: Account number for the balance to be returned from.
        :return: Balance of account.
        """
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            print("Account not found.")

    def get_transaction_history(self, account_number: int) -> list:
        if account_number in self.accounts:
            return self.accounts[account_number]['history']
        else:
            print("Account not found.")

@dataclass
class SavingsAccount(Bank):
    """
    A savings account class that inherits from Bank class.
    """
    interest_rate: float = 0.05  # Example interest rate

    def apply_interest(self, account_number: int):
        """
        Calculates the interest rate.
        :param account_number: Account number for the interest rate to be calculated and applied to.
        :return: None
        """
        if account_number in self.accounts:
            interest_amount = self.accounts[account_number]['balance'] * self.interest_rate
            self.accounts[account_number]['balance'] += interest_amount
            self.accounts[account_number]['history'].append(f"Interest applied: +{interest_amount}")
        else:
            print("Account not found.")

# Some trouble with this, and banking history.

bank = Bank()
bank.create_account('Alice', 500)

savings_account = SavingsAccount()
savings_account.interest_rate = 0.05
savings_account.create_account('Bob', 2000)
savings_account.deposit(1, 1000)  # Using the account number, not the name
savings_account.apply_interest(1)  # Using the account number, not the name
print(savings_account.get_balance(1))  # Using the account number, not the name
