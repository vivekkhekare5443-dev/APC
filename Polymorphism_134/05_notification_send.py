"""
Polymorphism - Program 5:
Create a base class Notification with a method send().
Derive EmailNotification, SMSNotification, and PushNotification.
Override send() to display the appropriate notification method.
"""

class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        print(f"Sending generic notification to {self.recipient}: {self.message}")


class EmailNotification(Notification):
    def __init__(self, recipient, message, subject="Important Notice"):
        super().__init__(recipient, message)
        self.subject = subject

    def send(self):
        print(f"[Email Notification] To: {self.recipient} | Subject: '{self.subject}'")
        print(f"  Body: \"{self.message}\" (Delivered via SMTP)")


class SMSNotification(Notification):
    def __init__(self, recipient, message, sender_id="GOVIND"):
        super().__init__(recipient, message)
        self.sender_id = sender_id

    def send(self):
        print(f"[SMS Notification] From: {self.sender_id} -> To: {self.recipient}")
        print(f"  Text: \"{self.message}\" (Delivered via Telecom SMS Gateway)")


class PushNotification(Notification):
    def __init__(self, recipient, message, device_token):
        super().__init__(recipient, message)
        self.device_token = device_token

    def send(self):
        print(f"[Push Notification] User: {self.recipient} (Device: {self.device_token[:8]}...)")
        print(f"  Banner Alert: \"{self.message}\" (Delivered via Firebase/APNs)")


def dispatch_notification(notification_obj):
    """Polymorphic helper function that triggers send() regardless of notification type."""
    notification_obj.send()


if __name__ == "__main__":
    notifications = [
        EmailNotification("student@apccollege.edu", "Your semester results are out!", subject="Grade Card Published"),
        SMSNotification("+91-9876543210", "Your OTP for login is 482910. Do not share it."),
        PushNotification("manju_07", "You have a new assignment submitted.", device_token="fcm-token-98421098412")
    ]

    print("=== Multi-Channel Notification Dispatcher (Polymorphism) ===")
    for notif in notifications:
        dispatch_notification(notif)
        print()
