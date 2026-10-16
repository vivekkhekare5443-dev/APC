"""
Polymorphism - Program 12:
Develop an online shopping payment module using polymorphism.
Create a base class Payment and derived classes UPIPayment, CardPayment, and WalletPayment.
Each class should implement its own make_payment() method.
Demonstrate polymorphism using a common function.
"""

class Payment:
    def __init__(self, payer_name):
        self.payer_name = payer_name

    def make_payment(self, amount):
        raise NotImplementedError("Subclasses must implement make_payment()")


class UPIPayment(Payment):
    def __init__(self, payer_name, upi_id):
        super().__init__(payer_name)
        self.upi_id = upi_id

    def make_payment(self, amount):
        print(f"[UPI Gateway] Initiating payment of Rs. {amount:,.2f} for {self.payer_name}...")
        print(f"  Request sent to VPA: {self.upi_id}")
        print("  Status: PIN verified! Payment successful via NPCI UPI network.")


class CardPayment(Payment):
    def __init__(self, payer_name, card_number, card_type="Credit Card"):
        super().__init__(payer_name)
        self.masked_card = f"XXXX-XXXX-XXXX-{card_number[-4:]}"
        self.card_type = card_type

    def make_payment(self, amount):
        print(f"[Card Gateway] Charging Rs. {amount:,.2f} to {self.payer_name}'s {self.card_type} ({self.masked_card})...")
        print("  Validating CVV and requesting 3D Secure OTP...")
        print("  Status: Authorized by Issuer Bank! Transaction ID: TXN_CARD_78912.")


class WalletPayment(Payment):
    def __init__(self, payer_name, wallet_service, wallet_balance):
        super().__init__(payer_name)
        self.wallet_service = wallet_service
        self.wallet_balance = wallet_balance

    def make_payment(self, amount):
        print(f"[{self.wallet_service} Wallet] Processing debit of Rs. {amount:,.2f} for {self.payer_name}...")
        if self.wallet_balance >= amount:
            self.wallet_balance -= amount
            print(f"  Status: Debited successfully! Remaining Wallet Balance: Rs. {self.wallet_balance:,.2f}")
        else:
            print("  Status: FAILED! Insufficient wallet balance.")


def checkout(payment_method, order_amount):
    """
    Common polymorphic payment processing function.
    Treats any payment subclass uniformly.
    """
    print(f"--- Processing Order of Rs. {order_amount:,.2f} ---")
    payment_method.make_payment(order_amount)
    print("-" * 55)


if __name__ == "__main__":
    upi = UPIPayment("Manjunath", "manju07@okhdfcbank")
    card = CardPayment("Diya Patel", "4111222233339081", "Visa Debit Card")
    wallet = WalletPayment("Aarav Sharma", "Paytm", wallet_balance=5000.0)

    print("=== E-Commerce Polymorphic Payment Gateway ===")
    checkout(upi, 1250.0)
    checkout(card, 8990.0)
    checkout(wallet, 2400.0)
