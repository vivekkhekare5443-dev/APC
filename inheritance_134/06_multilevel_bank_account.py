"""
Inheritance - Program 6 (Multilevel Inheritance):
Create a base class BankAccount with account number and balance.
Derive SavingsAccount from it with an interest rate.
Further derive PremiumSavingsAccount with additional benefits.
Define methods to calculate interest and display account details.
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : Rs. {self.balance:,.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # Annual percentage

    def calculate_interest(self):
        return (self.balance * self.interest_rate) / 100

    def display_details(self):
        super().display_details()
        print(f"Interest Rate  : {self.interest_rate}% per annum")
        print(f"Annual Interest: Rs. {self.calculate_interest():,.2f}")


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, cashback_percent, free_lounge_access):
        super().__init__(account_number, balance, interest_rate)
        self.cashback_percent = cashback_percent
        self.free_lounge_access = free_lounge_access

    def display_details(self):
        print("=== Premium Savings Account Details ===")
        super().display_details()
        print(f"Cashback Rate  : {self.cashback_percent}% on debit spends")
        print(f"Airport Lounge : {self.free_lounge_access} free visits per quarter")


if __name__ == "__main__":
    acc = PremiumSavingsAccount("SB-78901234", 250000.0, 5.5, 2.0, 4)
    acc.display_details()
