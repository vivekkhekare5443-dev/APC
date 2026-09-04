products = []


def add_product(name, price, quantity):
    products.append((name, price, quantity))


def remove_product(name):
    for product in products:
        if product[0] == name:
            products.remove(product)
            break


def subtotal():
    return sum(price * quantity for name, price, quantity in products)


def coupon_discount(amount):
    if amount >= 5000:
        return amount * 0.20
    elif amount >= 2000:
        return amount * 0.10
    else:
        return 0


def calculate_gst(amount):
    return amount * 0.18


def invoice():
    sub = subtotal()
    discount = coupon_discount(sub)
    taxable = sub - discount
    gst = calculate_gst(taxable)

    final = taxable + gst

    print("\n--- INVOICE ---")
    for name, price, quantity in products:
        print(name, "₹", price, "x", quantity)

    print("Subtotal = ₹", sub)
    print("Discount = ₹", discount)
    print("GST = ₹", gst)
    print("Final Amount = ₹", final)


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)

invoice()