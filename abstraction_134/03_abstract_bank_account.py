"""
Abstraction - Program 3:
Create an abstract class BankAccount with abstract methods deposit() and withdraw().
Derive SavingsAccount and CurrentAccount and implement the required operations.
"""

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_no, holder_name, balance=0.0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = float(balance)

    @abstractmethod
    def deposit(self, amount):
        """Abstract deposit operation."""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Abstract withdrawal operation."""
        pass

    def display_balance(self):
        print(f"[{self.__class__.__name__}] Acc: {self.account_no} ({self.holder_name}) | Balance: Rs. {self.balance:,.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance=0.0, min_balance=1000.0):
        super().__init__(account_no, holder_name, balance)
        self.min_balance = min_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[Savings Deposit] Credited Rs. {amount:,.2f}. Updated Balance: Rs. {self.balance:,.2f}")
        else:
            print("[Savings Deposit] Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("[Savings Withdraw] Invalid withdrawal amount.")
        elif (self.balance - amount) >= self.min_balance:
            self.balance -= amount
            print(f"[Savings Withdraw] Debited Rs. {amount:,.2f}. Updated Balance: Rs. {self.balance:,.2f}")
        else:
            print(f"[Savings Withdraw] REJECTED! Must maintain minimum balance of Rs. {self.min_balance:,.2f}.")


class CurrentAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance=0.0, overdraft_limit=25000.0):
        super().__init__(account_no, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[Current Deposit] Credited Rs. {amount:,.2f}. Updated Balance: Rs. {self.balance:,.2f}")
        else:
            print("[Current Deposit] Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("[Current Withdraw] Invalid withdrawal amount.")
        elif (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"[Current Withdraw] Debited Rs. {amount:,.2f}. Updated Balance: Rs. {self.balance:,.2f}")
            if self.balance < 0:
                print(f"  Note: Overdraft utilized: Rs. {abs(self.balance):,.2f}")
        else:
            print(f"[Current Withdraw] REJECTED! Exceeds maximum overdraft limit of Rs. {self.overdraft_limit:,.2f}.")


if __name__ == "__main__":
    print("=== Testing Savings Account (With Min Balance Rule) ===")
    sa = SavingsAccount("SB-101", "Aarav Sharma", balance=5000.0, min_balance=1000.0)
    sa.display_balance()
    sa.deposit(2000.0)
    sa.withdraw(5500.0)  # Allowed, balance becomes 1500 (>= 1000)
    sa.withdraw(1000.0)  # Rejected, violates min balance

    print("\n=== Testing Current Account (With Overdraft Feature) ===")
    ca = CurrentAccount("CA-202", "Nova Enterprise", balance=10000.0, overdraft_limit=20000.0)
    ca.display_balance()
    ca.withdraw(25000.0) # Allowed with overdraft, balance becomes -15000
    ca.deposit(30000.0)  # Restores positive balance
