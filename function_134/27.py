def consultation_charges():
    return 500


def laboratory_charges():
    return 1000


def medicine_charges():
    return 1500


def room_charges(days):
    return days * 2000


def final_bill(category, days):
    consultation = consultation_charges()
    laboratory = laboratory_charges()
    medicine = medicine_charges()
    room = room_charges(days)

    total = consultation + laboratory + medicine + room

    if category.lower() == "senior":
        discount = total * 0.20
    elif category.lower() == "regular":
        discount = total * 0.05
    else:
        discount = 0

    return total - discount


category = input("Enter patient category: ")
days = int(input("Enter room days: "))

print("Final Bill = ₹", final_bill(category, days))