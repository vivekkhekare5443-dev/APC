"""
Abstraction - Program 8:
Create an abstract class Authentication with an abstract method authenticate().
Implement the method using:
a) Password authentication
b) OTP authentication
c) Biometric authentication
Demonstrate abstraction by interacting with objects through the abstract interface.
"""

from abc import ABC, abstractmethod

class Authentication(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def authenticate(self, credential):
        """Abstract method to verify supplied credential against identity."""
        pass


class PasswordAuthentication(Authentication):
    def __init__(self, username, registered_password_hash):
        super().__init__(username)
        self.registered_password_hash = registered_password_hash

    def authenticate(self, credential):
        # Simulated hashed comparison
        if credential == self.registered_password_hash:
            return True, f"[Password Auth] Password verified successfully for '{self.username}'."
        return False, f"[Password Auth] Access Denied! Incorrect password for '{self.username}'."


class OTPAuthentication(Authentication):
    def __init__(self, username, phone_number, expected_otp="482910"):
        super().__init__(username)
        self.phone_number = phone_number
        self.expected_otp = expected_otp

    def authenticate(self, credential):
        if str(credential).strip() == self.expected_otp:
            return True, f"[OTP Auth] One-Time Password verified for phone {self.phone_number}."
        return False, f"[OTP Auth] Access Denied! Expired or mismatched OTP."


class BiometricAuthentication(Authentication):
    def __init__(self, username, registered_fingerprint_id):
        super().__init__(username)
        self.registered_fingerprint_id = registered_fingerprint_id

    def authenticate(self, credential):
        if credential == self.registered_fingerprint_id:
            return True, f"[Biometric Auth] Capacitive fingerprint match confirmed for '{self.username}'."
        return False, f"[Biometric Auth] Access Denied! Fingerprint pattern match failed."


def login_service(auth_provider: Authentication, submitted_credential):
    """
    Interacts with the user exclusively through the abstract Authentication interface.
    The caller does not need to know the internal cryptographic or hardware details.
    """
    success, message = auth_provider.authenticate(submitted_credential)
    status_icon = "SUCCESS" if success else "FAILED"
    print(f"[{status_icon}] User '{auth_provider.username}' -> {message}")
    return success


if __name__ == "__main__":
    pass_auth = PasswordAuthentication("aarav_admin", "Secr3tP@ss")
    otp_auth = OTPAuthentication("diya_patel", "+91-9876543210", expected_otp="654321")
    bio_auth = BiometricAuthentication("rohan_verma", "FP_SENSOR_HASH_9918")

    print("=== Uniform Security Gateway (Interacting via Abstract Interface) ===")
    login_service(pass_auth, "Secr3tP@ss")
    login_service(pass_auth, "WrongPassword")
    print()
    login_service(otp_auth, "654321")
    login_service(otp_auth, "000000")
    print()
    login_service(bio_auth, "FP_SENSOR_HASH_9918")
    login_service(bio_auth, "FOREIGN_PRINT_ID")
