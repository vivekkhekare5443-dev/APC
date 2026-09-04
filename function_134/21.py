def total_bill(prices, quantities):
    total = 0

    for price, quantity in zip(prices, quantities):
        total += price * quantity

    discount = total * 0.10
    return total - discount

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))

print("Final Bill = ₹", total_bill(prices, quantities))