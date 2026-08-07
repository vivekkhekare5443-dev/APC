email = input("Enter email address: ")
if email.count('@') == 1 and '.' in email[email.index('@'):]:
    name, domain = email.split('@')
    if name and domain and domain.count('.') >= 1 and not domain.startswith('.') and not domain.endswith('.'):
        print("Valid email")
    else:
        print("Invalid email")
else:
    print("Invalid email")