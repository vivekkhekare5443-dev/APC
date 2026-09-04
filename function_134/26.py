def calculate_bill(units):
    if units <= 100:
        energy = units * 5
    elif units <= 200:
        energy = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        energy = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        energy = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12

    fixed_charge = 100
    subtotal = energy + fixed_charge

    tax = subtotal * 0.05
    discount = subtotal * 0.10 if units < 100 else 0

    final_bill = subtotal + tax - discount

    return final_bill


units = int(input("Enter units consumed: "))

print("Final Electricity Bill = ₹", calculate_bill(units))