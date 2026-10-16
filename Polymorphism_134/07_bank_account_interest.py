"""
Polymorphism - Program 7:
Create a base class BankAccount with a method calculate_interest().
Derive SavingsAccount, CurrentAccount, and FixedDepositAccount.
Override the method to calculate interest differently for each account type.
"""

class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def calculate_interest(self):
        """Base interest calculation."""
        return 0.0


class SavingsAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance, interest_rate=4.0):
        super().__init__(account_no, holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        # Simple interest based on savings rate
        return (self.balance * self.interest_rate) / 100


class CurrentAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance, overdraft_limit=50000):
        super().__init__(account_no, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        # Current accounts in India typically earn 0% interest
        return 0.0


class FixedDepositAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance, tenure_years=3, fd_rate=7.25):
        super().__init__(account_no, holder_name, balance)
        self.tenure_years = tenure_years
        self.fd_rate = fd_rate

    def calculate_interest(self):
        # Compounded annually: A = P(1 + r/100)^t - P
        compounded_amount = self.balance * ((1 + (self.fd_rate / 100)) ** self.tenure_years)
        return compounded_amount - self.balance


if __name__ == "__main__":
    accounts = [
        SavingsAccount("SA-1001", "Neha Deshmukh", balance=150000.0, interest_rate=4.5),
        CurrentAccount("CA-2002", "Apex Tech Solutions", balance=480000.0),
        FixedDepositAccount("FD-3003", "Grandpa Joshi", balance=200000.0, tenure_years=3, fd_rate=7.5)
    ]

    print("=== Annual Interest Computation across Account Types ===")
    for acc in accounts:
        acc_type = type(acc).__name__
        interest = acc.calculate_interest()
        print(f"[{acc_type:<19}] Account: {acc.account_no} ({acc.holder_name})")
        print(f"  Balance: Rs. {acc.balance:,.2f} | Accrued Interest: Rs. {interest:,.2f}\n")
